#!/usr/bin/env python3
"""Build wearwisdomwell.com into ./dist. Usage: python3 build.py"""
import html, json, re, shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from catalog import COLLECTIONS, PRODUCTS, REDIRECTS, ETSY, CC1717_PRICES
from posts import POSTS

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"
SITE = "https://wearwisdomwell.com"
EMAIL = "info@OctogenarianEntrepreneur.com"
SHOP = "https://www.etsy.com/shop/WearWisdomWell"
TODAY = "2026-11-11"
GSV = "jnafY7VISnOXmhaeEXjdmL3bXL-lo9X2uV0H3y7feqE"

E = html.escape
COLL = {c["slug"]: c for c in COLLECTIONS}
PROD = {p["slug"]: p for p in PRODUCTS}
for c in COLLECTIONS:
    c["products"] = [p for p in PRODUCTS if p["collection"] == c["slug"]]

SIZE_CHART = [  # Comfort Colors 1717, inches (from the Printify size chart)
    ("Width", ["18.3", "20.3", "22.0", "24.0", "26.0", "27.8", "29.8"]),
    ("Length", ["26.6", "28.0", "29.4", "30.8", "31.6", "32.5", "33.5"]),
    ("Sleeve", ["16.3", "17.8", "19.0", "20.5", "21.8", "23.3", "24.6"]),
]

# ---------------------------------------------------------------- layout
def page(path, title, desc, body, *, og_image=None, ld=None, og_type="website", crumbs=None):
    canon = SITE + path
    og = SITE + "/img/" + (og_image or "og-default.jpg")
    lds = []
    if crumbs:
        lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList",
                    "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n,
                                         "item": SITE + u} for i, (n, u) in enumerate(crumbs)]})
    lds += ld or []
    ld_html = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    crumb_html = ""
    if crumbs and len(crumbs) > 1:
        parts = [f'<a href="{u}">{E(n)}</a>' for n, u in crumbs[:-1]] + [f"<span>{E(crumbs[-1][0])}</span>"]
        crumb_html = f'<nav class="crumbs" aria-label="Breadcrumb">{" / ".join(parts)}</nav>'
    out = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canon}">
<meta name="google-site-verification" content="{GSV}">
<meta property="og:site_name" content="WearWisdomWell"><meta property="og:type" content="{og_type}">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#1C2A39">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Playfair+Display:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TFHQS1BSD1"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-TFHQS1BSD1');</script>
{ld_html}
</head><body>
<div class="ship-bar">Free US shipping on orders of $35 or more · 30-day size exchanges</div>
<header class="site"><div class="wrap">
<a class="logo" href="/"><span class="mark">W</span>WearWisdomWell</a>
<nav aria-label="Main"><a href="/shop/">Shop</a><a href="/blog/">Journal</a><a href="/about/">About</a></nav>
</div></header>
<main class="wrap">{crumb_html}{body}</main>
<footer class="site"><div class="wrap">
<p class="sig">Wit for those wise enough to wear it.</p>
<nav aria-label="Footer"><a href="/shop/">Shop</a><a href="/blog/">Journal</a><a href="/about/">About</a><a href="/shipping-returns/">Shipping &amp; Returns</a><a href="/contact/">Contact</a><a href="{SHOP}">Our Etsy shop</a></nav>
<p class="small">Family-owned. Shirts printed on demand by Printify; checkout and payment are handled securely by Etsy.</p>
<p class="small">© 2026 WearWisdomWell — <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></footer>
<script>document.addEventListener('click',e=>{{const b=e.target.closest('a[data-etsy]');if(b&&window.gtag){{gtag('event','buy_on_etsy',{{etsy_listing_id:b.dataset.etsy,item_name:b.dataset.name,transport_type:'beacon'}});}}}});</script>
<script>document.addEventListener('click',e=>{{const t=e.target.closest('[data-swap]');if(!t)return;e.preventDefault();const m=document.getElementById('main-photo');m.src=t.dataset.swap;m.alt=t.querySelector('img').alt;document.querySelectorAll('[data-swap]').forEach(x=>x.classList.toggle('on',x===t));}});</script>
</body></html>"""
    dest = DIST / path.lstrip("/") / "index.html" if path.endswith("/") else DIST / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    return path

def img(file, alt, w=794, h=794, cls="", lazy=True):
    try:
        w, h = Image.open(SRC / "img" / file).size
    except Exception:
        pass
    return (f'<img src="/img/{file}" alt="{E(alt)}" width="{w}" height="{h}"'
            f'{" loading=\"lazy\"" if lazy else ""} decoding="async"{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>')

def price_label(p):
    return f"From ${p['price_from']}"

def card(p, lazy=True):
    return (f'<a class="card" href="/shop/{p["slug"]}/">{img(p["slug"] + "-1.jpg", p["alts"][0], lazy=lazy)}'
            f'<span class="card-body"><span class="card-title">{E(p["short"])}</span>'
            f'<span class="card-blurb">{E(p["blurb"])}</span>'
            f'<span class="card-price">{price_label(p)}</span></span></a>')

def grid(ps, lazy=True):
    return '<div class="grid">' + "".join(card(p, lazy) for p in ps) + "</div>"

def etsy(p):
    return ETSY.format(id=p["etsy_id"])

# ---------------------------------------------------------------- pages
def build_home():
    featured = [PROD[s] for s in ["know-more-than-i-say-tee", "old-and-wise-tee", "liberty-legacy-1776-2026-tee", "never-assume-donkey-tee"]]
    colls = "".join(
        f'<a class="coll" href="/shop/{c["slug"]}/">{img(c["products"][0]["slug"] + "-1.jpg", c["name"] + " collection")}'
        f'<span class="coll-name">{E(c["name"])}</span><span class="coll-short">{E(c["short"])}</span></a>'
        for c in COLLECTIONS)
    posts = "".join(post_teaser(x) for x in POSTS[:3])
    body = f"""
