#!/usr/bin/env python3
"""Build a self-contained interactive course.html for the Problem Solving micro-credential.

Reads the course Markdown files and emits a single, dependency-free HTML file that works from
file:// — sidebar navigation, phase progress, Mermaid diagrams (brand-themed, with graceful
fallback), syntax-tagged code blocks, embedded videos, and copy-able prompts.

Run:  python3 build-course.py   (from this folder)
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CUR_DIR = ""  # dir of the page being converted, relative to the course root (for image paths)


def resolve_src(src):
    """Rewrite a page-relative path to be relative to course.html (the course root)."""
    if not src or re.match(r"^([a-z]+:)?//", src) or src.startswith("data:") or src.startswith("/"):
        return src
    return os.path.normpath(os.path.join(CUR_DIR, src)).replace(os.sep, "/")

# (file, id, sidebar title, group)
PAGES = [
    ("README.md",                                                "overview",  "Course overview",                 "Start"),
    ("micro-credential.md",                                      "spec",      "Micro-credential spec",           "Start"),
    ("atoms/atom-1-how-problem-solving-works.md",               "atom-1",    "1 · How problem solving works",   "🙉 Phase 1 · hear"),
    ("atoms/atom-2-decisions-and-biases.md",                     "atom-2",    "2 · Decisions & biases",          "🙉 Phase 1 · hear"),
    ("atoms/atom-3-define-and-decompose.md",                     "atom-3",    "3 · Define & decompose 🛠️",       "🙈 Phase 2 · see"),
    ("atoms/atom-4-root-cause-analysis.md",                      "atom-4",    "4 · Find the root cause 🛠️",      "🙊 Phase 3 · do"),
    ("atoms/atom-5-generate-and-choose-solutions.md",            "atom-5",    "5 · Generate & choose 🛠️",        "🙊 Phase 3 · do"),
    ("atoms/atom-6-capstone-solve-a-real-problem.md",           "atom-6",    "6 · Capstone 🚀",                 "🐵 Phase 4 · share"),
    ("capstone.md",                                              "capstone",  "Capstone brief",                  "Assess"),
    ("rubrics.md",                                               "rubrics",   "Rubrics",                         "Assess"),
    ("skills-map.md",                                            "skillsmap", "Skills map → job match",          "Assess"),
]
ATOM_IDS = ["atom-1", "atom-2", "atom-3", "atom-4", "atom-5", "atom-6"]

PATH2ID = {p[0]: p[1] for p in PAGES}          # course file path -> in-app page id
COURSE_REL = "examples/problem-solving-micro-credential"  # course root, relative to repo root
MAIN_INDEX_REL = "../../index.html"            # main interactive site, from course root


def resolve_link(url):
    """Route a Markdown link target. Internal course pages -> in-app #id; other repo .md
    files -> open in the main interactive site; everything else -> left as-is."""
    if url.startswith("#") or re.match(r"^([a-z]+:)?//", url) or url.startswith("mailto:"):
        return url
    base = url.split("#", 1)[0]
    anchor = url[len(base):]
    resolved = resolve_src(base)  # course-root-relative
    if resolved in PATH2ID:
        return "#" + PATH2ID[resolved]
    if base.lower().endswith(".md"):
        repo_rel = os.path.normpath(os.path.join(COURSE_REL, resolved)).replace(os.sep, "/")
        return MAIN_INDEX_REL + "#/" + repo_rel + anchor
    return resolve_src(base) + anchor


# ----------------------------------------------------------------------------- inline markdown
def inline(text):
    spans = []
    lits = []

    def stash(m):
        spans.append(m.group(1))
        return "\x00%d\x00" % (len(spans) - 1)

    def stash_lit(m):
        lits.append(m.group(1))
        return "\x01%d\x01" % (len(lits) - 1)

    text = re.sub(r"\\([\\`*_{}\[\]()#+.!-])", stash_lit, text)  # backslash escapes
    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)",
                  lambda m: '<img alt="%s" src="%s">' % (html.escape(m.group(1)), html.escape(resolve_src(m.group(2)))), text)
    def _link(m):
        href = resolve_link(m.group(2))
        extra = "" if href.startswith("#") else ' target="_blank" rel="noopener"'
        return '<a href="%s"%s>%s</a>' % (html.escape(href, quote=True), extra, m.group(1))

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: "<code>%s</code>" % html.escape(spans[int(m.group(1))]), text)
    text = re.sub(r"\x01(\d+)\x01", lambda m: html.escape(lits[int(m.group(1))]), text)
    return text


def yt_id(url):
    m = re.search(r"(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{6,})", url)
    return m.group(1) if m else ""


# ----------------------------------------------------------------------------- block markdown
def md_to_html(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)

    def flush_list(buf, ordered):
        if not buf:
            return
        tag = "ol" if ordered else "ul"
        out.append("<%s>" % tag)
        for item in buf:
            cb = ""
            mm = re.match(r"\[([ xX])\]\s+(.*)", item)
            if mm:
                checked = " checked" if mm.group(1).lower() == "x" else ""
                cb = '<input type="checkbox" disabled%s> ' % checked
                item = mm.group(2)
            out.append("<li>%s%s</li>" % (cb, inline(item)))
        out.append("</%s>" % tag)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code
        if stripped.startswith("```"):
            lang = stripped[3:].strip().lower()
            i += 1
            body = []
            while i < n and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1  # closing fence
            src = "\n".join(body)
            if lang == "mermaid":
                out.append('<div class="mermaid">%s</div>' % html.escape(src))
            elif lang == "youtube":
                parts = src.strip().split("\n", 1)
                url = parts[0].strip()
                cap = parts[1].strip() if len(parts) > 1 else ""
                vid = yt_id(url)
                thumb = (' style="background-image:url(https://i.ytimg.com/vi/%s/hqdefault.jpg)"' % html.escape(vid)) if vid else ""
                out.append(
                    '<div class="yt" data-id="%s">'
                    '<button class="yt-play" type="button" aria-label="Play video"%s>'
                    '<span class="yt-tri">&#9654;</span></button>'
                    '<div class="yt-meta"><a href="%s" target="_blank" rel="noopener">%s</a>'
                    '<div class="yt-cap">%s</div></div></div>'
                    % (html.escape(vid), thumb, html.escape(url), html.escape(url), inline(cap))
                )
            elif lang == "prompt":
                out.append(
                    '<div class="promptcard"><div class="promptcard-h">'
                    '<span>🖼️ Image / AI prompt</span>'
                    '<button class="copybtn" type="button">Copy</button></div>'
                    '<pre><code>%s</code></pre></div>' % html.escape(src)
                )
            else:
                tag = ('<span class="lang">%s</span>' % html.escape(lang)) if lang else ""
                out.append('<pre class="code">%s<code>%s</code></pre>' % (tag, html.escape(src)))
            continue

        # raw block html passthrough (details/summary/p/div/img...) with image-path fixup
        if re.match(r"</?[a-zA-Z][\w-]*", stripped):
            out.append(re.sub(r'src="([^"]+)"',
                              lambda m: 'src="%s"' % html.escape(resolve_src(m.group(1))), line))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^---+\s*$", stripped):
            out.append("<hr>")
            i += 1
            continue

        # heading
        hm = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if hm:
            lvl = len(hm.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, inline(hm.group(2)), lvl))
            i += 1
            continue

        # table
        if "|" in line and i + 1 < n and re.match(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$", lines[i + 1]):
            def cells(row):
                row = row.strip().strip("|")
                return [c.strip() for c in row.split("|")]
            header = cells(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(cells(lines[i]))
                i += 1
            out.append("<div class='tablewrap'><table><thead><tr>"
                       + "".join("<th>%s</th>" % inline(c) for c in header)
                       + "</tr></thead><tbody>")
            for r in rows:
                out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
            out.append("</tbody></table></div>")
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = " ".join(x for x in buf if x.strip())
            out.append("<blockquote>%s</blockquote>" % inline(inner))
            continue

        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            buf = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append(re.sub(r"^\s*[-*]\s+", "", lines[i]))
                i += 1
            flush_list(buf, False)
            continue

        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            buf = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append(re.sub(r"^\s*\d+\.\s+", "", lines[i]))
                i += 1
            flush_list(buf, True)
            continue

        # blank
        if not stripped:
            i += 1
            continue

        # paragraph (gather until blank / block start)
        buf = [line]
        i += 1
        while i < n and lines[i].strip() and not re.match(
                r"^\s*(#{1,6}\s|[-*]\s|\d+\.\s|>|```|---+\s*$|\|)", lines[i]) \
                and not re.match(r"</?[a-zA-Z]", lines[i].strip()):
            buf.append(lines[i])
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(buf)))

    return "\n".join(out)


# ----------------------------------------------------------------------------- assemble
def build():
    global CUR_DIR
    pages_html = []
    nav_groups = []
    cur_group = None
    for path, pid, title, group in PAGES:
        with open(os.path.join(HERE, path), encoding="utf-8") as f:
            md = f.read()
        CUR_DIR = os.path.dirname(path)
        body = md_to_html(md)
        is_atom = pid in ATOM_IDS
        done = ('<label class="donebox"><input type="checkbox" class="donechk" data-atom="%s"> '
                'Mark this atom complete</label>' % pid) if is_atom else ""
        pages_html.append('<section class="page" id="page-%s" data-id="%s">%s%s</section>'
                          % (pid, pid, done, body))
        if group != cur_group:
            nav_groups.append('<div class="nav-group">%s</div>' % html.escape(group))
            cur_group = group
        nav_groups.append(
            '<a class="navlink" data-target="%s" href="#%s">%s</a>' % (pid, pid, html.escape(title)))
    nav = "\n".join(nav_groups)
    pages = "\n".join(pages_html)
    out = TEMPLATE.replace("{{NAV}}", nav).replace("{{PAGES}}", pages)
    dest = os.path.join(HERE, "course.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(out)
    print("Wrote", dest, "(%d KB)" % (len(out) // 1024))


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>🧩 Problem Solving · ADA Micro-Credential</title>
<link rel="icon" href="../../img/Isotipo.png">
<style>
:root{
  --ink:#0A1124; --indigo:#1E2A6E; --turq:#15B5C6; --gold:#E0A53C;
  --bg:#f6f8fc; --surface:#ffffff; --border:#e2e7f2; --text:#1b2440; --muted:#5b6685;
  --radius:14px; --shadow:0 6px 24px rgba(20,30,70,.08);
}
*{box-sizing:border-box}
html,body{margin:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Inter,Arial,sans-serif;
  background:var(--bg);color:var(--text);line-height:1.65}
a{color:var(--indigo);text-decoration:none}
a:hover{text-decoration:underline}
.app{display:grid;grid-template-columns:300px minmax(0,1fr);min-height:100vh}

/* sidebar */
.side{position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--ink);color:#dfe5fb;
  padding:18px 14px;border-right:1px solid #111a36}
.brand{display:flex;align-items:center;gap:10px;padding:6px 6px 14px}
.brand img{width:40px;height:40px;animation:spin 9s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.brand b{font-size:15px;color:#fff;line-height:1.2}
.brand small{display:block;color:var(--turq);font-weight:600;font-size:11px;letter-spacing:.04em}
.progwrap{margin:8px 6px 16px}
.progbar{height:8px;border-radius:8px;background:#1b2547;overflow:hidden}
.progfill{height:100%;width:0;background:linear-gradient(90deg,var(--turq),var(--gold));transition:width .5s}
.progtext{font-size:11px;color:#9fb0e6;margin-top:6px}
.nav-group{font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:#8fa0d8;
  margin:14px 8px 4px;font-weight:700}
.navlink{display:block;padding:8px 10px;border-radius:9px;color:#cdd6f6;font-size:14px;margin:2px 0}
.navlink:hover{background:#16204180;text-decoration:none;color:#fff}
.navlink.active{background:linear-gradient(90deg,var(--indigo),#2a3aa0);color:#fff;font-weight:600}

/* main */
.main{padding:0}
.topbar{position:sticky;top:0;z-index:5;background:rgba(246,248,252,.85);backdrop-filter:blur(8px);
  border-bottom:1px solid var(--border);padding:12px 28px;display:flex;align-items:center;gap:14px}
.topbar .pill{font-size:12px;font-weight:700;color:#fff;background:var(--indigo);padding:4px 12px;border-radius:30px}
.topbar .sp{flex:1}
.navbtn{border:1px solid var(--border);background:var(--surface);color:var(--text);border-radius:9px;
  padding:7px 14px;font-size:13px;cursor:pointer;font-weight:600}
.navbtn:hover{border-color:var(--turq)}
.navbtn:disabled{opacity:.4;cursor:not-allowed}
.wrap{max-width:880px;margin:0 auto;padding:30px 28px 90px}
.page{display:none;animation:fade .35s ease}
.page.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

h1,h2,h3,h4{color:var(--indigo);line-height:1.25}
h1{font-size:30px;margin:.2em 0 .5em;border-bottom:3px solid var(--turq);padding-bottom:.3em}
h2{font-size:22px;margin:1.5em 0 .5em}
h3{font-size:18px;margin:1.3em 0 .4em}
h4{font-size:15px;margin:1.1em 0 .3em;color:var(--ink)}
p{margin:.7em 0}
hr{border:0;border-top:1px solid var(--border);margin:1.6em 0}
ul,ol{padding-left:1.4em;margin:.6em 0}
li{margin:.3em 0}
li input[type=checkbox]{margin-right:6px}
img{max-width:100%;border-radius:10px}
code{background:#eef1f9;padding:.12em .4em;border-radius:6px;font-size:.88em;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;color:#27306b}
pre.code{background:var(--ink);color:#e7ecff;padding:16px 18px;border-radius:var(--radius);
  overflow:auto;position:relative;box-shadow:var(--shadow)}
pre.code code{background:none;color:inherit;padding:0;font-size:13.5px;line-height:1.6}
pre.code .lang{position:absolute;top:8px;right:12px;font-size:10px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--turq);font-family:inherit}
blockquote{margin:1em 0;padding:.7em 1.1em;border-left:4px solid var(--gold);
  background:#fff8ec;border-radius:0 10px 10px 0;color:#5a4a23}
.tablewrap{overflow-x:auto;margin:1em 0;border:1px solid var(--border);border-radius:var(--radius)}
table{border-collapse:collapse;width:100%;font-size:14px;background:var(--surface)}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--border);vertical-align:top}
th{background:var(--indigo);color:#fff;font-weight:600}
tr:nth-child(even) td{background:#f7f9fe}

.donebox{float:right;display:inline-flex;align-items:center;gap:7px;background:var(--surface);
  border:1px solid var(--border);border-radius:30px;padding:6px 14px;font-size:13px;font-weight:600;
  color:var(--muted);cursor:pointer;box-shadow:var(--shadow)}
.donebox input{accent-color:var(--turq)}

/* youtube facade */
.yt{margin:1.2em 0;border-radius:var(--radius);overflow:hidden;background:var(--ink);box-shadow:var(--shadow)}
.yt .yt-play{position:relative;display:block;width:100%;aspect-ratio:16/9;border:0;cursor:pointer;
  background:radial-gradient(circle at 50% 45%,#243069,#0A1124);background-size:cover;background-position:center;color:#fff}
.yt .yt-play::after{content:"";position:absolute;inset:0;background:rgba(10,17,36,.38)}
.yt-tri{position:relative;z-index:1;font-size:42px;color:#fff;background:rgba(225,165,60,.92);width:84px;height:58px;
  border-radius:16px;display:grid;place-items:center;margin:0 auto;box-shadow:0 6px 18px rgba(0,0,0,.4);
  transition:transform .2s}
.yt .yt-play:hover .yt-tri{transform:scale(1.08)}
.yt iframe{display:block;width:100%;aspect-ratio:16/9;border:0}
.yt-meta{padding:9px 14px;font-size:13px;background:#121c3a}
.yt-meta a{color:var(--turq);word-break:break-all}
.yt-cap{color:#aebadf;font-size:12px;margin-top:2px}

/* prompt card */
.promptcard{margin:1.2em 0;border:1px solid #d9c79a;border-radius:var(--radius);overflow:hidden;
  background:#fffdf6;box-shadow:var(--shadow)}
.promptcard-h{display:flex;align-items:center;justify-content:space-between;padding:8px 14px;
  background:linear-gradient(90deg,#fbf0d6,#fff7e6);font-weight:700;color:#7a5b16;font-size:13px}
.promptcard pre{margin:0;padding:14px 16px;white-space:pre-wrap;font-size:13px;color:#4a4634;
  font-family:ui-monospace,Menlo,monospace}
.copybtn{border:1px solid var(--gold);background:#fff;color:#8a6516;border-radius:7px;
  padding:3px 12px;font-size:12px;cursor:pointer;font-weight:700}
.copybtn:hover{background:var(--gold);color:#fff}
.copybtn.ok{background:var(--turq);border-color:var(--turq);color:#fff}

/* mermaid */
.mermaid{margin:1.2em 0;text-align:center;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius);padding:18px;box-shadow:var(--shadow)}
.mermaid.fallback{text-align:left;background:var(--ink)}
.mermaid.fallback pre{color:#e7ecff;margin:0;white-space:pre-wrap;font-size:12px}
.mermaid svg .nodeLabel,.mermaid svg .label{font-weight:600}
.mermaid svg .edgeLabel,.mermaid svg .edgeLabel *{color:#1E2A6E !important;font-weight:600}

@media(max-width:880px){
  .app{grid-template-columns:1fr}
  .side{position:fixed;left:-300px;width:300px;z-index:30;transition:left .25s}
  .side.open{left:0}
  .menutoggle{display:inline-flex !important}
}
.menutoggle{display:none;align-items:center;justify-content:center;width:38px;height:38px;
  border:1px solid var(--border);background:var(--surface);border-radius:9px;cursor:pointer;font-size:18px}
</style>
</head>
<body>
<div class="app">
  <aside class="side" id="side">
    <div class="brand">
      <img src="../../img/Isotipo.png" alt="ADA">
      <div><b>Problem Solving</b><small>ADA MICRO-CREDENTIAL</small></div>
    </div>
    <div class="progwrap">
      <div class="progbar"><div class="progfill" id="progfill"></div></div>
      <div class="progtext" id="progtext">0 / 6 atoms complete</div>
    </div>
    <nav id="nav">{{NAV}}</nav>
  </aside>
  <div class="main">
    <div class="topbar">
      <button class="menutoggle" id="menutoggle" aria-label="Menu">&#9776;</button>
      <span class="pill">🧩 Problem Solving</span>
      <span class="sp"></span>
      <button class="navbtn" id="prevbtn">&larr; Prev</button>
      <button class="navbtn" id="nextbtn">Next &rarr;</button>
    </div>
    <div class="wrap">{{PAGES}}</div>
  </div>
</div>

<script>
(function(){
  var pages=Array.prototype.slice.call(document.querySelectorAll(".page"));
  var ids=pages.map(function(p){return p.getAttribute("data-id");});
  var links=Array.prototype.slice.call(document.querySelectorAll(".navlink"));
  var atomIds=["atom-1","atom-2","atom-3","atom-4","atom-5","atom-6"];
  var idx=0;

  function show(id){
    var i=ids.indexOf(id); if(i<0)i=0; idx=i;
    pages.forEach(function(p){p.classList.toggle("active",p.getAttribute("data-id")===id);});
    links.forEach(function(a){a.classList.toggle("active",a.getAttribute("data-target")===id);});
    document.getElementById("prevbtn").disabled=(idx===0);
    document.getElementById("nextbtn").disabled=(idx===pages.length-1);
    if(location.hash.slice(1)!==id) history.replaceState(null,"","#"+id);
    document.getElementById("side").classList.remove("open");
    window.scrollTo(0,0);
    renderMermaid();
  }
  links.forEach(function(a){a.addEventListener("click",function(e){e.preventDefault();show(a.getAttribute("data-target"));});});
  document.getElementById("prevbtn").addEventListener("click",function(){if(idx>0)show(ids[idx-1]);});
  document.getElementById("nextbtn").addEventListener("click",function(){if(idx<ids.length-1)show(ids[idx+1]);});
  document.getElementById("menutoggle").addEventListener("click",function(){document.getElementById("side").classList.toggle("open");});

  // progress (localStorage)
  var KEY="problem-solving-progress";
  function load(){try{return JSON.parse(localStorage.getItem(KEY)||"{}");}catch(e){return {};}}
  function save(s){try{localStorage.setItem(KEY,JSON.stringify(s));}catch(e){}}
  function refresh(){
    var s=load(),done=0;
    document.querySelectorAll(".donechk").forEach(function(c){
      c.checked=!!s[c.getAttribute("data-atom")]; if(c.checked)done++;});
    var pct=Math.round(done/atomIds.length*100);
    document.getElementById("progfill").style.width=pct+"%";
    document.getElementById("progtext").textContent=done+" / "+atomIds.length+" atoms complete";
  }
  document.querySelectorAll(".donechk").forEach(function(c){
    c.addEventListener("change",function(){var s=load();s[c.getAttribute("data-atom")]=c.checked;save(s);refresh();});
  });
  refresh();

  // copy buttons
  document.querySelectorAll(".copybtn").forEach(function(b){
    b.addEventListener("click",function(){
      var pre=b.closest(".promptcard").querySelector("pre");
      var txt=pre.innerText;
      (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(function(){
        b.textContent="Copied!";b.classList.add("ok");setTimeout(function(){b.textContent="Copy";b.classList.remove("ok");},1400);
      }).catch(function(){
        var r=document.createRange();r.selectNodeContents(pre);var sel=getSelection();sel.removeAllRanges();sel.addRange(r);
        try{document.execCommand("copy");}catch(e){} sel.removeAllRanges();
        b.textContent="Copied!";b.classList.add("ok");setTimeout(function(){b.textContent="Copy";b.classList.remove("ok");},1400);
      });
    });
  });

  // youtube click-to-play
  document.querySelectorAll(".yt").forEach(function(y){
    var btn=y.querySelector(".yt-play");
    btn.addEventListener("click",function(){
      var id=y.getAttribute("data-id"); if(!id)return;
      // file:// pages can't host a YouTube iframe (Error 153) -> open on YouTube instead.
      if(location.protocol==="file:"){window.open("https://www.youtube.com/watch?v="+id,"_blank","noopener");return;}
      var f=document.createElement("iframe");
      f.src="https://www.youtube-nocookie.com/embed/"+id+"?autoplay=1&rel=0";
      f.allow="accelerated-sensors;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture;web-share;fullscreen";
      f.setAttribute("allowfullscreen","");
      f.setAttribute("referrerpolicy","strict-origin-when-cross-origin");
      f.title="YouTube video";
      btn.replaceWith(f);
    });
  });

  // mermaid (CDN, brand theme, root emphasis, graceful fallback)
  var mmReady=null;
  function ensureMermaid(){
    if(mmReady)return mmReady;
    mmReady=new Promise(function(res,rej){
      if(window.mermaid)return res(window.mermaid);
      var s=document.createElement("script");
      s.src="https://cdn.jsdelivr.net/npm/mermaid@11.15.0/dist/mermaid.min.js";
      s.onload=function(){res(window.mermaid);};
      s.onerror=function(){
        var s2=document.createElement("script");
        s2.src="https://unpkg.com/mermaid@11.15.0/dist/mermaid.min.js";
        s2.onload=function(){res(window.mermaid);}; s2.onerror=rej;
        document.head.appendChild(s2);
      };
      document.head.appendChild(s);
    });
    return mmReady;
  }
  function src(n){var s=n.getAttribute("data-src");if(s===null){s=n.textContent;n.setAttribute("data-src",s);}return s;}
  function fallback(n){n.classList.add("fallback");n.innerHTML="<pre>"+src(n).replace(/[&<>]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c];})+"</pre>";}
  function detectRoots(s){
    try{var L=s.split(/\r?\n/);if(!/^\s*(flowchart|graph)\b/i.test(L[0]||""))return [];
      var all={},tg={};
      for(var i=1;i<L.length;i++){var t=(L[i]||"").trim();
        if(!t||/^%%/.test(t))continue;
        if(/^(classdef|class|style|linkstyle|click|direction|subgraph|end)\b/i.test(t))continue;
        var x=L[i];for(var k=0;k<8;k++){x=x.replace(/\(\([^()]*\)\)/g," ").replace(/\[[^\[\]]*\]/g," ").replace(/\{[^{}]*\}/g," ").replace(/\([^()]*\)/g," ");}
        x=x.replace(/\|[^|]*\|/g," ");if(x.indexOf("--")<0&&x.indexOf("==")<0)continue;
        var ids=x.split(/\s*(?:-{2,}>?|={2,}>?|-\.->?)\s*/).map(function(z){return (z.trim().match(/^[A-Za-z0-9_]+/)||[""])[0];}).filter(Boolean);
        for(var j=0;j<ids.length;j++){all[ids[j]]=1;if(j>0)tg[ids[j]]=1;}}
      var r=Object.keys(all).filter(function(id){return !tg[id];});
      return r.length&&r.length<=4?r:[];
    }catch(e){return [];}
  }
  function emphasize(s){var r=detectRoots(s);if(!r.length)return s;
    return s+"\nclassDef adaRootNode fill:#1E2A6E,stroke:#E0A53C,stroke-width:3px,color:#ffffff,font-weight:bold,font-size:21px;\nclass "+r.join(",")+" adaRootNode;";}
  var seq=0;
  function renderMermaid(){
    var nodes=Array.prototype.slice.call(document.querySelectorAll(".page.active .mermaid:not([data-done])"));
    if(!nodes.length)return;
    nodes.forEach(src);
    ensureMermaid().then(function(m){
      m.initialize({startOnLoad:false,securityLevel:"loose",theme:"base",fontFamily:"inherit",fontSize:"16px",
        flowchart:{htmlLabels:true,useMaxWidth:true,curve:"basis",padding:14,nodeSpacing:52,rankSpacing:58},
        themeVariables:{fontSize:"16px",primaryColor:"#1E2A6E",primaryTextColor:"#ffffff",primaryBorderColor:"#15B5C6",
          mainBkg:"#1E2A6E",nodeBorder:"#15B5C6",nodeTextColor:"#ffffff",lineColor:"#1E2A6E",
          clusterBkg:"#eef2fb",clusterBorder:"#15B5C6",titleColor:"#1E2A6E",
          background:"#ffffff",textColor:"#1E2A6E",edgeLabelBackground:"#ffffff",
          cScale0:"#1E2A6E",cScale1:"#15B5C6",cScale2:"#E0A53C",cScale3:"#2a3aa0",
          cScaleLabel0:"#ffffff",cScaleLabel1:"#0A1124",cScaleLabel2:"#0A1124",cScaleLabel3:"#ffffff"}});
      nodes.forEach(function(n){
        n.setAttribute("data-done","1");
        var id="mm-"+(Date.now())+"-"+(seq++);
        try{m.render(id,emphasize(src(n))).then(function(o){n.innerHTML=o.svg;}).catch(function(){fallback(n);});}
        catch(e){fallback(n);}
      });
    }).catch(function(){nodes.forEach(fallback);});
  }

  window.addEventListener("hashchange",function(){show(location.hash.slice(1)||ids[0]);});
  show(location.hash.slice(1)||ids[0]);
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
