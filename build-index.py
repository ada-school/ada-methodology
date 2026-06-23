#!/usr/bin/env python3
"""
build-index.py — Generates a self-contained `index.html` that lets you browse and read
every Markdown file in this repository with a built-in renderer, navigation tree, search,
auto table-of-contents, dark/light theme, and CSS animations.

The Markdown content is embedded directly into the HTML, so `index.html` works when opened
directly from disk (file://) with NO web server and NO internet connection.

Re-run this script after changing docs:  python3 build-index.py
"""

import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Discover markdown files (skip .git and node_modules).
def find_md():
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules")]
        for fn in filenames:
            if fn.lower().endswith(".md"):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
                files.append(rel)
    return files

# Order: root docs first (README first), then specs, examples, guides, templates, .github.
FOLDER_PRIORITY = {"": 0, "specs": 1, "examples": 2, "guides": 3, "templates": 4, ".github": 5}

def sort_key(path):
    parts = path.split("/")
    folder = "" if len(parts) == 1 else parts[0]
    prio = FOLDER_PRIORITY.get(folder, 9)
    name = parts[-1].lower()
    # README / index files float to the top of their group.
    is_readme = 0 if name.startswith("readme") else 1
    return (prio, path.count("/"), is_readme, path.lower())

CSS = r"""
/* ADA School brand palette: Indigo #1E2A6E · Turquoise #15B5C6 · Gold #E0A53C · Ink #0A1124 */
:root{
  --bg:#0A1124; --bg-soft:#121c3a; --bg-elev:#1a2548; --border:#2a3663;
  --text:#e9edfb; --text-dim:#a3afd6; --text-faint:#6c79a6;
  --brand:#1E2A6E; --brand-bright:#4256c4;
  --accent:#15B5C6; --accent-2:#15B5C6; --accent-3:#1E2A6E; --gold:#E0A53C;
  --code-bg:#0c1430; --link:#3fc8d6;
  --grad-fill:linear-gradient(135deg,#15B5C6,#1E2A6E 90%);
  --grad-text:linear-gradient(120deg,#5fd6e3,#9fb0f0);
  --shadow:0 12px 44px rgba(2,6,23,.55);
  --sidebar-w:300px; --toc-w:230px; --radius:14px;
}
html[data-theme="light"]{
  --bg:#f3f6fc; --bg-soft:#ffffff; --bg-elev:#ffffff; --border:#dde3f2;
  --text:#1E2A6E; --text-dim:#4a5588; --text-faint:#8893b5;
  --brand:#1E2A6E; --brand-bright:#1E2A6E;
  --accent:#15B5C6; --accent-2:#15B5C6; --accent-3:#1E2A6E; --gold:#E0A53C;
  --code-bg:#eef2fa; --link:#1E2A6E;
  --grad-fill:linear-gradient(135deg,#15B5C6,#1E2A6E 90%);
  --grad-text:linear-gradient(120deg,#1E2A6E,#0f7d8a);
  --shadow:0 12px 44px rgba(30,42,110,.14);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  background:var(--bg); color:var(--text); line-height:1.65;
  -webkit-font-smoothing:antialiased; transition:background .4s ease,color .4s ease;
}
a{color:var(--link); text-decoration:none}
a:hover{text-decoration:underline}

/* progress bar */
#progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;
  background:linear-gradient(90deg,#15B5C6,#1E2A6E,#E0A53C);
  background-size:200% 100%; animation:flow 6s linear infinite; transition:width .1s ease;}
@keyframes flow{0%{background-position:0 0}100%{background-position:200% 0}}

/* header */
header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:14px;
  padding:10px 18px;background:rgba(10,17,36,.78);backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border); transition:background .4s ease;}
html[data-theme="light"] header{background:rgba(255,255,255,.82)}
.brand{display:flex;align-items:center;gap:12px;min-width:0}
.iso-spin{width:42px;height:42px;flex:0 0 auto;display:block;border-radius:50%;
  background:#0A1124;box-shadow:0 0 0 2px var(--border),0 4px 14px rgba(21,181,198,.28);
  animation:isospin 12s linear infinite;transition:box-shadow .3s ease}
.brand:hover .iso-spin{animation-duration:2.4s;box-shadow:0 0 0 2px var(--accent),0 6px 20px rgba(21,181,198,.5)}
@keyframes isospin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.iso-spin{animation:none}}
.brand h1{font-size:15px;margin:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--text)}
.brand small{display:block;color:var(--accent);font-size:11px;font-weight:600;letter-spacing:.3px}
html[data-theme="light"] .brand small{color:var(--brand)}
.spacer{flex:1}
.search{position:relative;display:flex;align-items:center}
.search input{background:var(--bg-soft);border:1px solid var(--border);color:var(--text);
  padding:9px 12px 9px 34px;border-radius:10px;width:230px;font-size:13px;outline:none;
  transition:width .25s ease,border-color .2s ease,box-shadow .2s ease}
.search input:focus{width:300px;border-color:var(--accent);box-shadow:0 0 0 3px rgba(21,181,198,.22)}
.search svg{position:absolute;left:10px;width:15px;height:15px;color:var(--text-faint);pointer-events:none}
.iconbtn{background:var(--bg-soft);border:1px solid var(--border);color:var(--text);
  width:38px;height:38px;border-radius:10px;cursor:pointer;display:grid;place-items:center;
  font-size:17px;transition:transform .2s ease,background .2s ease,border-color .2s ease}
.iconbtn:hover{transform:translateY(-2px) rotate(-6deg);border-color:var(--accent)}
.iconbtn:active{transform:scale(.92)}
.langsel{background:var(--bg-soft);border:1px solid var(--border);color:var(--text);
  height:38px;border-radius:10px;cursor:pointer;font-size:13px;font-weight:600;
  padding:0 8px;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
.langsel:hover{border-color:var(--accent)}
.langsel:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(21,181,198,.22)}
#menuBtn{display:none}

/* layout */
.layout{display:grid;grid-template-columns:var(--sidebar-w) minmax(0,1fr) var(--toc-w);
  max-width:1500px;margin:0 auto;align-items:start}

/* sidebar */
#sidebar{position:sticky;top:63px;height:calc(100vh - 63px);overflow-y:auto;
  padding:18px 12px 60px;border-right:1px solid var(--border);scrollbar-width:thin}
.nav-group{margin-bottom:6px}
.group-head{display:flex;align-items:center;gap:8px;padding:8px 10px;cursor:pointer;
  border-radius:9px;color:var(--text-dim);font-size:12px;font-weight:700;letter-spacing:.6px;
  text-transform:uppercase;user-select:none;transition:background .2s ease,color .2s ease}
.group-head:hover{background:var(--bg-soft);color:var(--text)}
.group-head .caret{margin-left:auto;transition:transform .3s ease;font-size:10px}
.group.collapsed .caret{transform:rotate(-90deg)}
.group-items{overflow:hidden;transition:max-height .35s ease,opacity .3s ease;opacity:1}
.group.collapsed .group-items{max-height:0!important;opacity:0}
.navlink{display:flex;align-items:center;gap:9px;padding:7px 10px 7px 12px;border-radius:9px;
  color:var(--text);font-size:13.5px;cursor:pointer;position:relative;
  transition:background .2s ease,transform .15s ease,color .2s ease;
  animation:slideIn .4s ease backwards}
.navlink .ic{opacity:.8;font-size:14px;width:16px;text-align:center;flex:0 0 auto}
.navlink:hover{background:var(--bg-soft);transform:translateX(4px);text-decoration:none}
.navlink.active{background:linear-gradient(90deg,rgba(21,181,198,.20),transparent);color:#fff;font-weight:600}
html[data-theme="light"] .navlink.active{color:var(--brand)}
.navlink.active::before{content:"";position:absolute;left:0;top:6px;bottom:6px;width:3px;
  border-radius:3px;background:linear-gradient(var(--accent),var(--accent-2))}
.navlink.nested{padding-left:26px;font-size:13px;color:var(--text-dim)}
.subfolder{padding:5px 10px 3px 18px;font-size:11px;color:var(--text-faint);font-weight:600;letter-spacing:.4px;text-transform:uppercase}
@keyframes slideIn{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:translateX(0)}}

/* content */
main{min-width:0;padding:34px 46px 120px;animation:fadeUp .5s ease}
#content{max-width:860px;margin:0 auto}
#content.swap{animation:fadeUp .45s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.crumbs{color:var(--text-faint);font-size:12.5px;margin-bottom:18px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.crumbs span{color:var(--text-dim)}

/* markdown typography */
.md{font-size:15.5px}
.md h1,.md h2,.md h3,.md h4{line-height:1.3;margin:1.6em 0 .6em;font-weight:700;scroll-margin-top:80px}
.md h1{font-size:2em;background:linear-gradient(120deg,var(--text),var(--text-dim));-webkit-background-clip:text;background-clip:text}
.md h2{font-size:1.5em;padding-bottom:.3em;border-bottom:1px solid var(--border)}
.md h3{font-size:1.2em}.md h4{font-size:1.05em;color:var(--text-dim)}
.md p{margin:.8em 0}
.md ul,.md ol{margin:.6em 0;padding-left:1.5em}
.md li{margin:.3em 0}
.md li input[type=checkbox]{margin-right:8px;accent-color:var(--accent)}
.md a{border-bottom:1px solid transparent;transition:border-color .2s}
.md a:hover{border-color:var(--link);text-decoration:none}
.md code{background:var(--code-bg);border:1px solid var(--border);padding:.12em .42em;
  border-radius:6px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em}
.md pre{background:var(--code-bg);border:1px solid var(--border);border-radius:12px;
  padding:16px 18px;overflow:auto;margin:1.1em 0;position:relative;box-shadow:inset 0 0 0 1px rgba(255,255,255,.02)}
.md pre code{background:none;border:none;padding:0;font-size:13px;line-height:1.6;display:block}
.md pre .lang-tag{position:absolute;top:8px;right:12px;font-size:10px;letter-spacing:1px;
  text-transform:uppercase;color:var(--text-faint)}
.md blockquote{margin:1em 0;padding:.5em 1.1em;border-left:4px solid var(--accent);
  background:var(--bg-soft);border-radius:0 10px 10px 0;color:var(--text-dim)}
.md blockquote p{margin:.35em 0}
.md hr{border:none;height:1px;background:var(--border);margin:2em 0}
.md table{border-collapse:collapse;width:100%;margin:1.2em 0;font-size:13.5px;
  border:1px solid var(--border);border-radius:12px;overflow:hidden;display:block;overflow-x:auto}
.md th,.md td{border:1px solid var(--border);padding:9px 13px;text-align:left;vertical-align:top}
.md th{background:var(--bg-soft);font-weight:700}
.md tr{transition:background .15s ease}
.md tbody tr:hover{background:var(--bg-soft)}
.md img{max-width:100%;border-radius:10px}
.md h2,.md h3{position:relative}
.anchor{opacity:0;margin-left:8px;font-size:.7em;color:var(--link);transition:opacity .2s}
.md h2:hover .anchor,.md h3:hover .anchor{opacity:1}

/* TOC */
#toc{position:sticky;top:63px;height:calc(100vh - 63px);overflow-y:auto;padding:30px 16px;
  border-left:1px solid var(--border);scrollbar-width:thin}
#toc .toc-title{font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--text-faint);
  font-weight:700;margin-bottom:12px}
#toc a{display:block;color:var(--text-dim);font-size:12.5px;padding:4px 10px;border-left:2px solid var(--border);
  margin-left:2px;transition:all .2s ease}
#toc a:hover{color:var(--text);border-color:var(--text-dim);text-decoration:none}
#toc a.lvl3{padding-left:22px;font-size:12px}
#toc a.active{color:var(--link);border-color:var(--accent);background:var(--bg-soft)}

/* home */
.hero{padding:30px 0 10px;animation:fadeUp .6s ease}
.hero .badge{display:inline-block;padding:5px 12px;border-radius:30px;font-size:12px;font-weight:600;
  background:var(--bg-soft);border:1px solid var(--border);color:var(--link);margin-bottom:16px}
.hero h2{font-size:2.4em;margin:.1em 0 .2em;line-height:1.15;border:none}
.hero .grad{background:var(--grad-text);
  -webkit-background-clip:text;background-clip:text;color:transparent;background-size:200% 200%;animation:flow 7s ease infinite}
.hero p.lead{font-size:1.15em;color:var(--text-dim);max-width:640px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:14px;margin:28px 0}
.stat{background:var(--bg-soft);border:1px solid var(--border);border-radius:var(--radius);padding:18px;
  transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease}
.stat:hover{transform:translateY(-5px);border-color:var(--accent);box-shadow:var(--shadow)}
.stat .num{font-size:1.9em;font-weight:800;background:var(--grad-text);-webkit-background-clip:text;background-clip:text;color:transparent}
.stat .lbl{color:var(--text-dim);font-size:12.5px;margin-top:2px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin:24px 0}
.card{background:var(--bg-soft);border:1px solid var(--border);border-radius:var(--radius);padding:20px;
  cursor:pointer;transition:transform .25s ease,border-color .25s,box-shadow .25s;position:relative;overflow:hidden}
.card::after{content:"";position:absolute;inset:0;background:linear-gradient(135deg,rgba(21,181,198,.14),transparent 60%);
  opacity:0;transition:opacity .3s}
.card:hover{transform:translateY(-6px);border-color:var(--accent);box-shadow:var(--shadow)}
.card:hover::after{opacity:1}
.card .ic{font-size:26px}.card h3{margin:10px 0 6px;font-size:1.05em}
.card p{color:var(--text-dim);font-size:13px;margin:0}
.pipeline{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:26px 0;padding:20px;
  background:var(--bg-soft);border:1px solid var(--border);border-radius:var(--radius)}
.pnode{padding:9px 14px;border-radius:10px;font-size:12.5px;font-weight:600;
  background:var(--bg-elev);border:1px solid var(--border);transition:transform .2s,border-color .2s}
.pnode:hover{transform:scale(1.06);border-color:var(--accent)}
.pnode.gold{border-color:var(--gold);color:var(--gold);background:rgba(224,165,60,.10);font-weight:800}
.parrow{color:var(--link);font-weight:800}

/* scroll top */
#top{position:fixed;right:24px;bottom:24px;width:46px;height:46px;border-radius:50%;border:none;
  background:linear-gradient(135deg,#15B5C6,#1E2A6E);color:#fff;font-size:20px;cursor:pointer;
  display:grid;place-items:center;opacity:0;pointer-events:none;transform:translateY(20px) scale(.8);
  transition:all .3s ease;box-shadow:0 8px 24px rgba(21,181,198,.42);z-index:40}
#top.show{opacity:1;pointer-events:auto;transform:translateY(0) scale(1)}
#top:hover{transform:translateY(-4px) scale(1.08)}

.overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);opacity:0;pointer-events:none;
  transition:opacity .3s;z-index:45}
.overlay.show{opacity:1;pointer-events:auto}
.empty{color:var(--text-faint);text-align:center;padding:60px 20px}

/* ===== mermaid diagram viewer ===== */
.mermaid{margin:1.5em 0;animation:fadeUp .5s ease}
/* pre-render state: hide raw source, show a loading shimmer */
.mermaid:not([data-processed]):not(.fallback){display:block;position:relative;min-height:120px;
  border:1px solid var(--border);border-radius:var(--radius);background:var(--bg-soft);
  color:transparent;font-size:0;overflow:hidden}
.mermaid:not([data-processed]):not(.fallback)::after{content:"";position:absolute;inset:0;
  background:linear-gradient(100deg,transparent 20%,rgba(21,181,198,.12) 50%,transparent 80%);
  background-size:200% 100%;animation:shimmer 1.2s linear infinite}
.mermaid:not([data-processed]):not(.fallback)::before{content:"⚛ rendering diagram\2026";
  position:absolute;inset:0;display:grid;place-items:center;color:var(--text-faint);
  font-family:inherit;font-size:13px;z-index:1}
@keyframes shimmer{0%{background-position:200% 0}100%{background-position:-200% 0}}
.mermaid.fallback{display:block;background:var(--bg-soft);border:1px solid var(--border);
  border-radius:var(--radius);padding:16px;text-align:left}

.diagram{position:relative;border:1px solid var(--border);border-radius:var(--radius);
  background:var(--bg-soft);overflow:hidden}
.diagram-canvas{overflow:hidden;display:flex;align-items:center;justify-content:center;
  padding:20px;min-height:120px;cursor:grab;touch-action:none;
  background:radial-gradient(circle at 50% 0,rgba(21,181,198,.06),transparent 60%)}
.diagram-canvas.grabbing{cursor:grabbing}
.diagram-canvas svg{max-width:100%;height:auto;transform-origin:center center;
  transition:transform .12s cubic-bezier(.2,.7,.3,1);will-change:transform}
.diagram-canvas.dragging svg{transition:none}
.diagram-canvas svg .nodeLabel,.diagram-canvas svg .label{font-weight:600}
.diagram-canvas svg .cluster .nodeLabel,.diagram-canvas svg .cluster-label .nodeLabel{font-weight:700}
/* edge labels reuse mermaid's .nodeLabel class, so force a readable (non-white) color */
.diagram-canvas svg .edgeLabel,.diagram-canvas svg .edgeLabel p,
.diagram-canvas svg .edgeLabel .nodeLabel,.diagram-canvas svg .edgeLabel .label,
.diagram-canvas svg .edgeLabel foreignObject *{color:#e9edfb !important;font-weight:600}
html[data-theme="light"] .diagram-canvas svg .edgeLabel,
html[data-theme="light"] .diagram-canvas svg .edgeLabel p,
html[data-theme="light"] .diagram-canvas svg .edgeLabel .nodeLabel,
html[data-theme="light"] .diagram-canvas svg .edgeLabel .label,
html[data-theme="light"] .diagram-canvas svg .edgeLabel foreignObject *{color:#1E2A6E !important}
.diagram-toolbar{position:absolute;top:8px;right:8px;display:flex;gap:4px;z-index:3;
  opacity:0;transform:translateY(-4px);transition:opacity .2s ease,transform .2s ease}
.diagram:hover .diagram-toolbar,.diagram:focus-within .diagram-toolbar{opacity:1;transform:none}
.dzlabel{position:absolute;left:10px;bottom:8px;z-index:3;font-size:11px;font-weight:600;
  color:var(--text-faint);background:var(--bg);border:1px solid var(--border);
  border-radius:20px;padding:2px 9px;opacity:0;transition:opacity .2s ease;pointer-events:none}
.diagram:hover .dzlabel{opacity:1}
.dbtn{width:30px;height:30px;border-radius:8px;border:1px solid var(--border);background:var(--bg);
  color:var(--text);cursor:pointer;display:grid;place-items:center;font-size:14px;line-height:1;
  transition:transform .15s ease,background .15s ease,border-color .15s ease,color .15s ease}
.dbtn:hover{transform:translateY(-1px);border-color:var(--accent);background:var(--bg-soft)}
.dbtn:active{transform:scale(.88)}
.dbtn.ok{border-color:var(--gold);color:var(--gold)}

/* fullscreen diagram modal */
.dmodal{position:fixed;inset:0;z-index:200;background:rgba(10,17,36,.94);display:none;
  flex-direction:column;backdrop-filter:blur(8px)}
.dmodal.open{display:flex;animation:fadeIn .22s ease}
.dmodal .dm-bar{display:flex;align-items:center;gap:6px;justify-content:flex-end;
  padding:12px 16px;border-bottom:1px solid var(--border)}
.dmodal .dm-stage{flex:1;overflow:hidden;display:flex;align-items:center;justify-content:center;
  padding:14px;cursor:grab;touch-action:none}
.dmodal .dm-stage.grabbing{cursor:grabbing}
.dmodal .dm-stage svg{max-width:94vw;max-height:82vh;height:auto;transform-origin:center center;
  transition:transform .12s cubic-bezier(.2,.7,.3,1)}
.dmodal .dm-stage.dragging svg{transition:none}
.dmodal-hint,.dm-hint{color:var(--text-faint);font-size:12px;margin-right:auto;padding-left:4px}

/* responsive */
@media(max-width:1080px){.layout{grid-template-columns:var(--sidebar-w) minmax(0,1fr)}#toc{display:none}}
@media(max-width:760px){
  .layout{grid-template-columns:1fr}
  #sidebar{position:fixed;left:0;top:63px;z-index:46;width:84%;max-width:330px;background:var(--bg);
    transform:translateX(-104%);transition:transform .32s cubic-bezier(.4,0,.2,1)}
  #sidebar.open{transform:translateX(0);box-shadow:var(--shadow)}
  #menuBtn{display:grid}
  main{padding:24px 20px 100px}
  .search input{width:110px}.search input:focus{width:160px}
  .langsel{padding:0 4px;font-size:12px}
  .brand small{display:none}
}
@media(max-width:480px){.brand h1{display:none}.search input{width:84px}}
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:10px;border:2px solid var(--bg)}
::-webkit-scrollbar-thumb:hover{background:var(--text-faint)}
"""