<section class="hero">
<h1>Subtle statements for people who don't need to argue.</h1>
<p class="lede">Understated graphic tees on faith, country and dry wit — set in quiet type on deep, washed cotton. For the one who'd rather be understood than seen.</p>
<p><a class="btn" href="/shop/">Browse the shirts</a> <a class="btn ghost" href="/blog/christmas-gifts-for-the-quiet-man/">Christmas gift guide</a></p>
</section>
<h2 class="section">Newest designs</h2>
{grid(featured, lazy=False)}
<h2 class="section">Collections</h2>
<div class="colls">{colls}</div>
<section class="promise">
<div><h3>Made when you order</h3><p>Printed on demand, so nothing sits in a warehouse. Ships in 3–5 business days.</p></div>
<div><h3>Checkout on Etsy</h3><p>Every Buy button opens the exact shirt on our Etsy shop, with Etsy Purchase Protection.</p></div>
<div><h3>Free US shipping at $35</h3><p>That's two shirts — one to keep, one for the friend who shares your outlook.</p></div>
</section>
<h2 class="section">From the journal</h2>
<div class="teasers">{posts}</div>
<section class="about-snip">
<h2>Some things don't need to be shouted.</h2>
<p>WearWisdomWell is a family-owned shop founded by an octogenarian entrepreneur, with decades behind it in farming, finance and real estate. Every design starts with one question: what does this quietly communicate? <a href="/about/">Our story</a>.</p>
</section>"""
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": "WearWisdomWell",
           "url": SITE + "/", "logo": SITE + "/apple-touch-icon.png", "email": EMAIL, "sameAs": [SHOP]},
          {"@context": "https://schema.org", "@type": "WebSite", "name": "WearWisdomWell", "url": SITE + "/"}]
    page("/", "WearWisdomWell | Subtle Statement Tees for Faith, Country and Dry Wit",
         "Understated graphic tees for people who don't need to argue: quiet patriotism, reflective faith and dry wit, from a family-owned shop.",
         body, ld=ld)

def build_shop():
    sections = "".join(
        f'<h2 class="section"><a href="/shop/{c["slug"]}/">{E(c["name"])}</a></h2><p class="muted">{E(c["short"])}</p>{grid(c["products"], lazy=i > 0)}'
        for i, c in enumerate(COLLECTIONS))
    body = f"""<h1>Shop</h1>
