#!/usr/bin/env python3
"""Extrahiert den Bestandsinhalt jeder Seite als Inventar (verbatim).

Aufruf:  python3 _design/tools/extract_content.py
Ausgabe: _design/inventar/<seite>.md

Zweck: Der Redesign-Umbau darf keinen Text verlieren. Diese Datei ist die
Quelle der Wahrheit fuer den Text; das Markup wird neu gebaut, der Text
wird von hier uebernommen.
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "_design", "inventar")

PAGES = [
    ("index.html", "startseite"),
    ("bauberatung/index.html", "bauberatung"),
    ("baubetreuung/index.html", "baubetreuung"),
    ("bauprojektmanagement/index.html", "bauprojektmanagement"),
    ("denkmalsanierung/index.html", "denkmalsanierung"),
    ("ueber-juergen/index.html", "ueber-juergen"),
    ("kontakt/index.html", "kontakt"),
    ("impressum/index.html", "impressum"),
    ("datenschutz/index.html", "datenschutz"),
    ("agb/index.html", "agb"),
    ("bauabnahme/index.html", "bauabnahme-VERWAIST"),
    ("404.html", "404"),
]

SKIP = {"script", "style", "noscript", "svg", "head"}
BLOCK = {
    "p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "div", "section", "footer",
    "header", "nav", "summary", "details", "blockquote", "figcaption", "td",
    "th", "tr", "address", "label", "button", "a", "span", "figure", "article",
    "main", "ul", "ol", "dl", "dt", "dd", "table", "form", "br", "img", "hr",
}
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}


class Outline(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.skip = 0
        self.rows = []          # (kind, depth, text)
        self.buf = []
        self.in_body = False
        self.stack = []
        self.in_heading = 0

    # -- helpers -------------------------------------------------------
    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        return t

    def emit_text(self):
        t = self.flush()
        if t:
            self.rows.append(("text", self.depth, t))

    # -- parser hooks --------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "body":
            self.in_body = True
            return
        if not self.in_body:
            return
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in BLOCK and not self.in_heading:
            self.emit_text()
        elif tag == "br" and self.in_heading:
            self.buf.append(" ")
        if tag == "img":
            src = a.get("src", "?")
            if src.startswith("data:"):
                src = "[BASE64 INLINE, %.0f KB — im Redesign als Datei ausliefern]" % (
                    len(src) / 1024)
            self.rows.append((
                "img", self.depth,
                "src=%s | alt=%s | %sx%s | loading=%s" % (
                    src, a.get("alt", "!!! FEHLT !!!"),
                    a.get("width", "?"), a.get("height", "?"),
                    a.get("loading", "-"))))
            return
        if tag in HEADINGS:
            self.emit_text()
            self.in_heading += 1
            self.stack.append(tag)
        if tag in ("section", "footer", "header", "nav", "main", "form", "details"):
            cls = a.get("class") or a.get("id") or ""
            self.rows.append(("open", self.depth, "<%s%s>" % (tag, (" ." + cls) if cls else "")))
            self.depth += 1
        if tag == "a":
            self.stack.append("a:" + (a.get("href") or ""))

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_body = False
            return
        if not self.in_body:
            return
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in HEADINGS:
            self.in_heading = max(0, self.in_heading - 1)
        t = self.flush() if (tag in HEADINGS or not self.in_heading) else ""
        if tag in HEADINGS:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            if t:
                self.rows.append((tag, self.depth, t))
            return
        if tag == "a":
            href = ""
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i].startswith("a:"):
                    href = self.stack.pop(i)[2:]
                    break
            if t:
                self.rows.append(("link", self.depth, "%s  ->  %s" % (t, href)))
            return
        if t:
            self.rows.append(("text", self.depth, t))
        if tag in ("section", "footer", "header", "nav", "main", "form", "details"):
            self.depth = max(0, self.depth - 1)
            self.rows.append(("close", self.depth, "</%s>" % tag))

    def handle_data(self, data):
        if self.in_body and not self.skip:
            self.buf.append(data)


def head_facts(src):
    out = {}
    m = re.search(r"<title>(.*?)</title>", src, re.S)
    out["title"] = html.unescape(m.group(1).strip()) if m else "!!! FEHLT !!!"
    for name, key in (("description", "description"), ("robots", "robots")):
        m = re.search(r'<meta\s+name="%s"\s+content="(.*?)"' % name, src, re.S)
        out[key] = html.unescape(m.group(1)) if m else "!!! FEHLT !!!"
    m = re.search(r'<link\s+rel="canonical"\s+href="(.*?)"', src)
    out["canonical"] = m.group(1) if m else "!!! FEHLT !!!"
    for prop in ("og:title", "og:description", "og:url", "og:image"):
        m = re.search(r'<meta\s+property="%s"\s+content="(.*?)"' % prop, src, re.S)
        out[prop] = html.unescape(m.group(1)) if m else "!!! FEHLT !!!"
    types = []
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
        try:
            data = json.loads(m.group(1))
        except Exception:
            types.append("!!! JSON-LD UNGUELTIG !!!")
            continue
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
        for n in nodes:
            if isinstance(n, dict) and n.get("@type"):
                types.append(str(n["@type"]))
    out["jsonld"] = types
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    for path, slug in PAGES:
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            print("fehlt:", path)
            continue
        src = open(full, encoding="utf-8").read()
        facts = head_facts(src)
        p = Outline()
        p.feed(src)

        lines = ["# Inhaltsinventar — %s" % path, "",
                 "Automatisch erzeugt. **Der Text hier ist verbindlich und wird 1:1 uebernommen.**",
                 "", "## Kopfdaten (unveraendert uebernehmen)", ""]
        for k in ("title", "description", "canonical", "robots",
                  "og:title", "og:description", "og:url", "og:image"):
            lines.append("- **%s:** %s" % (k, facts[k]))
        lines.append("- **JSON-LD Typen:** %s" % (", ".join(facts["jsonld"]) or "keine"))
        lines += ["", "## Gliederung und Text", "", "```"]
        for kind, depth, text in p.rows:
            pad = "  " * depth
            if kind in HEADINGS:
                lines.append("%s%s  %s" % (pad, kind.upper(), text))
            elif kind == "img":
                lines.append("%sIMG   %s" % (pad, text))
            elif kind == "link":
                lines.append("%slink  %s" % (pad, text))
            elif kind in ("open", "close"):
                lines.append("%s%s" % (pad, text))
            else:
                lines.append("%s      %s" % (pad, text))
        lines.append("```")

        dest = os.path.join(OUT, slug + ".md")
        open(dest, "w", encoding="utf-8").write("\n".join(lines) + "\n")
        hs = [r for r in p.rows if r[0] in HEADINGS]
        print("%-34s %5d Zeilen, %2d Ueberschriften (h1: %d)" % (
            slug, len(p.rows), len(hs), sum(1 for r in hs if r[0] == "h1")))


if __name__ == "__main__":
    sys.exit(main())
