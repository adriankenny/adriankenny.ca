# adriankenny.ca

Static mirror of [adriankenny.ca](https://adriankenny.ca). This repo stores one HTML page and all required assets with relative paths so it can run locally or as a static deploy.

## Contents

- **index.html** — Mirrored page with rewritten asset URLs
- **assets/** — Fonts (.woff2), scripts (.mjs), images (.png), etc.
- **suck_site.py** — Script to refresh the live snapshot (run `python3 suck_site.py`)

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

## Contact form (“Looking to chat with me?”)

The contact form uses [Formspree](https://formspree.io) so submissions are sent to your email. To enable it:

1. Go to [formspree.io](https://formspree.io) and create a free account.
2. Create a new form and copy your form ID (e.g. `xjvqqlop` from `https://formspree.io/f/xjvqqlop`).
3. In **index.html**, search for `YOUR_FORM_ID` and replace it with your form ID (e.g. `action="https://formspree.io/f/xjvqqlop"`).

After that, form submissions will go to your Formspree inbox and you can forward them to your email.

## Re-pull the live site

To refresh the mirror from adriankenny.ca:

```bash
python3 suck_site.py
git add index.html assets/
git commit -m "Re-pull adriankenny.ca"
git push
```
