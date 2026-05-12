# 📚 Documentation (MkDocs Guide)

This project uses **MkDocs Material** to generate the documentation website from Markdown files.

## 🚀 What is MkDocs?

MkDocs is a static site generator that converts Markdown files into a documentation website.

In this project:
- Markdown files are stored in `docs/`
- MkDocs builds them into a static site in `site/`
- Flask serves the generated `site/` folder


## 📁 Project Structure

```
docs/               # Source Markdown files
  ├── index.md
  ├── introduction.md
  ├── usage.md
  ├── limitations.md
  └── resources.md


mkdocs.yml          # MkDocs configuration
site/               # Generated static site (DO NOT EDIT)

```

## ⚙️ How to Run Docs Locally

1. Install MkDocs
```
pip install mkdocs mkdocs-material
```
2. Start development server
```
mkdocs serve
```

Then open:
```
http://127.0.0.1:8000/
```


This auto-reloads when you edit Markdown files.

## 🏗️ Build Static Site

To generate the final documentation:
```
mkdocs build

This creates/updates the site/ folder.
```

## 🌐 How It Works with Flask

After building:

MkDocs generates static HTML in site/
Flask serves the site/ folder
Users access docs through Flask routes
```
Example:

/ → site/index.html
/usage/ → site/usage/index.html
```

## ✍️ Editing Documentation

To update docs:

Edit .md files inside docs/
Save changes

Run or refresh:
```
mkdocs serve
```
OR rebuild:
```
mkdocs build
```

## ⚠️ Important Notes
Never edit the site/ folder manually (it is generated)
Always edit Markdown files inside docs/
Rebuild after changes before deploying

## 🎨 Theme

This project uses:

MkDocs Material theme
Dark/light mode support
Sidebar navigation
Search functionality

## 🧠 Summary

MkDocs converts Markdown → static website → Flask serves it

