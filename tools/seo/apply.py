import re, json, html, os, sys, glob
sys.path.insert(0, os.path.dirname(__file__))
from content_ing import ING
from content_hub import CAT, HUBS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BASE = "https://kalptarunaturals.in/"
TODAY = "2026-11-20"
E = lambda s: html.escape(s, quote=True)
os.chdir(ROOT)
touched = set()
posts = {p["slug"]: p for p in json.load(open("blog/posts.json"))}

def full_title(t):
    for suf in (" | Kalptaru Naturals", " | Kalptaru"):
        if len(t + suf) <= 65: return t + suf
    return t + " | Kalptaru"

def ld(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + '</script>'

def faq_ld(faq):
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub("<[^>]+>", "", a))}} for q, a in faq]})

def faq_html(faq, h="h2"):
    return f'<{h}>Frequently asked questions</{h}><div class="faq">' + "".join(
        f"<details><summary>{E(q)}</summary><p>{a}</p></details>" for q, a in faq) + "</div>"

def set_meta(h, t=None, d=None):
    if t:
        ft = E(full_title(t))
        h = re.sub(r"<title>.*?</title>", f"<title>{ft}</title>", h, count=1, flags=re.S)
        h = re.sub(r'(<meta property="og:title" content=")[^"]*(")', lambda m: m.group(1) + ft + m.group(2), h)
        h = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")', lambda m: m.group(1) + ft + m.group(2), h)
    if d:
        ed = E(d)
        for pat in (r'(<meta name="description" content=")[^"]*(")', r'(<meta property="og:description" content=")[^"]*(")', r'(<meta name="twitter:description" content=")[^"]*(")'):
            h = re.sub(pat, lambda m: m.group(1) + ed + m.group(2), h)
    return h

def add_head(h, s, marker):
    if marker in h: return h
    return h.replace("</head>", s + "</head>", 1)

def bloglinks(slugs, prefix="../"):
    out = []
    for s in slugs:
        p = posts.get(s)
        if p: out.append(f'<li><a href="{prefix}blog/{s}.html">{E(p["title"])}</a><small>{p["date"]} · {p.get("read_min",5)} min read</small></li>')
    return "".join(out)

problems = []
def check(t, d, name):
    if t and len(full_title(t)) > 70: problems.append(f"{name}: title {len(full_title(t))}")
    if d and not (115 <= len(d) <= 160): problems.append(f"{name}: desc {len(d)}")

# ------------------------------------------------ ingredient pages
for iid, c in ING.items():
    f = f"ingredient/{iid}.html"; h = open(f, encoding="utf-8").read()
    if "seo-about" in h: continue
    check(c["t"], c["d"], f)
    h = set_meta(h, c["t"], c["d"])
    # product schema description
    h = re.sub(r'("@type": "Product", "name": "[^"]*", "description": ")[^"]*(")', lambda m: m.group(1) + c["d"].replace('"', '\\"') + m.group(2), h, count=1)
    if c.get("faq"): h = add_head(h, faq_ld(c["faq"]), '"FAQPage"')
    name = re.search(r'<h1 class="iname">(.*?)(?:<span|</h1>)', h).group(1).strip()
    uses = "".join(f"<li>{u}</li>" for u in c.get("uses", []))
    about = (f'<div class="panel seo-about"><h2>About {name}</h2>{c["ov"]}'
             + (f'<h3>Typical uses</h3><ul class="ticks">{uses}</ul>' if uses else "") + "</div>\n  ")
    h, n = re.subn(r'(<div class="wrap rgrid">\s*<div>\s*)', lambda m: m.group(1) + about, h, count=1)
    assert n, f
    if c.get("faq"):
        faqp = f'<div class="panel">{faq_html(c["faq"])}</div>\n  '
        # end of first column = just before the right column (blogrel panel)
        h, n = re.subn(r'(\s*</div>\s*<div>\s*<div class="panel blogrel")', lambda m: "\n  " + faqp + m.group(1).lstrip(), h, count=1)
        assert n, f + " faq"
    bl = bloglinks(c.get("blog", []))
    if bl:
        h = re.sub(r'<div class="panel blogrel" data-ing="([^"]+)" hidden>(.*?)<ul class="bloglist"></ul>',
                   lambda m: f'<div class="panel blogrel" data-ing="{m.group(1)}">{m.group(2)}<ul class="bloglist">{bl}</ul>', h, count=1, flags=re.S)
    open(f, "w", encoding="utf-8").write(h); touched.add(f)