<p class="lede">All {len(PRODUCTS)} designs. Each page shows the price, sizes and colors; the Buy button opens that exact shirt on our Etsy shop for secure checkout.</p>
{sections}"""
    ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Shop WearWisdomWell",
           "url": SITE + "/shop/", "hasPart": [{"@type": "Product", "name": p["name"], "url": f"{SITE}/shop/{p['slug']}/"} for p in PRODUCTS]}]
    page("/shop/", "Shop Subtle Statement Tees | WearWisdomWell",
         "Every WearWisdomWell design: quiet patriotism, understated wit, reflective faith and thoughtful expression. Prices from $22.99.",
         body, ld=ld, crumbs=[("Home", "/"), ("Shop", "/shop/")])

def build_collections():
    for c in COLLECTIONS:
        others = " · ".join(f'<a href="/shop/{o["slug"]}/">{E(o["name"])}</a>' for o in COLLECTIONS if o is not c)
        body = f"""<h1>{E(c["name"])}</h1><p class="lede">{E(c["intro"])}</p>
{grid(c["products"], lazy=False)}
<p class="muted">Other collections: {others}</p>"""
        ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": c["name"], "description": c["intro"],
               "url": f"{SITE}/shop/{c['slug']}/",
               "hasPart": [{"@type": "Product", "name": p["name"], "url": f"{SITE}/shop/{p['slug']}/"} for p in c["products"]]}]
        page(f"/shop/{c['slug']}/", f"{c['name']} Tees | WearWisdomWell", c["intro"][:155], body,
             og_image=c["products"][0]["slug"] + "-1.jpg", ld=ld,
             crumbs=[("Home", "/"), ("Shop", "/shop/"), (c["name"], f"/shop/{c['slug']}/")])

def size_table():
    head = "".join(f"<th>{s}</th>" for s in ["S", "M", "L", "XL", "2XL", "3XL", "4XL"])
    rows = "".join(f"<tr><th>{n}</th>" + "".join(f"<td>{v}</td>" for v in vals) + "</tr>" for n, vals in SIZE_CHART)
    return (f'<div class="table-scroll"><table class="sizes"><caption>Comfort Colors 1717, inches, laid flat</caption>'
            f'<thead><tr><th></th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
            '<p class="small">Width is measured armpit to armpit. Measurements can vary by about 1.5 inches. '
            'Relaxed fit; if he\'s between sizes, his usual size is the safe choice.</p>')

def build_products():
    for p in PRODUCTS:
        c = COLL[p["collection"]]
        s = p["slug"]
        thumbs = "".join(
            f'<a href="/img/{s}-{i}.jpg" data-swap="/img/{s}-{i}.jpg" class="thumb{" on" if i == 1 else ""}">'
            + img(f"{s}-{i}.jpg", p["alts"][i - 1], lazy=False) + "</a>"
            for i in (1, 2, 3))
        paras = "".join(f"<p>{E(x)}</p>" for x in p["body"])
        price_line = (f"<strong>From ${p['price_from']}</strong> · {CC1717_PRICES}" if p["cc1717"]
                      else f"<strong>From ${p['price_from']}</strong> · larger sizes cost a little more")
        sizes = (f'<details class="sizechart"><summary>Size chart</summary>{size_table()}</details>' if p["cc1717"]
                 else f'<p class="small">Sizes {p["sizes"]}. The size chart is the last photo on the <a href="{etsy(p)}">Etsy listing</a>.</p>')
        quote = "" if p["body"][0][:18] == p["shirt_text"][:18] else f'<p class="shirt-text">“{E(p["shirt_text"])}”</p>'
        more = [x for x in c["products"] if x is not p][:3] or [x for x in PRODUCTS if x is not p][:3]
        body = f"""<article class="product">
