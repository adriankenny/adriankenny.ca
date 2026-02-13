#!/usr/bin/env python3
"""
Static site mirror helper: fetch a target URL and selected asset domains,
save locally, and rewrite HTML to use local asset paths.
"""
import re
import os
import hashlib
import urllib.request
import urllib.parse
import ssl
from pathlib import Path

TARGET_URL = "https://adriankenny.ca/"
OUT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = OUT_DIR / "assets"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

# Asset domains to mirror (keep external links untouched)
MIRROR_DOMAINS = ("framerusercontent.com", "adriankenny.ca")
# Skip noisy endpoints (analytics/events)
SKIP_PATTERNS = ("events.framer.com",)

def extract_urls(html: str) -> set:
    urls = set()
    for pattern in [
        r'href=["\'](https?://[^"\']+)["\']',
        r'src=["\'](https?://[^"\']+)["\']',
        r'url\((https?://[^)]+)\)',
        r'content=["\'](https?://[^"\']+)["\']',
    ]:
        urls.update(re.findall(pattern, html))
    return urls

def should_mirror(url: str) -> bool:
    if any(s in url for s in SKIP_PATTERNS):
        return False
    try:
        host = urllib.parse.urlparse(url).netloc
        return any(host.endswith(d) or host == d for d in MIRROR_DOMAINS)
    except Exception:
        return False

def url_to_local_path(url: str) -> Path:
    """Map URL to a local file path under assets/."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"
    # Sanitize: replace / with _ to avoid deep dirs; keep extension
    safe = path.replace("/", "_")[:200]
    ext = ".bin"
    if "." in safe:
        ext = "." + safe.rsplit(".", 1)[-1].split("?")[0]
    elif "woff2" in url:
        ext = ".woff2"
    elif "mjs" in url:
        ext = ".mjs"
    elif "png" in url or "jpg" in url or "jpeg" in url or "webp" in url or "gif" in url:
        ext = ".png" if "png" in url else ".jpg"
    name = hashlib.sha256(url.encode()).hexdigest()[:16] + ext
    return ASSETS_DIR / name

def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return r.read()

def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    print("Fetching", TARGET_URL)
    html = fetch(TARGET_URL).decode("utf-8", errors="replace")
    urls = extract_urls(html)
    to_mirror = sorted([u for u in urls if should_mirror(u)], key=len, reverse=True)
    print(f"Found {len(to_mirror)} assets to mirror (of {len(urls)} total URLs)")

    url_to_path = {}
    for i, url in enumerate(to_mirror):
        local = url_to_path.get(url)
        if local is None:
            local = url_to_local_path(url)
            url_to_path[url] = local
        if local.exists():
            continue
        try:
            data = fetch(url)
            local.write_bytes(data)
            print(f"  [{i+1}/{len(to_mirror)}] {local.name} ({len(data)} bytes)")
        except Exception as e:
            print(f"  FAIL {url[:60]}... : {e}")

    # Rewrite HTML: replace each mirrored URL with relative path
    rewritten = html
    for url in to_mirror:
        local = url_to_path[url]
        rel = "assets/" + local.name
        rewritten = rewritten.replace(url, rel)

    index_path = OUT_DIR / "index.html"
    index_path.write_text(rewritten, encoding="utf-8")
    print(f"Wrote {index_path} ({len(rewritten)} chars)")

if __name__ == "__main__":
    main()
