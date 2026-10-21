#!/usr/bin/env python3
"""Build the static website in web/ from the Markdown sources.

Run it in a container (see tools/README.md). It needs the `markdown` package.

Input : README.md, LICENSE.md, guide/*.md
Output: web/*.html  (flat folder, relative links only, no JavaScript needed to read)
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / "web"
COPY = "© 2026 UncleJS — Licensed under CC BY-NC-SA 4.0"
BACK = "[↑ Back to TOC](#toc)"
SITE = "Online Privacy Guide"

# Source file -> output file
def out_name(src: Path) -> str:
    rel = src.relative_to(ROOT).as_posix()
    if rel == "README.md":
        return "index.html"
    if rel == "LICENSE.md":
        return "license.html"
    return src.stem + ".html"


def gh_slug(value, separator="-"):
    s = re.sub(r"[^\w\- ]", "", value.strip().lower())
    return s.replace(" ", separator)


def is_nav(line: str) -> bool:
    return line.startswith("Previous:") or line.startswith("[Home](")


def is_badge(line: str) -> bool:
    return line.startswith("[![") or line.startswith("![")


FLOW = (
    '<ol class="flow">'
    '<li><a href="disclaimer.html">Disclaimer</a></li>'
    '<li><a href="00-how-to-read.html">How to read</a></li>'
    '<li><a href="01-privacy-security-anonymity.html">Concepts</a></li>'
    '<li><a href="02-threat-models.html">Threat models</a></li>'
    '<li><a href="03-accounts.html">Everyday (03&ndash;16)</a></li>'
    '<li><a href="17-targeted-threats.html">Higher-risk (17&ndash;23)</a></li>'
    '<li><a href="glossary.html">Back matter</a></li>'
    "</ol>"
)


def prepare(src: Path):
    """Return (title, body_markdown, h2_list, az_markdown)."""
    lines = src.read_text(encoding="utf-8").split("\n")
    title = lines[0][2:].strip()
    rest = lines[1:]

    # Split header chrome from the rest at the TOC anchor.
    try:
        k = next(i for i, l in enumerate(rest) if l.strip() == '<a name="toc"></a>')
    except StopIteration:
        k = None

    if k is None:
        head, tail = rest, []
    else:
        head, tail = rest[:k], rest[k + 1:]

    head = [l for l in head if not is_badge(l) and not is_nav(l)]
    while head and head[-1].strip() in ("", "---"):
        head.pop()
    while head and head[0].strip() == "":
        head.pop(0)

    # Drop the Markdown "Table of contents" block (the site builds its own).
    az = ""
    if tail:
        i = 0
        while i < len(tail) and tail[i].strip() == "":
            i += 1
        if i < len(tail) and tail[i].startswith("## Table of contents"):
            j = i + 1
            toc_block = []
            while j < len(tail) and not tail[j].startswith("## "):
                toc_block.append(tail[j])
                j += 1
            if src.name == "glossary.md":
                az = "\n".join(toc_block).strip().replace(" · ", " ")
            tail = tail[j:]

    # Remove footer: trailing blanks, copyright, hr, nav lines.
    while tail and (tail[-1].strip() == "" or tail[-1].strip() == "---"
                    or tail[-1].startswith("©") or is_nav(tail[-1])):
        tail.pop()

    glossary = src.name == "glossary.md"
    cleaned = []
    for l in tail:
        if l.strip() == BACK:
            if glossary:
                cleaned.append('<a class="back-link" href="#toc">&uarr; A&ndash;Z</a>')
            continue
        cleaned.append(l)

    # The README's "Website" section describes the repository, not the site.
    if src.name == "README.md":
        kept, skip = [], False
        for l in cleaned:
            if l.startswith("## "):
                skip = l.strip() == "## Website"
            if not skip:
                kept.append(l)
        cleaned = kept

    # Replace mermaid diagram with plain HTML.
    text = "\n".join(head + [""] + cleaned)
    text = re.sub(r"```mermaid\n.*?```", "\n" + FLOW + "\n", text, flags=re.S)

    # Collect h2 headings outside fences.
    h2 = []
    fence = False
    for l in text.split("\n"):
        if l.strip().startswith("```"):
            fence = not fence
        if not fence and l.startswith("## "):
            h2.append(l[3:].strip())
    return title, text, h2, az


def render(md_text: str) -> str:
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"slugify": gh_slug}},
    )
    return md.convert(md_text)


def fix_links(h: str) -> str:
    def repl(m):
        url = m.group(1)
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            return m.group(0)
        path, _, frag = url.partition("#")
        name = path.split("/")[-1]
        if name == "README.md":
            new = "index.html"
        elif name == "LICENSE.md":
            new = "license.html"
        elif name.endswith(".md"):
            new = name[:-3] + ".html"
        else:
            return m.group(0)
        return 'href="%s%s"' % (new, ("#" + frag) if frag else "")
    h = re.sub(r'href="([^"]+)"', repl, h)
    # External links: safe defaults.
    h = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener noreferrer"', h)
    return h


def post(h: str) -> str:
    h = fix_links(h)
    h = re.sub(r"<li>\[ \] (.*?)</li>",
               r'<li class="task"><label><input type="checkbox"> <span>\1</span></label></li>',
               h, flags=re.S)
    h = h.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return h


# Navigation structure -------------------------------------------------------
def collect():
    pages = []
    pages.append(ROOT / "README.md")
    pages.append(ROOT / "guide" / "disclaimer.md")
    for p in sorted((ROOT / "guide").glob("[0-9][0-9]-*.md")):
        pages.append(p)
    pages.append(ROOT / "guide" / "glossary.md")
    pages.append(ROOT / "guide" / "further-reading.md")
    pages.append(ROOT / "LICENSE.md")
    return pages


def sidebar(meta, current):
    groups = [
        ("Start", lambda n, num: n in ("index.html", "disclaimer.html") or (num is not None and num <= 2)),
        ("Everyday", lambda n, num: num is not None and 3 <= num <= 16),
        ("Higher-risk", lambda n, num: num is not None and 17 <= num <= 23),
        ("Reference", lambda n, num: n in ("glossary.html", "further-reading.html", "license.html")),
    ]
    out = []
    for label, test in groups:
        items = []
        for name, title, num in meta:
            if test(name, num):
                cur = ' aria-current="page"' if name == current else ""
                text = {"index.html": "Home", "disclaimer.html": "Disclaimer",
                        "license.html": "License"}.get(name, title)
                items.append('<li><a href="%s"%s>%s</a></li>' % (name, cur, html.escape(text)))
        out.append("<h2>%s</h2><ul>%s</ul>" % (label, "".join(items)))
    return "\n".join(out)


TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {site}</title>
<meta name="description" content="A practical guide to protecting your privacy online, from everyday habits to higher-risk situations.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230f1419'/%3E%3Cpath d='M16 5l9 3v7c0 6-4 10-9 12-5-2-9-6-9-12V8z' fill='%235aa9ff'/%3E%3C/svg%3E">
<script>
(function () {{
  try {{
    var t = localStorage.getItem('privacy-guide-theme');
    if (t === 'light' || t === 'dark') {{
      document.documentElement.setAttribute('data-theme', t);
    }}
  }} catch (e) {{}}
}})();
</script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header">
  <button class="icon-btn menu-btn" id="menu-toggle" type="button" aria-expanded="false" aria-controls="sidebar">Menu</button>
  <a class="site-title" href="index.html">{site}</a>
  <button class="icon-btn" id="theme-toggle" type="button">Light mode</button>
</header>
<div class="disclaimer-bar">Read the <a href="disclaimer.html">Disclaimer and Limitation of Liability</a> before using this guide. General information only; not legal or professional security advice.</div>
<div class="layout">
<nav class="sidebar" id="sidebar" aria-label="Guide contents">
{sidebar}
</nav>
<main>
<article>
<h1>{title_html}</h1>
{toc}{body}
<nav class="pager" aria-label="Previous and next page">
{prev}{nxt}
</nav>
</article>
</main>
</div>
<footer class="site-footer">
<p>{copy} &middot; <a href="disclaimer.html">Disclaimer</a> &middot; <a href="license.html">License</a></p>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
"""