# ------------------------------------------------ category / concern pages
def guide_section(c, prefix):
    links = "".join(f'<li><a href="{prefix}{href}">{E(lbl)}</a></li>' for href, lbl in c.get("links", []))
    return (f'\n<section class="alt seo-guide"><div class="wrap"><div class="prose" style="max-width:920px">{c["guide"]}'
            + (faq_html(c["faq"]) if c.get("faq") else "")
            + (f'<h2>Related guides</h2><ul>{links}</ul>' if links else "")
            + "</div></div></section>\n")

for f, c in CAT.items():
    h = open(f, encoding="utf-8").read()
    if "seo-guide" in h: continue
    check(c.get("t"), c.get("d"), f)
    h = set_meta(h, c.get("t"), c.get("d"))
    if c.get("lead"):
        h, n = re.subn(r'<p class="lead">.*?</p>', f'<p class="lead">{c["lead"]}</p>', h, count=1, flags=re.S)
        if not n: problems.append(f + ": no lead")
    if c.get("faq"): h = add_head(h, faq_ld(c["faq"]), '"FAQPage"')
    prefix = "" if "/" not in f else "../"
    h = h.replace("</main>", guide_section(c, prefix) + "</main>", 1)
    open(f, "w", encoding="utf-8").write(h); touched.add(f)

# ------------------------------------------------ hub pages
shell = open("concern/anti-ageing.html", encoding="utf-8").read()
head_end = shell.index("</head>"); main_s = shell.index('<main id="main">'); main_e = shell.index("</main>") + len("</main>")
head_tpl = shell[:head_end]; body_pre = shell[head_end:main_s]; body_post = shell[main_e:]
# a map of card html by ingredient id
cards = {}
for g in glob.glob("category/*.html") + glob.glob("concern/*.html"):
    for m in re.finditer(r'<article class="card" data-id="([^"]+)">.*?</article>', open(g, encoding="utf-8").read(), re.S):
        cards.setdefault(m.group(1), m.group(0))

for f, c in HUBS.items():
    check(c["t"], c["d"], f)
    url = BASE + f
    hd = head_tpl
    hd = re.sub(r'https://kalptarunaturals\.in/concern/anti-ageing\.html', url, hd)
    hd = re.sub(r'<script type="application/ld\+json">.*?</script>', "", hd, flags=re.S)
    hd = set_meta(hd + "</head>", c["t"], c["d"])[:-len("</head>")]
    hd += ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": "Ingredients", "item": BASE + "ingredients.html"},
        {"@type": "ListItem", "position": 3, "name": c["h1"], "item": url}]})
    hd += ld({"@context": "https://schema.org", "@type": "CollectionPage", "name": c["h1"], "description": c["d"], "url": url,
              "isPartOf": {"@type": "WebSite", "name": "Kalptaru Naturals", "url": BASE},
              "mainEntity": {"@type": "ItemList", "numberOfItems": len(c["ids"]), "itemListElement": [
                  {"@type": "ListItem", "position": i + 1, "url": f"{BASE}ingredient/{x}.html"} for i, x in enumerate(c["ids"])]}})
    hd += faq_ld(c["faq"])
    grid = "".join(cards[x] for x in c["ids"] if x in cards)
    missing = [x for x in c["ids"] if x not in cards]
    if missing: problems.append(f"{f}: no card for {missing}")
    links = "".join(f'<li><a href="../{href}">{E(lbl)}</a></li>' for href, lbl in c["links"])
    main = f'''<main id="main">
<section class="phead"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> › <a href="../ingredients.html">Ingredients</a> › <span>{E(c["h1"])}</span></nav>
 <p class="eyebrow">{E(c["eyebrow"])} · {len(c["ids"])} ingredients</p><h1 class="cat-title">{E(c["h1"])}</h1>
 <p class="lead">{c["lead"]}</p>
 <div class="actions"><a class="btn" href="../contact.html">Request samples &amp; TDS</a><a class="btn ghost" href="../ingredients.html">Full catalogue</a></div>
</div></section>
<section><div class="wrap"><div class="grid">{grid}</div></div></section>
<section class="alt seo-guide"><div class="wrap"><div class="prose" style="max-width:920px">{c["body"]}{faq_html(c["faq"])}<h2>Related guides</h2><ul>{links}</ul></div></div></section>
</main>'''
    body_pre2 = body_pre.replace('class=on aria-current=page', '')
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(hd + body_pre2 + main + body_post); touched.add(f)

