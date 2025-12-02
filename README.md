# Document Editor

Simple Flask app that provides a web-based rich text editor (Quill) so you can write and save HTML like a word document.

Quick start:

1. Create a virtualenv and install deps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open http://127.0.0.1:5000 in your browser. Use the editor and click Save. The saved HTML will be stored in `saved_doc.html` and can be opened with the "Open saved HTML" link.

## Deploying to GitHub Pages

This repository includes a GitHub Actions workflow that builds a static version of the Flask app and publishes it to the `gh-pages` branch.

What it does:

- Uses `build_static.py` to render `/` and `/saved` to static HTML into the `build/` folder and copies the `static/` folder.
- The workflow runs on push to `main` or `master` and deploys `build/` to GitHub Pages using `peaceiris/actions-gh-pages`.

How to enable:

1. Push this repo to GitHub (set the default branch to `main` if needed).
2. The workflow will run automatically on push and publish the site to GitHub Pages.
3. In your repository Settings → Pages, ensure the source is set to the `gh-pages` branch (the action will create/update this branch).

Local build:

Run the following to generate a `build/` folder locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build_static.py
```

The generated static site will be in `build/` and can be served with any static host.
