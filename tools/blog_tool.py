#!/usr/bin/env python3
"""Kalptaru Naturals blog generator.

Usage:
  python3 blog_tool.py build  SHELL.html POSTS.json SPEC.json OUTDIR
      -> writes OUTDIR/blog/<slug>.html, OUTDIR/blog/index.html,
         OUTDIR/blog/posts.json (updated), OUTDIR/blog-sitemap.xml
  python3 blog_tool.py index  SHELL.html POSTS.json OUTDIR    (rebuild index + sitemap only)

SHELL.html  = /blog/_shell.html from the live site (made by build.py; tokens
              __SLUG__ __TITLE__ __DESC__ __BODY__ __HEAD__ __OGIMAGE__)
POSTS.json  = /blog/posts.json from the live site ([] if none yet)
SPEC.json   = the new post, see SPEC_FIELDS below.

Charts: put figures in spec["figures"] as chart specs; reference them in
body_html with {{fig:NAME}}. Chart types: "xy" (line/scatter), "bar", "flow".
"""
import json, sys, os, html, datetime, math

BASE = "https://kalptarunaturals.in/"
WA = "919667551115"
GREEN, TEAL, GOLD, INK, MUTED, LINE = "#3d4b41", "#6c9696", "#c39a4a", "#2b332d", "#6b746d", "#dde3df"
PAL = [GREEN, GOLD, TEAL, "#a8574a", "#7c6aa6", "#8aa05a"]
e = lambda s: html.escape(str(s), quote=True)

SPEC_FIELDS = """slug, seo_title (<=60 chars), title (H1), desc (meta, 140-158 chars), lede,
date (YYYY-MM-DD), ingredients [ingredient ids from site], principal (id), principal_name,
category_label, keywords [..], read_min, keyfacts [[value,label],..], body_html (uses <h2>/<h3>/<p>/<ul>/<table>, {{fig:NAME}}),
figures {NAME: chart spec + "caption"}, faq [[q,a],..], sources [[title,url],..], ingredient_name, ingredient_inci"""

# ---------------------------------------------------------------- charts
def _nice(lo, hi, n=5):
    span = hi - lo or 1
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n: step *= m; break
    a = math.floor(lo / step) * step; b = math.ceil(hi / step) * step
    t = []; v = a
    while v <= b + step / 1e6: t.append(round(v, 10)); v += step
    return t

def _fmt(v):
    return ("%g" % v) if abs(v) < 1e5 else "{:,.0f}".format(v)