def main():
    pages = collect()
    # Pass 1: prepare everything and gather nav metadata.
    prepared = []
    meta = []
    for src in pages:
        title, text, h2, az = prepare(src)
        name = out_name(src)
        m = re.match(r"(\d\d)-", src.name)
        num = int(m.group(1)) if m else None
        prepared.append((src, name, title, text, h2, az))
        meta.append((name, title, num))

    order = [n for n, _, _ in meta]
    titles = {n: t for n, t, _ in meta}
    WEB.mkdir(exist_ok=True)

    for src, name, title, text, h2, az in prepared:
        body = post(render(text))
        if az:
            body = ('<nav class="az" id="toc" aria-label="Glossary letters">%s</nav>\n' % post(render(az))) + body
        seen = {}
        items = []
        for t in h2:
            s = gh_slug(t)
            n = seen.get(s, 0)
            seen[s] = n + 1
            anchor = s if n == 0 else "%s_%d" % (s, n)
            items.append('<li><a href="#%s">%s</a></li>' % (anchor, html.escape(t)))
        toc = ""
        if len(items) > 3 and src.name != "glossary.md" and name != "index.html":
            toc = ('<details class="page-toc" open><summary>On this page</summary><ul>%s</ul></details>\n'
                   % "".join(items))

        i = order.index(name)
        prev = nxt = ""
        if name == "license.html":
            pass
        else:
            if i > 0:
                p = order[i - 1]
                prev = '<a class="prev" href="%s">&larr; %s</a>' % (p, html.escape("Home" if p == "index.html" else titles[p]))
            else:
                prev = '<span class="spacer"></span>'
            if i + 1 < len(order) - 1:  # skip the licence page as a "next"
                n = order[i + 1]
                nxt = '<a class="next" href="%s">%s &rarr;</a>' % (n, html.escape(titles[n]))

        page = TEMPLATE.format(
            title=html.escape(title.rstrip(".")),
            site=SITE,
            sidebar=sidebar(meta, name),
            title_html=html.escape(title),
            toc=toc,
            body=body,
            prev=prev,
            nxt=nxt,
            copy=COPY,
        )
        (WEB / name).write_text(page, encoding="utf-8")
        print("wrote web/%s" % name)


if __name__ == "__main__":
    main()
