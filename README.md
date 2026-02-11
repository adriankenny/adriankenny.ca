# adriankenny.ca

Mirror of [adriankenny.ca](https://adriankenny.ca) (Framer-built). Pulled with a Site Sucker–style script: one HTML page plus all Framer assets (fonts, scripts, images) saved locally and linked with relative paths.

## Contents

- **index.html** — Full Framer page with rewritten asset URLs
- **assets/** — Fonts (.woff2), scripts (.mjs), images (.png), etc.
- **suck_site.py** — Script to re-pull the live site (run `python3 suck_site.py`)

## Run locally

Use a local server (required for module scripts):

```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

## Deploy on GitHub Pages

1. Push this repo to GitHub.
2. **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**, Folder: **/ (root)**.
3. Site: `https://adriankenny.github.io/adriankenny.ca/`.

## Re-pull the live site

To refresh the mirror from adriankenny.ca:

```bash
python3 suck_site.py
git add index.html assets/
git commit -m "Re-pull adriankenny.ca"
git push
```
