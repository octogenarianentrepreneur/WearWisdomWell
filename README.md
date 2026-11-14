# WearWisdomWell.com — live site (Python generator)

This branch holds the source for the site currently live at https://wearwisdomwell.com (Netlify site c82e6b60-74b5-431a-b216-710713fea13f).
It replaced the Hugo version on `main` in Nov 2026; `main` is kept for reference.

- `catalog.py` — collections and products (names, Etsy listing IDs, prices, copy, colors)
- `posts.py` — journal articles
- `build.py` — builds every page into `dist/` (needs Python 3 + Pillow)
- `src/` — stylesheet and product images (`<slug>-1.jpg` … `-3.jpg`)

Build: `pip install pillow && python3 build.py`
Deploy: add `dist/netlify.toml` with `[build] publish = "." command = ""`, then deploy `dist/` to the Netlify site above.
GA4: G-TFHQS1BSD1 (buy_on_etsy is a key event).