<div class="gallery">{img(p["slug"] + "-1.jpg", p["alts"][0], cls="main", lazy=False).replace("<img ", '<img id="main-photo" ', 1)}
<div class="thumbs">{thumbs}</div></div>
<div class="info">
<h1>{E(p["name"]).replace("T-Shirt", "T&#8209;Shirt")}</h1>
{quote}
<p class="price">{price_line}</p>
<a class="btn buy" href="{etsy(p)}" data-etsy="{p['etsy_id']}" data-name="{E(p['short'])}">See sizes &amp; buy on Etsy</a>
<p class="small">Opens this shirt on our Etsy shop. Checkout, payment and Etsy Purchase Protection are handled by Etsy.</p>
{paras}
<p class="close">{E(p["close"])}</p>
<h2 class="h3">Details</h2>
<ul class="specs">
<li>{E(p["build"])}</li>
<li>Colors: {E(", ".join(p["colors"]))}</li>
<li>Made to order: ships in 3–5 business days, then about a week in transit (US economy)</li>
<li>Free US shipping on orders of $35 or more</li>
<li>Wrong size? <a href="/shipping-returns/">Exchange it within 30 days</a>; damaged or misprinted, we'll make it right</li>
</ul>
{sizes}
<p class="small">Questions before you order? <a href="/contact/">Send a message</a> — we usually reply within a day.</p>
</div></article>
<h2 class="section">More from {E(c["name"])}</h2>
{grid(more)}"""
        offer = {"@type": "Offer", "price": p["price_from"], "priceCurrency": "USD",
                 "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition",
                 "url": etsy(p), "priceValidUntil": "2027-06-30",
                 "seller": {"@type": "Organization", "name": "WearWisdomWell"}}
        ld = [{"@context": "https://schema.org", "@type": "Product", "name": p["name"],
               "description": " ".join(p["body"]), "sku": p["etsy_id"],
               "image": [f"{SITE}/img/{p['slug']}-{i}.jpg" for i in (1, 2, 3)],
               "brand": {"@type": "Brand", "name": "WearWisdomWell"}, "category": "Apparel > T-Shirts",
               "color": ", ".join(p["colors"]), "url": f"{SITE}/shop/{p['slug']}/", "offers": offer}]
        page(f"/shop/{p['slug']}/", f"{p['name']} | WearWisdomWell",
             f"{p['blurb']} {p['name'].replace(' T-Shirt', ' tee')}, from ${p['price_from']}. Printed to order; checkout on Etsy.",
             body, og_image=p["slug"] + "-1.jpg", ld=ld, og_type="product",
             crumbs=[("Home", "/"), ("Shop", "/shop/"), (c["name"], f"/shop/{c['slug']}/"), (p["short"], f"/shop/{p['slug']}/")])

def expand(body):
    def prod(m):
        p = PROD[m.group(1)]
        return (f'<a class="inline-prod" href="/shop/{p["slug"]}/">{img(p["slug"] + "-1.jpg", p["alts"][0])}'
                f'<span><strong>{E(p["name"])}</strong><span class="muted">{price_label(p)} · {E(COLL[p["collection"]]["name"])}</span></span></a>')
    body = re.sub(r"\{p:([a-z0-9-]+)\}", prod, body)
    body = re.sub(r"\{c:([a-z0-9-]+)\}", lambda m: f'<a href="/shop/{m.group(1)}/">{E(COLL[m.group(1)]["name"])}</a>', body)
    return body

def nice_date(d):
    y, m, dd = d.split("-")
    return f"{['January','February','March','April','May','June','July','August','September','October','November','December'][int(m)-1]} {int(dd)}, {y}"

def post_teaser(x):
    return (f'<a class="teaser" href="/blog/{x["slug"]}/">{img(x["image"], x["title"])}'
            f'<span class="muted small">{nice_date(x["date"])}</span><span class="teaser-title">{E(x["title"])}</span>'
            f'<span class="small">{E(x["desc"])}</span></a>')

def build_blog():
    for x in POSTS:
        words = len(re.sub(r"<[^>]+>", " ", x["body"]).split())
        body = f"""<article class="post">
<p class="muted small">{nice_date(x["date"])}{" · updated " + nice_date(x["modified"]) if x.get("modified") else ""} · {max(1, round(words / 230))} min read</p>
<h1>{E(x["title"])}</h1>
{img(x["image"], x["title"], cls="post-hero", lazy=False)}
{expand(x["body"])}
</article>
<h2 class="section">Keep reading</h2><div class="teasers">{"".join(post_teaser(o) for o in POSTS if o is not x)[:99999]}</div>"""
        ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": x["title"], "description": x["desc"],
               "image": f"{SITE}/img/{x['image']}", "datePublished": x["date"], "dateModified": x.get("modified", x["date"]),
               "author": {"@type": "Organization", "name": "WearWisdomWell"},
               "publisher": {"@type": "Organization", "name": "WearWisdomWell", "logo": {"@type": "ImageObject", "url": SITE + "/apple-touch-icon.png"}},
               "mainEntityOfPage": f"{SITE}/blog/{x['slug']}/", "wordCount": words}]
        page(f"/blog/{x['slug']}/", f"{x['seo_title']} | WearWisdomWell", x["desc"], body,
             og_image=x["image"], ld=ld, og_type="article",
             crumbs=[("Home", "/"), ("Journal", "/blog/"), (x["title"], f"/blog/{x['slug']}/")])
    body = f"""<h1>Journal</h1><p class="lede">Notes on quiet patriotism, reflective faith, dry wit and gifts for people who'd rather be understood than seen.</p>