JS = r"""
(function(){
  "use strict";
  // ---- collect embedded docs ----
  var DOCS = {};
  var ORDER = [];
  document.querySelectorAll('script[type="text/markdown"]').forEach(function(s){
    var p = s.getAttribute('data-path');
    DOCS[p] = s.textContent;
    ORDER.push(p);
  });

  // ---- i18n: simple JSON string map + EN/ES/PT switcher ----
  // Only the UI "chrome" + the home dashboard are translated. Document bodies are
  // shown in their own language; v2 specs are English-only (canonical source).
  var I18N = {
    en: {
      subtitle:"Applied Digital Apprenticeship",
      search:"Search docs\u2026  ( / )",
      onThisPage:"On this page",
      result:"result", results:"results", noMatches:"No matches",
      heroBadge:"\uD83D\uDCDA Interactive Docs Browser",
      heroTitle:"ADA Methodology", heroGrad:"Applied Digital Apprenticeship",
      heroLead:"Browse the full methodology, v2 KSA specifications, templates, and worked examples \u2014 rendered right here, no server required.",
      stDocs:"Documents", stSpecs:"v2 Specs", stExamples:"Examples", stTemplates:"Templates", stLangs:"Languages",
      pPosting:"\uD83D\uDCC4 Job Posting", pProfile:"\uD83E\uDDEC KSA Profile", pMap:"\uD83D\uDDFA\uFE0F Skills Map", pMC:"\u269B Micro-credentials", pReady:"\uD83C\uDFC5 Job-Ready",
      jumpIn:"Jump in", readme:"README.md",
      cards:{
        method:{h:"Methodology (v1)",d:"The canonical ADA methodology: atoms, phases, micro-credentials."},
        ksa:{h:"ADA v2 \u2014 KSA",d:"Knowledge \u00B7 Skills \u00B7 Abilities competency spine."},
        role:{h:"Role \u2192 Pathway",d:"Deconstruct a job into micro-credentials via high-performer observation."},
        map:{h:"Skills Map",d:"Gap graph + job-match score model."},
        genai:{h:"Gen AI Workflow",d:"Posting \u2192 profile \u2192 atoms, with human gates."},
        example:{h:"End-to-End Example",d:"From a job posting to job-ready, fully worked."},
        agent:{h:"Agent Guide",d:"How AI assistants should work in this repo."}
      }
    },
    es: {
      subtitle:"Aprendizaje Digital Aplicado",
      search:"Buscar documentos\u2026  ( / )",
      onThisPage:"En esta p\u00E1gina",
      result:"resultado", results:"resultados", noMatches:"Sin coincidencias",
      heroBadge:"\uD83D\uDCDA Explorador Interactivo de Documentos",
      heroTitle:"Metodolog\u00EDa ADA", heroGrad:"Aprendizaje Digital Aplicado",
      heroLead:"Explora la metodolog\u00EDa completa, las especificaciones KSA v2, plantillas y ejemplos pr\u00E1cticos \u2014 renderizados aqu\u00ED mismo, sin servidor.",
      stDocs:"Documentos", stSpecs:"Specs v2", stExamples:"Ejemplos", stTemplates:"Plantillas", stLangs:"Idiomas",
      pPosting:"\uD83D\uDCC4 Oferta Laboral", pProfile:"\uD83E\uDDEC Perfil KSA", pMap:"\uD83D\uDDFA\uFE0F Mapa de Habilidades", pMC:"\u269B Micro-credenciales", pReady:"\uD83C\uDFC5 Listo para el Trabajo",
      jumpIn:"Empieza aqu\u00ED", readme:"README-ES.md",
      cards:{
        method:{h:"Metodolog\u00EDa (v1)",d:"La metodolog\u00EDa ADA can\u00F3nica: \u00E1tomos, fases, micro-credenciales."},
        ksa:{h:"ADA v2 \u2014 KSA",d:"Columna de competencias Conocimientos \u00B7 Habilidades \u00B7 Aptitudes."},
        role:{h:"Cargo \u2192 Ruta",d:"Descompon un cargo en micro-credenciales con observaci\u00F3n de altos desempe\u00F1os."},
        map:{h:"Mapa de Habilidades",d:"Grafo de brechas + modelo de puntaje de match laboral."},
        genai:{h:"Flujo con IA Generativa",d:"Oferta \u2192 perfil \u2192 \u00E1tomos, con validaci\u00F3n humana."},
        example:{h:"Ejemplo de Principio a Fin",d:"De una oferta laboral a estar listo para el trabajo."},
        agent:{h:"Gu\u00EDa para Agentes",d:"C\u00F3mo deben trabajar los asistentes de IA en este repo."}
      }
    },
    pt: {
      subtitle:"Aprendizado Digital Aplicado",
      search:"Buscar documentos\u2026  ( / )",
      onThisPage:"Nesta p\u00E1gina",
      result:"resultado", results:"resultados", noMatches:"Nenhuma correspond\u00EAncia",
      heroBadge:"\uD83D\uDCDA Navegador Interativo de Documentos",
      heroTitle:"Metodologia ADA", heroGrad:"Aprendizado Digital Aplicado",
      heroLead:"Explore a metodologia completa, as especifica\u00E7\u00F5es KSA v2, modelos e exemplos pr\u00E1ticos \u2014 renderizados aqui mesmo, sem servidor.",
      stDocs:"Documentos", stSpecs:"Specs v2", stExamples:"Exemplos", stTemplates:"Modelos", stLangs:"Idiomas",
      pPosting:"\uD83D\uDCC4 Vaga de Emprego", pProfile:"\uD83E\uDDEC Perfil KSA", pMap:"\uD83D\uDDFA\uFE0F Mapa de Habilidades", pMC:"\u269B Micro-credenciais", pReady:"\uD83C\uDFC5 Pronto para o Trabalho",
      jumpIn:"Comece aqui", readme:"README-PT-BR.md",
      cards:{
        method:{h:"Metodologia (v1)",d:"A metodologia ADA can\u00F4nica: \u00E1tomos, fases, micro-credenciais."},
        ksa:{h:"ADA v2 \u2014 KSA",d:"Coluna de compet\u00EAncias Conhecimentos \u00B7 Habilidades \u00B7 Aptid\u00F5es."},
        role:{h:"Vaga \u2192 Trilha",d:"Decomponha uma vaga em micro-credenciais via observa\u00E7\u00E3o de alto desempenho."},
        map:{h:"Mapa de Habilidades",d:"Grafo de lacunas + modelo de pontua\u00E7\u00E3o de match de vaga."},
        genai:{h:"Fluxo com IA Generativa",d:"Vaga \u2192 perfil \u2192 \u00E1tomos, com valida\u00E7\u00E3o humana."},
        example:{h:"Exemplo Ponta a Ponta",d:"De uma vaga at\u00E9 estar pronto para o trabalho."},
        agent:{h:"Guia para Agentes",d:"Como assistentes de IA devem trabalhar neste reposit\u00F3rio."}
      }
    }
  };
  var LANG = "en";
  function t(k){ var o = I18N[LANG] || I18N.en; return (k in o) ? o[k] : I18N.en[k]; }

  var FOLDER_META = {
    "":         {icon:"📄", label:"Overview"},
    "specs":    {icon:"🧬", label:"Specs · ADA v2"},
    "examples": {icon:"📘", label:"Examples"},
    "guides":   {icon:"🗺️", label:"Guides"},
    "templates":{icon:"🧩", label:"Templates"},
    ".github":  {icon:"⚙️", label:".github"}
  };
  function fileIcon(p){
    if(/readme/i.test(p)) return "🏠";
    if(p.indexOf("specs/")===0) return "🧬";
    if(p.indexOf("examples/")===0) return "📘";
    if(p.indexOf("guides/")===0) return "🗺️";
    if(p.indexOf("templates/")===0) return "🧩";
    if(/claude/i.test(p)) return "🤖";
    if(/contributing/i.test(p)) return "🤝";
    return "📄";
  }
  function prettyName(p){
    var n = p.split("/").pop().replace(/\.md$/i,"");
    return n.replace(/[-_]/g," ").replace(/\b\w/g,function(c){return c.toUpperCase()})
            .replace(/\bEs\b/,"ES").replace(/\bPt Br\b/i,"PT-BR").replace(/Ksa/i,"KSA")
            .replace(/Ada/g,"ADA").replace(/Rest/i,"REST").replace(/Genai/i,"GenAI")
            .replace(/V2/i,"v2");
  }

  // =====================================================================
  // Minimal, dependency-free Markdown -> HTML renderer (GFM-ish).
  // =====================================================================
  function slugify(t){
    return t.toLowerCase().replace(/<[^>]+>/g,"")
      .replace(/[^\w\u00c0-\u024f \-]/g,"").trim().replace(/\s+/g,"-").replace(/-+/g,"-") || "section";
  }
  function escapeHtml(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");}

  function inline(text){
    var codes=[];
    text = text.replace(/`([^`]+)`/g,function(m,c){codes.push(c);return "\u0001"+(codes.length-1)+"\u0001";});
    text = escapeHtml(text);
    text = text.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+&quot;[^&]*&quot;)?\)/g,'<img alt="$1" src="$2">');
    text = text.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g,'<img alt="$1" src="$2">');
    text = text.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g,'<a href="$2">$1</a>');
    text = text.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
    text = text.replace(/__([^_]+)__/g,'<strong>$1</strong>');
    text = text.replace(/(^|[\s(])\*([^*\s][^*]*?)\*(?=[\s).,!?:;]|$)/g,'$1<em>$2</em>');
    text = text.replace(/(^|[\s(])_([^_\s][^_]*?)_(?=[\s).,!?:;]|$)/g,'$1<em>$2</em>');
    text = text.replace(/~~([^~]+)~~/g,'<del>$1</del>');
    text = text.replace(/\u0001(\d+)\u0001/g,function(m,i){return "<code>"+escapeHtml(codes[+i])+"</code>";});
    return text;
  }

  function parse(md, toc){
    md = md.replace(/\r\n?/g,"\n");
    var blocks=[];
    md = md.replace(/```([^\n]*)\n([\s\S]*?)```/g,function(m,lang,code){
      blocks.push({lang:(lang||"").trim(),code:code.replace(/\n$/,"")});
      return "\n\u0000"+(blocks.length-1)+"\u0000\n";
    });
    var lines = md.split("\n");
    var out=[], i=0, slugs={};
    function uid(s){var b=s,n=1;while(slugs[s]){s=b+"-"+(n++);}slugs[s]=1;return s;}

    function listBlock(){
      var items=[];
      while(i<lines.length){
        var m=lines[i].match(/^(\s*)([-*+]|\d+\.)\s+(.*)$/);
        if(!m) break;
        items.push({indent:m[1].replace(/\t/g,"  ").length, ordered:/\d/.test(m[2]), text:m[3]});
        i++;
      }
      var hostHtml="", stack=[];
      items.forEach(function(it){
        while(stack.length && it.indent < stack[stack.length-1].indent)
          hostHtml += stack.pop().ordered?"</ol>":"</ul>";
        if(!stack.length || it.indent > stack[stack.length-1].indent){
          hostHtml += it.ordered?"<ol>":"<ul>"; stack.push(it);
        } else if(it.ordered!==stack[stack.length-1].ordered){
          hostHtml += stack.pop().ordered?"</ol>":"</ul>";
          hostHtml += it.ordered?"<ol>":"<ul>"; stack.push(it);
        }
        var t=it.text, tm=t.match(/^\[([ xX])\]\s+(.*)$/);
        if(tm){ t='<input type="checkbox" disabled '+(tm[1].toLowerCase()==="x"?"checked":"")+"> "+inline(tm[2]); }
        else { t=inline(t); }
        hostHtml += "<li>"+t+"</li>";
      });
      while(stack.length) hostHtml += stack.pop().ordered?"</ol>":"</ul>";
      out.push(hostHtml);
    }

    function tableBlock(){
      var header=lines[i], sep=lines[i+1];
      var aligns = sep.split("|").map(function(c){return c.trim();}).filter(function(c){return c.length;})
        .map(function(c){var l=c[0]===":",r=c[c.length-1]===":";return r&&l?"center":r?"right":l?"left":"";});
      function row(line){return line.replace(/^\s*\|/,"").replace(/\|\s*$/,"").split("|").map(function(c){return c.trim();});}
      var h=row(header), html="<table><thead><tr>";
      h.forEach(function(c,idx){html+="<th"+(aligns[idx]?' style="text-align:'+aligns[idx]+'"':"")+">"+inline(c)+"</th>";});
      html+="</tr></thead><tbody>";
      i+=2;
      while(i<lines.length && lines[i].indexOf("|")>-1 && lines[i].trim()!==""){
        var r=row(lines[i]); html+="<tr>";
        r.forEach(function(c,idx){html+="<td"+(aligns[idx]?' style="text-align:'+aligns[idx]+'"':"")+">"+inline(c)+"</td>";});
        html+="</tr>"; i++;
      }
      out.push(html+"</tbody></table>");
    }

    while(i<lines.length){
      var line=lines[i];
      if(line.trim()===""){i++;continue;}
      var cb=line.match(/^\u0000(\d+)\u0000$/);
      if(cb){var b=blocks[+cb[1]];
        if((b.lang||"").toLowerCase()==="mermaid"){
          out.push('<div class="mermaid" data-src="'+escapeHtml(b.code).replace(/"/g,"&quot;")+'">'+escapeHtml(b.code)+'</div>');
        } else {
          out.push('<pre>'+(b.lang?'<span class="lang-tag">'+escapeHtml(b.lang.split(":").pop())+'</span>':"")+
                   '<code>'+escapeHtml(b.code)+'</code></pre>');
        }
        i++; continue;}
      // raw HTML block
      if(/^<(\/?)([a-zA-Z][\w-]*)(\s|>|\/)/.test(line)){
        var buf=[]; while(i<lines.length && lines[i].trim()!==""){buf.push(lines[i]);i++;}
        out.push(buf.join("\n")); continue;
      }
      var h=line.match(/^(#{1,6})\s+(.*?)\s*#*$/);
      if(h){var lvl=h[1].length, txt=inline(h[2]), id=uid(slugify(h[2]));
        if(lvl>=2&&lvl<=3) toc.push({lvl:lvl,text:h[2].replace(/[#*`]/g,"").trim(),id:id});
        var a=(lvl===2||lvl===3)?'<a class="anchor" href="#'+id+'">#</a>':"";
        out.push("<h"+lvl+' id="'+id+'">'+txt+a+"</h"+lvl+">"); i++; continue;}
      if(/^(\s*)(-{3,}|\*{3,}|_{3,})\s*$/.test(line) && line.indexOf("|")<0){out.push("<hr>");i++;continue;}
      if(/^\s*>/.test(line)){
        var q=[]; while(i<lines.length && /^\s*>/.test(lines[i])){q.push(lines[i].replace(/^\s*>\s?/,""));i++;}
        out.push("<blockquote>"+parse(q.join("\n"),toc)+"</blockquote>"); continue;
      }
      if(line.indexOf("|")>-1 && i+1<lines.length && /^\s*\|?[\s:]*-{2,}/.test(lines[i+1]) && lines[i+1].indexOf("|")>-1){
        tableBlock(); continue;
      }
      if(/^(\s*)([-*+]|\d+\.)\s+/.test(line)){ listBlock(); continue; }
      // paragraph
      var p=[]; while(i<lines.length && lines[i].trim()!=="" &&
            !/^\u0000\d+\u0000$/.test(lines[i]) && !/^#{1,6}\s/.test(lines[i]) &&
            !/^\s*>/.test(lines[i]) && !/^(\s*)([-*+]|\d+\.)\s+/.test(lines[i]) &&
            !/^<(\/?)([a-zA-Z][\w-]*)(\s|>|\/)/.test(lines[i]) &&
            !/^(\s*)(-{3,}|\*{3,}|_{3,})\s*$/.test(lines[i])){p.push(lines[i]);i++;}
      if(p.length) out.push("<p>"+inline(p.join(" "))+"</p>");
    }
    return out.join("\n");
  }
  function mdToHtml(md){var toc=[];var html=parse(md,toc);return {html:html,toc:toc};}

  // =====================================================================
  // Path helpers
  // =====================================================================
  function dirname(p){var i=p.lastIndexOf("/");return i<0?"":p.slice(0,i);}
  function resolvePath(base,rel){
    if(/^([a-z]+:)?\/\//i.test(rel)||rel[0]==="#"||rel.indexOf("mailto:")===0) return rel;
    var dir=dirname(base).split("/").filter(Boolean);
    rel.split("/").forEach(function(seg){
      if(seg===".."){dir.pop();} else if(seg==="."||seg===""){} else {dir.push(seg);}
    });
    return dir.join("/");
  }

  // =====================================================================
  // Sidebar tree
  // =====================================================================
  function buildTree(){
    var groups={};
    ORDER.forEach(function(p){
      var parts=p.split("/");
      var top = parts.length===1 ? "" : parts[0];
      (groups[top]=groups[top]||[]).push(p);
    });
    return groups;
  }
  function renderSidebar(){
    var nav=document.getElementById("nav"); nav.innerHTML="";
    var groups=buildTree();
    var topOrder=["","specs","examples","guides","templates",".github"];
    var seen={}, idx=0;
    topOrder.concat(Object.keys(groups)).forEach(function(g){
      if(seen[g]||!groups[g]) return; seen[g]=1;
      var meta=FOLDER_META[g]||{icon:"📁",label:g};
      var wrap=document.createElement("div"); wrap.className="nav-group";
      var grp=document.createElement("div"); grp.className="group"; if(g==="templates"||g===".github") grp.classList.add("collapsed");
      var head=document.createElement("div"); head.className="group-head";
      head.innerHTML='<span>'+meta.icon+'</span><span>'+meta.label+'</span><span class="caret">▾</span>';
      var items=document.createElement("div"); items.className="group-items";
      // subfolder grouping for templates (es / pt-br)
      var bySub={};
      groups[g].forEach(function(p){
        var parts=p.split("/");
        var sub = (g!=="" && parts.length>2) ? parts[1] : "";
        (bySub[sub]=bySub[sub]||[]).push(p);
      });
      Object.keys(bySub).forEach(function(sub){
        if(sub){var sf=document.createElement("div");sf.className="subfolder";sf.textContent=sub;items.appendChild(sf);}
        bySub[sub].forEach(function(p){
          var a=document.createElement("div");
          a.className="navlink"+(sub?" nested":"");
          a.setAttribute("data-path",p);
          a.style.animationDelay=(idx*22)+"ms"; idx++;
          a.innerHTML='<span class="ic">'+fileIcon(p)+'</span><span>'+prettyName(p)+'</span>';
          a.addEventListener("click",function(){go(p);closeMobile();});
          items.appendChild(a);
        });
      });
      head.addEventListener("click",function(){grp.classList.toggle("collapsed");
        items.style.maxHeight = grp.classList.contains("collapsed")?"0":items.scrollHeight+"px";});
      grp.appendChild(head); grp.appendChild(items); wrap.appendChild(grp); nav.appendChild(wrap);
      requestAnimationFrame(function(){if(!grp.classList.contains("collapsed")) items.style.maxHeight=items.scrollHeight+"px";});
    });
  }
  function setActive(path){
    document.querySelectorAll(".navlink").forEach(function(n){
      n.classList.toggle("active", n.getAttribute("data-path")===path);
    });
  }

  // =====================================================================
  // Home page
  // =====================================================================
  function homeHtml(){
    var folders={};
    ORDER.forEach(function(p){var t=p.indexOf("/")<0?"root":p.split("/")[0];folders[t]=(folders[t]||0)+1;});
    var C=t("cards");
    var cards=[
      {p:t("readme"),ic:"🏠",h:C.method.h,d:C.method.d},
      {p:"specs/ada-v2-ksa-framework.md",ic:"🧬",h:C.ksa.h,d:C.ksa.d},
      {p:"specs/role-to-credential-mapping.md",ic:"🧭",h:C.role.h,d:C.role.d},
      {p:"specs/skills-map-and-job-matching.md",ic:"🗺️",h:C.map.h,d:C.map.d},
      {p:"specs/genai-authoring-workflow.md",ic:"🤖",h:C.genai.h,d:C.genai.d},
      {p:"examples/skills-map-job-match-frontend.md",ic:"📘",h:C.example.h,d:C.example.d},
      {p:"CLAUDE.md",ic:"⚙️",h:C.agent.h,d:C.agent.d}
    ];
    var html='<div class="hero">'+
      '<span class="badge">'+t("heroBadge")+'</span>'+
      '<h2>'+escapeHtml(t("heroTitle"))+'<br><span class="grad">'+escapeHtml(t("heroGrad"))+'</span></h2>'+
      '<p class="lead">'+escapeHtml(t("heroLead"))+'</p>'+
      '<p style="margin:22px 0"><img src="img/ada-methodology-overview.png" alt="The ADA Methodology: Building Job-Ready Digital Talent" style="max-width:100%;border-radius:14px;border:1px solid var(--border);box-shadow:var(--shadow)"></p>'+
      '<div class="stats">'+
        '<div class="stat"><div class="num">'+ORDER.length+'</div><div class="lbl">'+t("stDocs")+'</div></div>'+
        '<div class="stat"><div class="num">'+(folders["specs"]||0)+'</div><div class="lbl">'+t("stSpecs")+'</div></div>'+
        '<div class="stat"><div class="num">'+(folders["examples"]||0)+'</div><div class="lbl">'+t("stExamples")+'</div></div>'+
        '<div class="stat"><div class="num">'+(folders["templates"]||0)+'</div><div class="lbl">'+t("stTemplates")+'</div></div>'+
        '<div class="stat"><div class="num">3</div><div class="lbl">'+t("stLangs")+'</div></div>'+
      '</div>'+
      '<div class="pipeline">'+
        '<span class="pnode">'+t("pPosting")+'</span><span class="parrow">→</span>'+
        '<span class="pnode">'+t("pProfile")+'</span><span class="parrow">→</span>'+
        '<span class="pnode">'+t("pMap")+'</span><span class="parrow">→</span>'+
        '<span class="pnode">'+t("pMC")+'</span><span class="parrow">→</span>'+
        '<span class="pnode gold">'+t("pReady")+'</span>'+
      '</div>'+
      '<h3 style="margin-top:30px">'+escapeHtml(t("jumpIn"))+'</h3>'+
      '<div class="cards">';
    cards.forEach(function(c){ if(!DOCS[c.p]) return;
      html+='<div class="card" data-go="'+c.p+'"><div class="ic">'+c.ic+'</div><h3>'+c.h+'</h3><p>'+c.d+'</p></div>';
    });
    html+='</div></div>';
    return html;
  }

  // =====================================================================
  // Mermaid diagrams (loaded on demand from CDN; graceful offline fallback)
  // =====================================================================
  function mermaidTheme(){return document.documentElement.getAttribute("data-theme")==="light"?"default":"dark";}
  // Pin an exact version: floating "@11" can pull a patch with a mindmap regression.
  var MERMAID_SRCS=[
    "https://cdn.jsdelivr.net/npm/mermaid@11.15.0/dist/mermaid.min.js",
    "https://unpkg.com/mermaid@11.15.0/dist/mermaid.min.js"
  ];
  var _mmLoading=null;
  function loadScript(i){
    return new Promise(function(res,rej){
      if(i>=MERMAID_SRCS.length){rej();return;}
      var s=document.createElement("script");
      s.src=MERMAID_SRCS[i];
      s.onload=function(){ window.mermaid?res(window.mermaid):loadScript(i+1).then(res,rej); };
      s.onerror=function(){ loadScript(i+1).then(res,rej); };
      document.head.appendChild(s);
    });
  }
  function ensureMermaid(){
    if(window.mermaid) return Promise.resolve(window.mermaid);
    if(_mmLoading) return _mmLoading;
    _mmLoading=loadScript(0);
    return _mmLoading;
  }
  // The diagram source is the single source of truth (stored in data-src). We never
  // re-parse a node's live DOM, because after a successful render it holds SVG, not source.
  function diagramSrc(n){
    var s=n.getAttribute("data-src");
    if(s===null){ s=n.textContent; n.setAttribute("data-src", s); }
    return s;
  }
  function mermaidFallback(nodes){
    nodes.forEach(function(n){
      if(n.querySelector("svg"))return;
      n.setAttribute("data-fb","1"); n.classList.add("fallback");
      n.innerHTML='<pre><span class="lang-tag">mermaid</span><code>'+escapeHtml(diagramSrc(n))+'</code></pre>'+
        '<div style="font-size:11px;color:var(--text-faint);margin-top:6px">⚠️ Diagram source shown — Mermaid could not be loaded.</div>';
    });
  }
  // ----- pan + zoom for a diagram canvas (drag to pan, ctrl/cmd+wheel to zoom) -----
  function attachZoom(canvas, svg, onZoom){
    var st={s:1,x:0,y:0}, drag=null, MIN=0.4, MAX=5;
    function apply(){ if(svg){svg.style.transform="translate("+st.x+"px,"+st.y+"px) scale("+st.s+")";}
      if(onZoom) onZoom(Math.round(st.s*100)); }
    function zoomTo(ns){ st.s=Math.min(MAX,Math.max(MIN,ns)); apply(); }
    canvas.addEventListener("wheel",function(e){
      if(!(e.ctrlKey||e.metaKey)) return;            // plain scroll keeps scrolling the page
      e.preventDefault(); zoomTo(st.s*(e.deltaY<0?1.12:0.892)); },{passive:false});
    canvas.addEventListener("pointerdown",function(e){
      drag={px:e.clientX,py:e.clientY,ox:st.x,oy:st.y};
      canvas.classList.add("grabbing","dragging");
      try{canvas.setPointerCapture(e.pointerId);}catch(_){} });
    canvas.addEventListener("pointermove",function(e){ if(!drag)return;
      st.x=drag.ox+(e.clientX-drag.px); st.y=drag.oy+(e.clientY-drag.py); apply(); });
    function end(){ drag=null; canvas.classList.remove("grabbing","dragging"); }
    canvas.addEventListener("pointerup",end);
    canvas.addEventListener("pointercancel",end);
    canvas.addEventListener("dblclick",function(){ st={s:1,x:0,y:0}; apply(); });
    apply();
    return { zin:function(){zoomTo(st.s*1.25);}, zout:function(){zoomTo(st.s*0.8);},
             reset:function(){st={s:1,x:0,y:0};apply();} };
  }
  // ----- single fullscreen modal reused by every diagram -----
  var _dModal=null;
  function diagramModal(){
    if(_dModal) return _dModal;
    var wrap=document.createElement("div"); wrap.className="dmodal";
    wrap.innerHTML='<div class="dm-bar"><span class="dm-hint">Drag to pan \u00B7 Ctrl/\u2318 + scroll to zoom \u00B7 double-click to reset</span>'+
      '<button class="dbtn" data-a="out" title="Zoom out">\u2212</button>'+
      '<button class="dbtn" data-a="reset" title="Reset">\u21BA</button>'+
      '<button class="dbtn" data-a="in" title="Zoom in">+</button>'+
      '<button class="dbtn" data-a="close" title="Close (Esc)">\u2715</button></div>'+
      '<div class="dm-stage"></div>';
    document.body.appendChild(wrap);
    var stage=wrap.querySelector(".dm-stage"), ctl=null;
    function close(){ wrap.classList.remove("open"); stage.innerHTML=""; ctl=null; }
    wrap.addEventListener("click",function(e){ if(e.target===wrap) close(); });
    wrap.querySelectorAll(".dm-bar .dbtn").forEach(function(b){ b.addEventListener("click",function(){
      var a=b.getAttribute("data-a");
      if(a==="close") return close();
      if(!ctl) return;
      if(a==="in")ctl.zin(); else if(a==="out")ctl.zout(); else ctl.reset();
    });});
    document.addEventListener("keydown",function(e){
      if(e.key==="Escape"&&wrap.classList.contains("open")) close(); });
    _dModal={ open:function(svgString){ stage.innerHTML=svgString;
        var svg=stage.querySelector("svg");
        if(svg){svg.removeAttribute("width");svg.removeAttribute("height");svg.style.maxWidth="94vw";svg.style.maxHeight="82vh";}
        wrap.classList.add("open"); ctl=attachZoom(stage,svg); } };
    return _dModal;
  }
  function flashBtn(b){ b.classList.add("ok"); setTimeout(function(){b.classList.remove("ok");},1100); }
  function copyText(s){
    try{ if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(s);return;} }catch(e){}
    var ta=document.createElement("textarea"); ta.value=s; ta.style.position="fixed"; ta.style.opacity="0";
    document.body.appendChild(ta); ta.focus(); ta.select();
    try{document.execCommand("copy");}catch(e){} document.body.removeChild(ta);
  }
  function downloadSvg(svgString){
    var blob=new Blob(['<?xml version="1.0" encoding="UTF-8"?>\n'+svgString],{type:"image/svg+xml"});
    var url=URL.createObjectURL(blob), a=document.createElement("a");
    a.href=url; a.download=(currentPath?currentPath.replace(/[\\/.]/g,"-"):"ada")+"-diagram.svg";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function(){URL.revokeObjectURL(url);},1500);
  }
  // ----- turn a rendered SVG into an interactive figure (toolbar + pan/zoom) -----
  function enhanceDiagram(n, svgString, bind){
    n.classList.remove("fallback"); n.removeAttribute("data-fb"); n.setAttribute("data-processed","1");
    n.innerHTML='<div class="diagram">'+
        '<div class="diagram-toolbar">'+
          '<button class="dbtn" data-a="out" title="Zoom out">\u2212</button>'+
          '<button class="dbtn" data-a="reset" title="Reset view">\u21BA</button>'+
          '<button class="dbtn" data-a="in" title="Zoom in">+</button>'+
          '<button class="dbtn" data-a="full" title="Fullscreen">\u26F6</button>'+
          '<button class="dbtn" data-a="copy" title="Copy diagram source">\u29C9</button>'+
          '<button class="dbtn" data-a="dl" title="Download SVG">\u2913</button>'+
        '</div>'+
        '<div class="dzlabel">100%</div>'+
        '<div class="diagram-canvas"></div>'+
      '</div>';
    var canvas=n.querySelector(".diagram-canvas");
    canvas.innerHTML=svgString;
    var svg=canvas.querySelector("svg");
    if(svg){ svg.removeAttribute("width"); svg.removeAttribute("height");
      svg.style.maxWidth="100%"; svg.style.height="auto"; }
    if(bind) try{ bind(canvas); }catch(e){}
    var label=n.querySelector(".dzlabel");
    var ctl=attachZoom(canvas, svg, function(p){ if(label) label.textContent=p+"%"; });
    n.querySelectorAll(".diagram-toolbar .dbtn").forEach(function(b){
      b.addEventListener("click",function(ev){ ev.stopPropagation();
        var a=b.getAttribute("data-a");
        if(a==="in")ctl.zin();
        else if(a==="out")ctl.zout();
        else if(a==="reset")ctl.reset();
        else if(a==="full")diagramModal().open(svgString);
        else if(a==="copy"){ copyText(diagramSrc(n)); flashBtn(b); }
        else if(a==="dl") downloadSvg(svgString);
      });
    });
  }
  var _mmSeq=0;
  // ---- find the root node(s) of a flowchart: declared but never an edge target ----
  function detectRoots(src){
    try{
      var lines=src.split(/\r?\n/);
      if(!/^\s*(flowchart|graph)\b/i.test(lines[0]||"")) return [];
      var all={}, targets={};
      for(var i=1;i<lines.length;i++){
        var ln=lines[i], tt=(ln||"").trim();
        if(!tt||/^%%/.test(tt)) continue;
        if(/^(classdef|class|style|linkstyle|click|direction|subgraph|end)\b/i.test(tt)) continue;
        var s=ln;
        for(var k=0;k<8;k++){
          s=s.replace(/\(\([^()]*\)\)/g," ").replace(/\[\[[^\[\]]*\]\]/g," ")
             .replace(/\[\([^\[\]]*\)\]/g," ").replace(/\(\[[^\[\]]*\]\)/g," ")
             .replace(/\[[^\[\]]*\]/g," ").replace(/\{[^{}]*\}/g," ").replace(/\([^()]*\)/g," ");
        }
        s=s.replace(/\|[^|]*\|/g," ");                 // inline edge labels |..|
        if(s.indexOf("--")<0 && s.indexOf("==")<0) continue;
        var ids=s.split(/\s*(?:-{2,}>?|={2,}>?|-\.->?|<-{2,})\s*/)
                 .map(function(x){return (x.trim().match(/^[A-Za-z0-9_]+/)||[""])[0];})
                 .filter(Boolean);
        for(var j=0;j<ids.length;j++){ all[ids[j]]=1; if(j>0) targets[ids[j]]=1; }
      }
      var roots=Object.keys(all).filter(function(id){return !targets[id];});
      return roots.length && roots.length<=4 ? roots : [];
    }catch(e){ return []; }
  }
  function withRootEmphasis(src){
    var roots=detectRoots(src);
    if(!roots.length) return src;
    return src+"\n"+
      "classDef adaRootNode fill:#1E2A6E,stroke:#E0A53C,stroke-width:3.5px,color:#ffffff,font-weight:bold,font-size:22px;\n"+
      "class "+roots.join(",")+" adaRootNode;";
  }
  function renderDiagrams(){
    var nodes=Array.prototype.slice.call(content.querySelectorAll(".mermaid"));
    if(!nodes.length) return;
    nodes.forEach(diagramSrc); // capture source before anything mutates the DOM
    var light=document.documentElement.getAttribute("data-theme")==="light";
    var INK="#0A1124", INDIGO="#1E2A6E", TURQ="#15B5C6", GOLD="#E0A53C";
    ensureMermaid().then(function(m){
      m.initialize({startOnLoad:false,securityLevel:"loose",fontFamily:"inherit",theme:"base",
        fontSize:"17px",
        flowchart:{htmlLabels:true,useMaxWidth:true,curve:"basis",padding:14,nodeSpacing:54,rankSpacing:62},
        themeVariables:{
          fontSize:"17px",
          // nodes: brand indigo fill with white text (high contrast on both themes)
          primaryColor:INDIGO, primaryTextColor:"#ffffff", primaryBorderColor:TURQ,
          mainBkg:INDIGO, nodeBorder:TURQ, nodeTextColor:"#ffffff",
          lineColor: light?INDIGO:TURQ,
          secondaryColor: light?"#eef2fb":"#1a2548", secondaryTextColor: light?INK:"#ffffff", secondaryBorderColor:TURQ,
          tertiaryColor: light?"#f3f6fc":"#121c3a", tertiaryTextColor: light?INDIGO:"#e9edfb", tertiaryBorderColor: light?"#cfd8ee":"#2a3566",
          background: light?"#ffffff":INK,
          textColor: light?INDIGO:"#e9edfb",
          clusterBkg: light?"#eef2fb":"#121c3a", clusterBorder:TURQ,
          titleColor: light?INDIGO:"#e9edfb", edgeLabelBackground: light?"#ffffff":"#121c3a",
          // mindmap / pie section palette — brand colors with readable labels
          cScale0:INDIGO, cScale1:TURQ, cScale2:GOLD, cScale3:"#2a3aa0", cScale4:"#0e8d9b", cScale5:INDIGO,
          cScaleLabel0:"#ffffff", cScaleLabel1:INK, cScaleLabel2:INK, cScaleLabel3:"#ffffff", cScaleLabel4:"#ffffff", cScaleLabel5:"#ffffff"
        }});
      nodes.forEach(function(n){
        var src=withRootEmphasis(diagramSrc(n));
        var id="mmd-"+(Date.now())+"-"+(_mmSeq++);
        try{
          m.render(id, src).then(function(out){
            enhanceDiagram(n, out.svg, out.bindFunctions);
          }).catch(function(){ mermaidFallback([n]); });
        }catch(e){ mermaidFallback([n]); }
      });
    }).catch(function(){mermaidFallback(nodes);});
  }

  // =====================================================================
  // Render / routing
  // =====================================================================
  var content=document.getElementById("content");
  var toc=document.getElementById("toc");
  var crumbs=document.getElementById("crumbs");
  var currentPath="";

  function go(path,anchor){
    location.hash = "#/"+path + (anchor?("#"+anchor):"");
  }
  function render(path,anchor){
    currentPath=path; window.__anchor=anchor;
    content.classList.remove("swap"); void content.offsetWidth; content.classList.add("swap");
    if(path==="__home__"||!path){
      crumbs.innerHTML="";
      content.innerHTML=homeHtml();
      toc.innerHTML="";
      setActive("");
      bindCards();
      bindImages();
      renderDiagrams();
      window.scrollTo(0,0);
      return;
    }
    if(!DOCS[path]){
      content.innerHTML='<div class="empty"><h2>404</h2><p>No document at <code>'+escapeHtml(path)+'</code></p></div>';
      toc.innerHTML=""; return;
    }
    var res=mdToHtml(DOCS[path]);
    crumbs.innerHTML = path.split("/").map(function(s,idx,arr){
      return idx===arr.length-1?'<span>'+s+'</span>':s;
    }).join(" / ");
    content.innerHTML='<div class="md">'+res.html+'</div>';
    // TOC
    if(res.toc.length>1){
      toc.innerHTML='<div class="toc-title">'+escapeHtml(t("onThisPage"))+'</div>'+res.toc.map(function(item){
        return '<a href="#'+item.id+'" class="'+(item.lvl===3?"lvl3":"")+'" data-id="'+item.id+'">'+escapeHtml(item.text)+'</a>';
      }).join("");
    } else { toc.innerHTML=""; }
    setActive(path);
    bindImages();
    bindContentLinks();
    bindTocLinks();
    renderDiagrams();
    if(anchor){var el=document.getElementById(anchor); if(el) setTimeout(function(){el.scrollIntoView();},50);}
    else window.scrollTo(0,0);
  }

  function bindCards(){
    content.querySelectorAll(".card[data-go]").forEach(function(c){
      c.addEventListener("click",function(){go(c.getAttribute("data-go"));});
    });
  }
  function bindImages(){
    content.querySelectorAll("img[src]").forEach(function(im){
      var src=im.getAttribute("src");
      if(!src||/^([a-z]+:)?\/\//i.test(src)||src.indexOf("data:")===0) return;
      im.setAttribute("src", resolvePath(currentPath, src));
      im.setAttribute("loading","lazy");
    });
  }
  function bindContentLinks(){
    content.querySelectorAll("a[href]").forEach(function(a){
      var href=a.getAttribute("href");
      if(/^([a-z]+:)?\/\//i.test(href)||href.indexOf("mailto:")===0){a.target="_blank";a.rel="noopener";return;}
      if(href[0]==="#"){a.addEventListener("click",function(e){e.preventDefault();
        var el=document.getElementById(href.slice(1)); if(el)el.scrollIntoView({behavior:"smooth"});});return;}
      var parts=href.split("#"); var target=resolvePath(currentPath,parts[0]); var anc=parts[1];
      a.addEventListener("click",function(e){
        e.preventDefault();
        if(DOCS[target]) go(target,anc);
        else if(/\.md$/i.test(parts[0])===false){ /* maybe folder link */ }
        else go(target,anc);
      });
    });
  }
  function bindTocLinks(){
    toc.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click",function(e){e.preventDefault();
        var el=document.getElementById(a.getAttribute("data-id"));
        if(el)el.scrollIntoView({behavior:"smooth"});});
    });
  }

  function route(){
    var h=location.hash;
    if(!h||h==="#"||h==="#/"){render("__home__");return;}
    h=h.replace(/^#\//,"");
    var parts=h.split("#"); // path # anchor
    render(parts[0]||"__home__", parts[1]);
  }
  window.addEventListener("hashchange",route);

  // =====================================================================
  // Search
  // =====================================================================
  var searchInput=document.getElementById("search");
  searchInput.addEventListener("input",function(){
    var q=this.value.trim().toLowerCase();
    if(!q){renderSidebar();afterSidebar();return;}
    var matches=ORDER.filter(function(p){
      return p.toLowerCase().indexOf(q)>-1 || prettyName(p).toLowerCase().indexOf(q)>-1 ||
             DOCS[p].toLowerCase().indexOf(q)>-1;
    });
    var nav=document.getElementById("nav");
    nav.innerHTML='<div class="group-head" style="cursor:default">🔎 '+matches.length+' '+(matches.length===1?t("result"):t("results"))+'</div>';
    matches.forEach(function(p,idx){
      var a=document.createElement("div");a.className="navlink";a.setAttribute("data-path",p);
      a.style.animationDelay=(idx*18)+"ms";
      var hit="";
      var ci=DOCS[p].toLowerCase().indexOf(q);
      if(ci>-1){var snip=DOCS[p].slice(Math.max(0,ci-20),ci+40).replace(/\n/g," ");
        hit='<div style="font-size:11px;color:var(--text-faint);margin-top:2px">…'+escapeHtml(snip)+'…</div>';}
      a.innerHTML='<span class="ic">'+fileIcon(p)+'</span><span>'+prettyName(p)+hit+'</span>';
      a.addEventListener("click",function(){go(p);closeMobile();});
      nav.appendChild(a);
    });
    if(!matches.length) nav.innerHTML+='<div class="empty" style="padding:30px 10px;font-size:13px">'+escapeHtml(t("noMatches"))+'</div>';
    setActive(currentPath);
  });
  document.addEventListener("keydown",function(e){
    if(e.key==="/"&&document.activeElement!==searchInput){e.preventDefault();searchInput.focus();}
    if(e.key==="Escape"){searchInput.value="";searchInput.blur();renderSidebar();afterSidebar();}
  });

  // =====================================================================
  // Theme
  // =====================================================================
  var themeBtn=document.getElementById("theme");
  function applyTheme(t){document.documentElement.setAttribute("data-theme",t);
    themeBtn.textContent=t==="light"?"🌙":"☀️"; try{localStorage.setItem("ada-theme",t);}catch(e){}}
  themeBtn.addEventListener("click",function(){
    applyTheme(document.documentElement.getAttribute("data-theme")==="light"?"dark":"light");
    if(content.querySelector(".mermaid")) render(currentPath, window.__anchor);});
  var saved; try{saved=localStorage.getItem("ada-theme");}catch(e){}
  applyTheme(saved|| (window.matchMedia&&window.matchMedia("(prefers-color-scheme: light)").matches?"light":"dark"));

  // =====================================================================
  // Language switcher (i18n)
  // =====================================================================
  var langSel=document.getElementById("lang");
  function setLangStatic(lang){
    if(!I18N[lang]) lang="en";
    LANG=lang;
    document.documentElement.setAttribute("lang", lang==="pt"?"pt-br":lang);
    var sub=document.querySelector('[data-i18n="subtitle"]'); if(sub) sub.textContent=t("subtitle");
    if(searchInput) searchInput.placeholder=t("search");
    if(langSel&&langSel.value!==lang) langSel.value=lang;
    try{localStorage.setItem("ada-lang",lang);}catch(e){}
  }
  function applyLang(lang){ setLangStatic(lang); render(currentPath, window.__anchor); }
  if(langSel) langSel.addEventListener("change",function(){applyLang(this.value);});
  var savedLang; try{savedLang=localStorage.getItem("ada-lang");}catch(e){}
  if(!savedLang){ var nl=((navigator&&navigator.language)||"en").toLowerCase();
    savedLang= nl.indexOf("es")===0?"es":(nl.indexOf("pt")===0?"pt":"en"); }
  setLangStatic(savedLang);

  // =====================================================================
  // Progress bar, scroll-top, scrollspy
  // =====================================================================
  var bar=document.getElementById("progress"), topBtn=document.getElementById("top");
  window.addEventListener("scroll",function(){
    var st=document.documentElement.scrollTop||document.body.scrollTop;
    var h=(document.documentElement.scrollHeight-document.documentElement.clientHeight)||1;
    bar.style.width=(st/h*100)+"%";
    topBtn.classList.toggle("show",st>400);
    // scrollspy
    var links=toc.querySelectorAll("a"); var cur=null;
    links.forEach(function(a){var el=document.getElementById(a.getAttribute("data-id"));
      if(el&&el.getBoundingClientRect().top<140)cur=a;});
    links.forEach(function(a){a.classList.toggle("active",a===cur);});
  },{passive:true});
  topBtn.addEventListener("click",function(){window.scrollTo({top:0,behavior:"smooth"});});

  // mobile
  var sidebar=document.getElementById("sidebar"), overlay=document.getElementById("overlay");
  document.getElementById("menuBtn").addEventListener("click",function(){
    sidebar.classList.toggle("open");overlay.classList.toggle("show");});
  function closeMobile(){sidebar.classList.remove("open");overlay.classList.remove("show");}
  overlay.addEventListener("click",closeMobile);
  document.getElementById("homeLink").addEventListener("click",function(){go("__home__");});

  function afterSidebar(){setActive(currentPath);}

  // init
  renderSidebar();
  route();
})();
"""