def chart_xy(c, W=720, H=420):
    """c: title, xlabel, ylabel, series[{name, points[[x,y]], color?, line(bool, default true), dash?}],
    xticks?, yticks?, band? {lo,hi,label}, note?"""
    L, R, T, B = 70, 24, 46, 62
    xs = [p[0] for s in c["series"] for p in s["points"]]; ys = [p[1] for s in c["series"] for p in s["points"]]
    if c.get("band"): ys += [c["band"]["lo"], c["band"]["hi"]]
    xt = c.get("xticks") or _nice(min(xs), max(xs)); yt = c.get("yticks") or _nice(min(0, min(ys)) if c.get("y0", True) else min(ys), max(ys))
    x0, x1, y0, y1 = xt[0], xt[-1], yt[0], yt[-1]
    X = lambda v: L + (v - x0) / (x1 - x0) * (W - L - R); Y = lambda v: H - B - (v - y0) / (y1 - y0) * (H - T - B)
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{e(c["title"])}" font-family="Roboto,Arial,sans-serif">',
         f'<title>{e(c["title"])}</title>',
         f'<text x="{L}" y="24" font-size="16" font-weight="500" fill="{GREEN}">{e(c["title"])}</text>']
    if c.get("band"):
        b = c["band"]; o.append(f'<rect x="{L}" y="{Y(b["hi"]):.1f}" width="{W-L-R}" height="{Y(b["lo"])-Y(b["hi"]):.1f}" fill="{GREEN}" opacity=".07"/>'
                                f'<text x="{W-R-6}" y="{Y(b["hi"])+15:.1f}" font-size="11" text-anchor="end" fill="{GREEN}">{e(b.get("label",""))}</text>')
    for v in yt:
        o.append(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{LINE}"/><text x="{L-8}" y="{Y(v)+4:.1f}" font-size="12" text-anchor="end" fill="{MUTED}">{_fmt(v)}</text>')
    for v in xt:
        o.append(f'<line x1="{X(v):.1f}" x2="{X(v):.1f}" y1="{H-B}" y2="{H-B+5}" stroke="{MUTED}"/><text x="{X(v):.1f}" y="{H-B+20}" font-size="12" text-anchor="middle" fill="{MUTED}">{_fmt(v)}</text>')
    o.append(f'<line x1="{L}" x2="{W-R}" y1="{H-B}" y2="{H-B}" stroke="{MUTED}"/>')
    o.append(f'<text x="{(L+W-R)/2:.0f}" y="{H-16}" font-size="13" text-anchor="middle" fill="{INK}">{e(c.get("xlabel",""))}</text>')
    o.append(f'<text transform="translate(18 {(T+H-B)/2:.0f}) rotate(-90)" font-size="13" text-anchor="middle" fill="{INK}">{e(c.get("ylabel",""))}</text>')
    lx = L + 8
    for i, s in enumerate(c["series"]):
        col = s.get("color") or PAL[i % len(PAL)]; pts = sorted(s["points"])
        if s.get("line", True) and len(pts) > 1:
            d = " ".join(f'{"M" if k==0 else "L"}{X(x):.1f},{Y(y):.1f}' for k, (x, y) in enumerate(pts))
            o.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2.5"{" stroke-dasharray=\"6 5\"" if s.get("dash") else ""}/>')
        if s.get("markers", True):
            o += [f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="4.5" fill="{col}" stroke="#fff" stroke-width="1.5"><title>{e(s["name"])}: {_fmt(x)}, {_fmt(y)}</title></circle>' for x, y in pts]
        o.append(f'<rect x="{lx}" y="{T-8}" width="12" height="12" rx="3" fill="{col}"/><text x="{lx+17}" y="{T+2}" font-size="12" fill="{INK}">{e(s["name"])}</text>')
        lx += 30 + 7 * len(s["name"])
    o.append('</svg>'); return "".join(o)

def chart_bar(c, W=720, H=400):
    """c: title, ylabel, bars [[label, value, color?]], unit?, ymax?"""
    L, R, T, B = 64, 20, 46, 70
    vals = [b[1] for b in c["bars"]]; yt = _nice(0, c.get("ymax", max(vals)))
    y1 = yt[-1]; Y = lambda v: H - B - v / y1 * (H - T - B)
    n = len(c["bars"]); slot = (W - L - R) / n; bw = min(90, slot * .6)
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{e(c["title"])}" font-family="Roboto,Arial,sans-serif"><title>{e(c["title"])}</title>',
         f'<text x="{L}" y="24" font-size="16" font-weight="500" fill="{GREEN}">{e(c["title"])}</text>']
    for v in yt:
        o.append(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{LINE}"/><text x="{L-8}" y="{Y(v)+4:.1f}" font-size="12" text-anchor="end" fill="{MUTED}">{_fmt(v)}</text>')
    for i, b in enumerate(c["bars"]):
        col = b[2] if len(b) > 2 else PAL[i % len(PAL)]; x = L + slot * i + (slot - bw) / 2
        o.append(f'<rect x="{x:.1f}" y="{Y(b[1]):.1f}" width="{bw:.1f}" height="{H-B-Y(b[1]):.1f}" rx="4" fill="{col}"/>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{Y(b[1])-6:.1f}" font-size="13" font-weight="500" text-anchor="middle" fill="{INK}">{_fmt(b[1])}{e(c.get("unit",""))}</text>')
        words = str(b[0]).split(); lines = [" ".join(words[:max(1,len(words)//2)]), " ".join(words[max(1,len(words)//2):])] if len(str(b[0])) > 16 else [b[0]]
        for k, ln in enumerate(lines):
            o.append(f'<text x="{x+bw/2:.1f}" y="{H-B+18+k*15}" font-size="12" text-anchor="middle" fill="{INK}">{e(ln)}</text>')
    o.append(f'<line x1="{L}" x2="{W-R}" y1="{H-B}" y2="{H-B}" stroke="{MUTED}"/>')
    o.append(f'<text transform="translate(18 {(T+H-B)/2:.0f}) rotate(-90)" font-size="13" text-anchor="middle" fill="{INK}">{e(c.get("ylabel",""))}</text></svg>')
    return "".join(o)

def chart_flow(c, W=720, H=170):
    """c: title, steps [[label, sublabel]], arrows [labels between steps]"""
    n = len(c["steps"]); bw = (W - 40 - (n - 1) * 60) / n
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{e(c["title"])}" font-family="Roboto,Arial,sans-serif"><title>{e(c["title"])}</title>',
         f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="{GOLD}"/></marker></defs>',
         f'<text x="20" y="24" font-size="16" font-weight="500" fill="{GREEN}">{e(c["title"])}</text>']
    for i, s in enumerate(c["steps"]):
        x = 20 + i * (bw + 60); hi = s[2] if len(s) > 2 else (i == n - 1)
        o.append(f'<rect x="{x:.1f}" y="50" width="{bw:.1f}" height="84" rx="12" fill="{GREEN if hi else "#f3f6f4"}" stroke="{GREEN}"/>')
        o.append(f'<text x="{x+bw/2:.1f}" y="88" font-size="15" font-weight="500" text-anchor="middle" fill="{"#fff" if hi else GREEN}">{e(s[0])}</text>')
        o.append(f'<text x="{x+bw/2:.1f}" y="110" font-size="12" text-anchor="middle" fill="{"#dfe7e1" if hi else MUTED}">{e(s[1])}</text>')
        if i < n - 1:
            ax = x + bw + 6
            o.append(f'<line x1="{ax:.1f}" y1="92" x2="{ax+46:.1f}" y2="92" stroke="{GOLD}" stroke-width="2.5" marker-end="url(#ah)"/>')
            if c.get("arrows"): o.append(f'<text x="{ax+24:.1f}" y="80" font-size="11" text-anchor="middle" fill="{MUTED}">{e(c["arrows"][i])}</text>')
    o.append('</svg>'); return "".join(o)

def render_fig(name, f):
    t = f.get("type", "xy")
    svg = {"xy": chart_xy, "bar": chart_bar, "flow": chart_flow}[t](f)
    return f'<figure class="fig" id="fig-{e(name)}">{svg}<figcaption>{f.get("caption","")}</figcaption></figure>'

# ---------------------------------------------------------------- pages
def fill(shell, slug, title, desc, body, head, og):
    return (shell.replace("__SLUG__", slug).replace("__TITLE__", e(title)).replace("__DESC__", e(desc))
            .replace("__OGIMAGE__", og).replace("__HEAD__", head).replace("__BODY__", body))

def ld(o): return '<script type="application/ld+json">' + json.dumps(o, ensure_ascii=False) + '</script>'

def post_html(shell, p, posts):
    body = p["body_html"]
    for k, f in p.get("figures", {}).items(): body = body.replace("{{fig:%s}}" % k, render_fig(k, f))
    url = f"{BASE}blog/{p['slug']}.html"; og = f"{BASE}assets/img/principals/{p.get('og_logo', p['principal'] + '.png')}"
    ing = p["ingredients"][0]
    kf = "".join(f"<div><b>{e(v)}</b><span>{e(l)}</span></div>" for v, l in p.get("keyfacts", []))
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in p.get("faq", []))
    src = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' for t, u in p.get("sources", []))
    wa = "https://wa.me/%s?text=%s" % (WA, __import__("urllib.parse").parse.quote(f"Hello Kalptaru Naturals, I read your article on {p['ingredient_name']}. Please share TDS, sample and price."))
    rel = [x for x in posts if x["slug"] != p["slug"]][:3]
    relh = "".join(f'<li><a href="{e(x["slug"])}.html">{e(x["title"])}</a><small>{e(x["date"])}</small></li>' for x in rel)
    b = f'''
<section class="bhero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> › <a href="index.html">Blog</a> › <span>{e(p["ingredient_name"])}</span></nav>
 <p class="eyebrow">{e(p.get("category_label","Formulator guide"))} · {e(p["principal_name"])}</p>
 <h1>{e(p["title"])}</h1>
 <p class="lede">{e(p["lede"])}</p>
 <div class="bmeta"><span>By Kalptaru Naturals technical team</span><span>Published <time datetime="{p["date"]}">{datetime.date.fromisoformat(p["date"]).strftime("%d %b %Y")}</time></span><span>{p.get("read_min",6)} min read</span></div>
</div></section>
<div class="wrap post">
 <article class="prose">
  {f'<div class="keyfacts">{kf}</div>' if kf else ''}
  {body}
  {f'<h2>Frequently asked questions</h2><div class="faq">{faq}</div>' if faq else ''}
  <div class="cta-box"><h2>Formulating with {e(p["ingredient_name"])}?</h2>
   <p>Kalptaru Naturals supplies {e(p["ingredient_name"])} from {e(p["principal_name"])} across India, with TDS, MSDS, CoA, samples and formulation support.</p>
   <a class="btn" href="{wa}" target="_blank" rel="noopener">Request TDS &amp; sample on WhatsApp</a></div>
  {f'<h2>Sources</h2><ol class="small">{src}</ol>' if src else ''}
  <p class="note small">Technical data summarised from the manufacturer's TDS and published literature for formulators. It is not medical advice. Claims for finished products must be substantiated by the brand owner.</p>
 </article>
 <aside class="aside"><div class="panel">
  <p class="eyebrow">Ingredient at a glance</p><h2>{e(p["ingredient_name"])}</h2>
  <p class="small muted">INCI: {e(p.get("ingredient_inci",""))}</p>
  <p><a href="../principal/{e(p["principal"])}.html">{e(p["principal_name"])}</a></p>
  <div class="actions"><a class="btn sm" href="../ingredient/{e(ing)}.html">View ingredient</a> <button class="btn ghost sm" type="button" data-add="{e(ing)}">+ Enquire</button></div>
  {f'<h3 class="small" style="margin-top:20px">More from the blog</h3><ul class="bloglist">{relh}</ul>' if relh else ''}
 </div></aside>
</div>'''
    head = (ld({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"][:110], "description": p["desc"],
                "datePublished": p["date"], "dateModified": p.get("updated", p["date"]), "inLanguage": "en-IN",
                "mainEntityOfPage": url, "url": url, "image": og, "keywords": ", ".join(p.get("keywords", [])),
                "author": {"@type": "Organization", "name": "Kalptaru Naturals", "url": BASE},
                "publisher": {"@type": "Organization", "name": "Kalptaru Naturals", "logo": {"@type": "ImageObject", "url": BASE + "assets/img/logo-dark.png"}},
                "about": {"@type": "Product", "name": p["ingredient_name"], "url": f"{BASE}ingredient/{ing}.html", "brand": {"@type": "Brand", "name": p["principal_name"]}}})
            + ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": BASE + "blog/index.html"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]})
            + (ld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}} for q, a in p["faq"]]}) if p.get("faq") else "")
            + f'<meta property="article:published_time" content="{p["date"]}"><meta name="keywords" content="{e(", ".join(p.get("keywords", [])))}">')
    return fill(shell, p["slug"], p.get("seo_title", p["title"]), p["desc"], b, head, og)