<div class="teasers">{"".join(post_teaser(x) for x in POSTS)}</div>"""
    ld = [{"@context": "https://schema.org", "@type": "Blog", "name": "WearWisdomWell Journal", "url": SITE + "/blog/",
           "blogPost": [{"@type": "BlogPosting", "headline": x["title"], "url": f"{SITE}/blog/{x['slug']}/", "datePublished": x["date"]} for x in POSTS]}]
    page("/blog/", "Journal | WearWisdomWell", "Notes on quiet patriotism, reflective faith, dry wit and gift ideas from WearWisdomWell.",
         body, ld=ld, crumbs=[("Home", "/"), ("Journal", "/blog/")])

def build_info():
    page("/about/", "About WearWisdomWell | A Family-Owned Shop", "WearWisdomWell is a family-owned shop founded by an octogenarian entrepreneur. Subtle statements for people who don't need to argue.", f"""
<h1>About WearWisdomWell</h1>
<p class="lede">Some things don't need to be shouted.</p>
<p>WearWisdomWell makes thoughtful apparel for people who've lived long enough to have formed opinions — and are done explaining them. Our designs speak quietly, for those who prefer conviction over confrontation.</p>
<p>The shop was founded by an octogenarian entrepreneur, out of decades of lived experience in farming, finance, real estate and a great deal of practical problem-solving. It's family-owned and run the way that background would suggest: plainly, carefully, and with an eye on the details.</p>
<h2>What we make</h2>
<p>Graphic tees built around one question: what does this quietly communicate? Our collections cover the things that matter most to people who've earned the right to say so — patriotism without argument, faith without a sermon, humor without meanness, and the kind of wisdom that only comes from having been around long enough to know better.</p>
<h2>How it's made</h2>
<p>Every shirt is printed to order by our production partner, Printify, mostly on Comfort Colors 1717 — a soft, substantial garment-dyed cotton tee in deep, washed colors. We set the type ourselves and keep designs modest in size, so they read as considered rather than loud. Because nothing is printed until you order, there's no warehouse of unsold shirts.</p>
<h2>Why we sell through Etsy</h2>
<p>Etsy handles our checkout, payment and order tracking, and covers eligible orders with Etsy Purchase Protection. You browse here, and each Buy button takes you to that exact shirt on our Etsy shop.</p>
<p>The best statement a shirt can make is one that earns a slow nod from a stranger who gets it.</p>
<p><a class="btn" href="/shop/">Browse the shirts</a></p>
<p class="sig">Wear your convictions — gracefully.</p>""", crumbs=[("Home", "/"), ("About", "/about/")])

    page("/shipping-returns/", "Shipping & Returns | WearWisdomWell", "Shipping times, costs and our make-it-right promise for WearWisdomWell shirts, printed to order and sold on Etsy.", f"""
<h1>Shipping &amp; Returns</h1>
<h2>Shipping</h2>
<ul class="specs">
<li><strong>Made to order.</strong> Each shirt is printed when you order it. Allow 3–5 business days before it ships.</li>
<li><strong>Transit.</strong> US economy shipping usually takes about a week (4–8 business days). Faster standard shipping is offered at checkout.</li>
<li><strong>Cost.</strong> US economy shipping starts at $3.99 for the first shirt, with a smaller charge for each additional shirt. <strong>Orders of $35 or more ship free in the US.</strong></li>
<li><strong>Tracking.</strong> Etsy emails tracking as soon as your order ships. International shipping is available; Etsy shows the cost at checkout.</li>
<li><strong>Gifts.</strong> For Christmas, ordering by early December leaves comfortable room.</li>
</ul>
<h2>Exchanges and our make-it-right promise</h2>
<p><strong>Size exchanges within 30 days.</strong> If the size isn't right, message us through Etsy within 30 days of delivery and we'll exchange it for another size. Because each shirt is printed for you, we offer exchanges rather than refunds for change of mind; the buyer covers return shipping, and the shirt should come back unworn and in its original condition.</p>
<p><strong>Damaged or misprinted?</strong> <a href="/contact/">Message us</a> with a photo and we'll make it right at no cost to you. Eligible orders are also covered by <a href="https://www.etsy.com/purchase-protection">Etsy Purchase Protection</a>.</p>
<h2>Sizing</h2>
<p>Most of our shirts are Comfort Colors 1717, a relaxed fit:</p>
{size_table()}
<p>Not sure? Lay a shirt he already likes flat and measure across the chest, armpit to armpit, then compare.</p>""",
         crumbs=[("Home", "/"), ("Shipping & Returns", "/shipping-returns/")])

    page("/contact/", "Contact | WearWisdomWell", "Questions about a shirt, sizing or an order? Contact WearWisdomWell; we usually reply within a day.", f"""
