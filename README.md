# adriankenny.ca

Static portfolio site. Built with plain HTML and CSS for easy hosting and version control.

## Contents

- **index.html** — Main page (hero, work, contact)
- **styles.css** — Layout and typography (DM Sans, Instrument Serif)

Portfolio images are loaded from Framer’s CDN; links point to Dribbble, Figma, Instagram, Threads, Mastodon, and LinkedIn.

## Run locally

Open `index.html` in a browser, or use a simple server:

```bash
# Python 3
python3 -m http.server 8000

# Then open http://localhost:8000
```

## Deploy on GitHub Pages

1. Push this folder to a GitHub repo named `adriankenny.ca` (see below).
2. In the repo: **Settings → Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Branch: **main**, folder: **/ (root)**.
5. Save. The site will be at `https://adriankenny.github.io/adriankenny.ca/`.

## Put this site on GitHub

From your machine, in the folder that contains `index.html` and `styles.css`:

```bash
cd /path/to/adriankenny.ca
git init
git add .
git commit -m "Initial commit: portfolio site"
git branch -M main
git remote add origin https://github.com/adriankenny/adriankenny.ca.git
git push -u origin main
```

Create the repo on [github.com/new](https://github.com/new) with the name **adriankenny.ca** (no README or .gitignore), then run the commands above.