def index_html(shell, posts):
    cards = "".join(f'''<article class="bcard"><p class="eyebrow">{e(x.get("principal_name",""))}</p>
 <h2><a href="{e(x["slug"])}.html">{e(x["title"])}</a></h2><p>{e(x.get("excerpt",""))}</p>
 <div class="bmeta"><span>{datetime.date.fromisoformat(x["date"]).strftime("%d %b %Y")}</span><span>{x.get("read_min",6)} min read</span></div></article>''' for x in posts)
    body = f'''<section class="bhero"><div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> › <span>Blog</span></nav>
 <p class="eyebrow">Formulator guides</p><h1>Kalptaru Naturals Blog: cosmetic ingredient guides</h1>
 <p class="lede">Data-backed articles on the actives, delivery systems, oils and butters we supply in India: how they work, what the technical data shows, and how to formulate with them.</p>
</div></section><div class="wrap"><div class="bcards">{cards or '<p class="muted">New articles are on the way.</p>'}</div></div>'''
    head = ld({"@context": "https://schema.org", "@type": "Blog", "name": "Kalptaru Naturals Blog", "url": BASE + "blog/index.html",
               "publisher": {"@type": "Organization", "name": "Kalptaru Naturals"},
               "blogPost": [{"@type": "BlogPosting", "headline": x["title"], "url": f"{BASE}blog/{x['slug']}.html", "datePublished": x["date"]} for x in posts[:30]]})
    return fill(shell, "index", "Blog: Cosmetic Ingredient Guides for Formulators | Kalptaru Naturals",
                "Formulator guides from Kalptaru Naturals: how cosmetic actives, peptides, delivery systems, oils and butters work, with TDS data, graphs and formulation tips.",
                body, head, BASE + "assets/img/logo-dark.png")