def build():
    md_files = sorted(find_md(), key=sort_key)
    embeds = []
    for rel in md_files:
        with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as f:
            content = f.read()
        # guard against breaking out of the script tag (none expected)
        content = content.replace("</script", "<\\/script")
        embeds.append('<script type="text/markdown" data-path="%s">%s</script>' % (rel, content))
    embeds_html = "\n".join(embeds)

    page = (
        "<!doctype html>\n"
        '<html lang="en" data-theme="dark">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>ADA Methodology · Docs Browser</title>\n"
        '<meta name="description" content="Interactive browser for the ADA Methodology repository.">\n'
        '<meta name="theme-color" content="#0A1124">\n'
        '<link rel="icon" type="image/png" href="img/Isotipo.png">\n'
        "<style>\n" + CSS + "\n</style>\n</head>\n<body>\n"
        '<div id="progress"></div>\n'
        "<header>\n"
        '  <button class="iconbtn" id="menuBtn" aria-label="Menu">☰</button>\n'
        '  <div class="brand" id="homeLink" style="cursor:pointer">\n'
        '    <img class="iso-spin" src="img/Isotipo.png" alt="ADA" title="ADA Methodology — home">\n'
        '    <div><h1>ADA Methodology</h1><small data-i18n="subtitle">Applied Digital Apprenticeship</small></div>\n'
        "  </div>\n"
        '  <div class="spacer"></div>\n'
        '  <div class="search">\n'
        '    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>\n'
        '    <input id="search" type="text" placeholder="Search docs…  ( / )" autocomplete="off">\n'
        "  </div>\n"
        '  <select id="lang" class="langsel" aria-label="Language">\n'
        '    <option value="en">\U0001F1EC\U0001F1E7 EN</option>\n'
        '    <option value="es">\U0001F1EA\U0001F1F8 ES</option>\n'
        '    <option value="pt">\U0001F1E7\U0001F1F7 PT</option>\n'
        "  </select>\n"
        '  <button class="iconbtn" id="theme" aria-label="Toggle theme">☀️</button>\n'
        "</header>\n"
        '<div class="overlay" id="overlay"></div>\n'
        '<div class="layout">\n'
        '  <aside id="sidebar"><div id="nav"></div></aside>\n'
        '  <main><div class="crumbs" id="crumbs"></div><div id="content"></div></main>\n'
        '  <aside id="toc"></aside>\n'
        "</div>\n"
        '<button id="top" aria-label="Scroll to top">↑</button>\n\n'
        "<!-- ===== Embedded Markdown content ===== -->\n"
        + embeds_html + "\n\n"
        "<script>\n" + JS + "\n</script>\n"
        "</body>\n</html>\n"
    )

    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print("Wrote %s (%d docs, %.0f KB)" % (out, len(md_files), len(page) / 1024))

if __name__ == "__main__":
    build()
