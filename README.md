# Wear Wisdom Well — Hugo Site

Marketing site for OctogenarianEntrep / Wear Wisdom Well. Built with Hugo, deployed to Cloudflare Pages via GitHub.

**Tech stack:** Hugo · GitHub · Cloudflare Pages · Zero monthly cost

---

## One-Time Setup (20 minutes)

### 1. Install Hugo
Download from https://gohugo.io/installation/ — choose the **extended** edition.
Verify: `hugo version`

### 2. Create GitHub Repository
- Go to github.com → New repository
- Name: `wear-wisdom-well`
- Visibility: Public (required for free Cloudflare Pages)
- Copy this folder's contents into it and push to `main`

### 3. Connect Cloudflare Pages
- Go to dash.cloudflare.com → Pages → Create a project
- Connect your GitHub account → Select `wear-wisdom-well`
- Build settings:
  - **Framework preset:** Hugo
  - **Build command:** `hugo --minify`
  - **Build output directory:** `public`
  - **Environment variable:** `HUGO_VERSION` = `0.147.0`
- Click Save and Deploy — your site goes live in ~30 seconds

### 4. Add Your Domain (optional)
In Cloudflare Pages → Custom domains → add `wearwisdomwell.com`
Point your DNS CNAME to `wear-wisdom-well.pages.dev`

### 5. Add GitHub Secrets (for Actions deployment)
In GitHub repo → Settings → Secrets → Actions:
- `CF_API_TOKEN` — create at dash.cloudflare.com/profile/api-tokens
- `CF_ACCOUNT_ID` — found in Cloudflare dashboard right sidebar

---

## Adding New Products

Create a new file in `content/products/your-product-name.md`:

```yaml
---
title: "Your Product Title"
description: "One-sentence SEO description"
date: 2026-06-01
price: "22.44"
free_shipping: true
featured: true          # show on homepage (set false to hide)
bestseller: false       # show gold badge
collections: ["quiet-patriotism"]   # must match a folder name in collections/
tags: ["patriotic", "gift", "unisex"]
image: "https://i.etsystatic.com/..."   # paste og:image URL from the Etsy listing
etsy_url: "https://www.etsy.com/listing/..."
hook: "One italic sentence that captures the emotional hook."
signals:
  - What this design quietly communicates
  - Second signal
  - Third signal
---

Your product description in plain prose. Two or three paragraphs.
```

Push to GitHub → Cloudflare rebuilds automatically in ~30 seconds.

---

## Adding Blog Posts (Gift Guides)

Create `content/blog/your-post-title.md`:

```yaml
---
title: "Best Patriotic Shirts for People Who Don't Like to Argue"
description: "SEO meta description — 120–155 characters"
date: 2026-06-15
tags: ["gift guide", "patriotic", "quiet patriotism"]
---

Your post content in Markdown...
```

**Blog post ideas that drive organic traffic:**
- Best Patriotic T-Shirts That Aren't Loud
- Funny Retirement Gifts That Actually Get It Right
- Wisdom Quote Shirts for People Who've Earned It
- Best Gifts for People Who Believe in Faith Family Freedom
- Father's Day Gifts for Sarcastic Dads (already done)
- Mother's Day Gifts for the Woman Who Gets It

---

## Site Structure

```
hugo-site/
├── hugo.toml                  ← site config, update baseURL before launch
├── .github/workflows/
│   └── deploy.yml             ← auto-deploy on push to main
├── content/
│   ├── products/              ← one .md per Etsy listing
│   ├── collections/           ← one .md per collection
│   └── blog/                  ← gift guides and SEO content
├── layouts/                   ← Hugo templates
└── static/css/main.css        ← all styles — navy/gold brand
```

---

## SEO Keywords to Work Into Content

From the Website Fix Kit — blend these naturally:
- patriotic shirt · conservative apparel · faith family freedom
- thoughtful patriot · wisdom quote shirt · subtle conservative shirt
- family values apparel · liberty themed clothing
- Christian patriotic tee · retirement gift · funny dad gift