def sitemap(posts):
    today = datetime.date.today().isoformat()
    u = [f"<url><loc>{BASE}blog/index.html</loc><lastmod>{posts[0]['date'] if posts else today}</lastmod><priority>0.8</priority></url>"]
    u += [f"<url><loc>{BASE}blog/{x['slug']}.html</loc><lastmod>{x.get('updated', x['date'])}</lastmod><priority>0.7</priority></url>" for x in posts]
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(u) + "\n</urlset>\n"

def write(out, rel, s):
    p = os.path.join(out, rel); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w", encoding="utf-8").write(s)

if __name__ == "__main__":
    cmd = sys.argv[1]; shell = open(sys.argv[2], encoding="utf-8").read()
    posts = json.load(open(sys.argv[3])) if os.path.exists(sys.argv[3]) else []
    if cmd == "build":
        p = json.load(open(sys.argv[4], encoding="utf-8")); out = sys.argv[5]
        for k in ("slug", "title", "desc", "date", "ingredients", "principal", "principal_name", "ingredient_name", "body_html"):
            assert p.get(k), "missing " + k
        assert len(p.get("seo_title", p["title"])) <= 65, "seo_title too long"
        assert 110 <= len(p["desc"]) <= 165, "desc should be 110-165 chars (is %d)" % len(p["desc"])
        posts = [x for x in posts if x["slug"] != p["slug"]]
        posts.insert(0, {k: p.get(k) for k in ("slug", "title", "date", "ingredients", "principal", "principal_name", "read_min")} | {"excerpt": p.get("excerpt", p["desc"])})
        posts.sort(key=lambda x: x["date"], reverse=True)
        write(out, f"blog/{p['slug']}.html", post_html(shell, p, posts))
    else:
        out = sys.argv[4]
    write(out, "blog/index.html", index_html(shell, posts))
    write(out, "blog/posts.json", json.dumps(posts, ensure_ascii=False, indent=1))
    write(out, "blog-sitemap.xml", sitemap(posts))
    print("ok", len(posts), "posts")