<h1>Contact</h1>
<p class="lede">Questions before you order? We usually reply within a day.</p>
<ul class="specs">
<li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>About an order:</strong> message us through <a href="{SHOP}">our Etsy shop</a>, so your order details come with it.</li>
</ul>
<p>We're glad to help with sizing, colors, gift timing, or anything that arrived not quite right.</p>""",
         crumbs=[("Home", "/"), ("Contact", "/contact/")])

    page("/404.html", "Page not found | WearWisdomWell", "That page isn't here.", f"""
<h1>That page isn't here.</h1>
<p class="lede">It may have moved. The shirts are all in one place:</p>
<p><a class="btn" href="/shop/">Browse the shop</a></p>
{grid(PRODUCTS[:4])}""")

# ---------------------------------------------------------------- assets
def font(size, bold=False):
    for f in ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]:
        try:
            return ImageFont.truetype(f, size)
        except Exception:
            pass
    return ImageFont.load_default()

NAVY, GOLD, CREAM = (28, 42, 57), (194, 168, 90), (239, 232, 216)

def build_assets():
    (DIST / "img").mkdir(parents=True, exist_ok=True)
    for f in (SRC / "img").glob("*.jpg"):
        shutil.copy(f, DIST / "img" / f.name)
    shutil.copy(SRC / "style.css", DIST / "style.css")
    # favicon
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#1C2A39"/>'
           '<text x="32" y="45" text-anchor="middle" font-family="Georgia,serif" font-size="38" font-weight="700" fill="#C2A85A">W</text></svg>')
    (DIST / "favicon.svg").write_text(svg)
    for size, name in [(32, "favicon-32.png"), (180, "apple-touch-icon.png")]:
        im = Image.new("RGB", (size, size), NAVY)
        d = ImageDraw.Draw(im)
        fnt = font(int(size * .62), True)
        d.text((size / 2, size / 2), "W", fill=GOLD, font=fnt, anchor="mm")
        im.save(DIST / name)
    # default share image
    im = Image.new("RGB", (1200, 630), NAVY)
    d = ImageDraw.Draw(im)
    d.rectangle([40, 40, 1160, 590], outline=GOLD, width=2)
    d.text((600, 250), "WearWisdomWell", fill=CREAM, font=font(76, True), anchor="mm")
    d.text((600, 345), "Subtle statements for people who don't need to argue.", fill=GOLD, font=font(32), anchor="mm")
    d.text((600, 470), "Wit for those wise enough to wear it.", fill=CREAM, font=font(26), anchor="mm")
    im.save(DIST / "img" / "og-default.jpg", quality=90)

def build_meta(paths):
    urls = "".join(f"<url><loc>{SITE}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths if not p.endswith(".html"))
    (DIST / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    lines = [f"{a}  {b}  301" for a, b in REDIRECTS] + [f"{a.rstrip('/')}  {b}  301" for a, b in REDIRECTS]
    (DIST / "_redirects").write_text("\n".join(lines) + "\n")
    (DIST / "_headers").write_text("/img/*\n  Cache-Control: public, max-age=2592000\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n")

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    build_assets()
    build_home(); build_shop(); build_collections(); build_products(); build_blog(); build_info()
    paths = (["/", "/shop/"] + [f"/shop/{c['slug']}/" for c in COLLECTIONS] + [f"/shop/{p['slug']}/" for p in PRODUCTS]
             + ["/blog/"] + [f"/blog/{x['slug']}/" for x in POSTS] + ["/about/", "/shipping-returns/", "/contact/"])
    build_meta(paths)
    print(f"built {len(paths)} pages into {DIST}")

if __name__ == "__main__":
    main()
