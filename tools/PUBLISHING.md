# Publishing to kalptarunaturals.in (GitHub Pages)

The site is served by GitHub Pages from the `main` branch of this repository.
Every push to `main` goes live within about 1–2 minutes. Nothing is uploaded to GoDaddy any more.

## Publishing an approved blog post
1. Clone this repo (via the session's GitHub access) and put the post spec JSON at `tools/specs/<date>-<slug>.json`.
2. Build in place:
   `python3 tools/blog_tool.py build blog/_shell.html blog/posts.json tools/specs/<date>-<slug>.json .`
   This writes `blog/<slug>.html`, `blog/index.html`, `blog/posts.json` and `blog-sitemap.xml`.
3. Commit and push to `main`. Wait ~2 minutes, then check https://kalptarunaturals.in/blog/<slug>.html loads.

## Other
- Dispatch Form: Google Apps Script web app; `dispatch/index.html` redirects to it (set `DISPATCH_URL`).
- Custom domain is set by the `CNAME` file. `.nojekyll` must stay.
