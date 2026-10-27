# Alkarar Arrow website

Static, bilingual (Arabic default, English) website for Alkarar Arrow (سهم الكرار).

## Structure
- `/` Arabic home, `/food/`, `/technology/`, `/contracting/`, `/privacy/`
- `/en/` English equivalents
- `assets/` CSS, JS, images. `sitemap.xml`, `robots.txt`, `404.html`, `site.webmanifest`
- `_headers` security and cache headers (Netlify / Cloudflare Pages)

## Editing
All page content lives in `build.py`. Edit the text, then run:

    python3 build.py

and commit the regenerated HTML. No dependencies.

## Hosting
Any static host. The pages use root-relative paths (`/assets/...`), so serve from a domain root
(e.g. sahmalkarar.sa), not a sub-folder.