# ------------------------------------------------ footer links site-wide
HUBLINKS = '<li><a href="{p}topic/retinol-and-retinaldehyde.html">Retinol &amp; retinaldehyde</a></li><li><a href="{p}topic/vitamin-c-ingredients.html">Vitamin C ingredients</a></li><li><a href="{p}category/rheology.html">Clay thickeners</a></li>'
nfoot = 0
for g in glob.glob("*.html") + glob.glob("*/*.html"):
    if g.startswith("_godaddy"): continue
    h = open(g, encoding="utf-8").read()
    if "topic/vitamin-c-ingredients.html\">Vitamin C ingredients</a></li><li>" in h: continue
    h2, n = re.subn(r'(<li><a href="((?:\.\./)?)category/clays\.html">Clays</a></li>)(</ul>)',
                    lambda m: m.group(1) + HUBLINKS.format(p=m.group(2)) + m.group(3), h, count=1)
    if n:
        open(g, "w", encoding="utf-8").write(h2); nfoot += 1
        if g not in touched and not g.startswith("blog/_"): pass

# ------------------------------------------------ blog cross-links + posts.json
REL = {
 "encapsulated-retinaldehyde-microsponge-520ra": [("../topic/retinol-and-retinaldehyde.html","Compare all retinol and retinaldehyde grades"),("magnabrite-polargel-clay-rheology-modifiers.html","Choosing a clay thickener (Magnabrite® and Polargel®)"),("vitamin-c-serum-l-ascorbic-acid-stable.html","Stable vitamin C serums")],
 "vitamin-c-serum-l-ascorbic-acid-stable": [("../topic/vitamin-c-ingredients.html","Compare all vitamin C ingredients"),("encapsulated-retinaldehyde-microsponge-520ra.html","Encapsulated retinaldehyde (Microsponge® 520RA)"),("../encapsulation.html","Custom encapsulation")],
 "magnabrite-polargel-clay-rheology-modifiers": [("../category/rheology.html","All clay thickeners and stabilisers"),("../category/clays.html","All Amazonian clays"),("encapsulated-retinaldehyde-microsponge-520ra.html","Encapsulated retinaldehyde guide")],
}
for slug, rel in REL.items():
    f = f"blog/{slug}.html"; h = open(f, encoding="utf-8").read()
    if "seo-related" in h: continue
    block = '<div class="seo-related"><h2>Related guides</h2><ul>' + "".join(f'<li><a href="{u}">{E(l)}</a></li>' for u, l in rel) + "</ul></div>"
    h, n = re.subn(r"(<h2>Frequently asked questions</h2>)", block + r"\1", h, count=1)
    assert n, f
    open(f, "w", encoding="utf-8").write(h); touched.add(f)
pj = json.load(open("blog/posts.json"))
for p in pj:
    if p["slug"] == "encapsulated-retinaldehyde-microsponge-520ra" and "microsponge-n-720tra" not in p["ingredients"]:
        p["ingredients"].append("microsponge-n-720tra")
json.dump(pj, open("blog/posts.json", "w"), ensure_ascii=False, indent=1)

# ------------------------------------------------ sitemap
sm = open("sitemap.xml").read()
for f in sorted(touched):
    if f.startswith("blog/"): continue
    loc = BASE + f
    if loc in sm:
        sm = re.sub(rf"(<loc>{re.escape(loc)}</loc><lastmod>)[^<]+", rf"\g<1>{TODAY}", sm)
    else:
        sm = sm.replace("</urlset>", f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>0.9</priority></url>\n</urlset>")
open("sitemap.xml", "w").write(sm)
bs = open("blog-sitemap.xml").read()
for slug in REL:
    bs = re.sub(rf"(<loc>{re.escape(BASE)}blog/{slug}\.html</loc><lastmod>)[^<]+", rf"\g<1>{TODAY}", bs)
open("blog-sitemap.xml", "w").write(bs)
rb = open("robots.txt").read()
if "_godaddy_backup" not in rb:
    rb = rb.replace("Disallow: /blog/_shell.html", "Disallow: /blog/_shell.html\nDisallow: /_godaddy_backup/")
    open("robots.txt", "w").write(rb)

print("touched", len(touched), "footers", nfoot)
print("PROBLEMS:", *problems, sep="\n ")
