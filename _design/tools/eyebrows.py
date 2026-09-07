#!/usr/bin/env python3
"""Erzeugt _design/eyebrows.md — die Abarbeitungsliste der Versalzeilen.

REDESIGN §3 streicht jede kleine Versalzeile ueber einer Ueberschrift.
Im Bestand heisst sie .section-eyebrow / .svc-hero-eyebrow / .eyebrow.

Aufruf:  python3 _design/tools/eyebrows.py
"""
import html
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SEITEN = [
    "index.html", "bauberatung/index.html", "baubetreuung/index.html",
    "bauprojektmanagement/index.html", "denkmalsanierung/index.html",
    "ueber-juergen/index.html", "kontakt/index.html", "impressum/index.html",
    "datenschutz/index.html", "agb/index.html", "bauabnahme/index.html",
]

MUSTER = re.compile(
    r'<[^>]*class="[^"]*(?:section-eyebrow|svc-hero-eyebrow|\beyebrow\b)[^"]*"[^>]*>(.*?)</\w+>',
    re.S)

KOPF = """# Abarbeitungsliste: Versalzeilen ueber Ueberschriften

REDESIGN §3: **Ueber einer Ueberschrift steht nie eine zweite, kleinere Ueberschrift.**
Die Klassen `.section-eyebrow`, `.svc-hero-eyebrow` und `.eyebrow` verschwinden
restlos, ebenso die Farbe `#4A5D3C`.

Erzeugt mit `python3 _design/tools/eyebrows.py`. HTML-Kommentare sind
ausgenommen — abgeschaltete Bloecke werden nicht mitgezaehlt.
Beim Umbau Zeile fuer Zeile abarbeiten; `pruefung.py` meldet, was offen ist.

Die Ziffern sind eine durchgehende Nummerierung von oben nach unten. Wo ein
Abschnitt fachlich Unterpunkte hat (Leistungen der Startseite), darf daraus
`02.1`, `02.2` … werden — siehe `_design/muster.html`.
"""


def text(x):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x)).strip())


def main():
    zeilen, gesamt = [], 0
    for rel in SEITEN:
        pfad = os.path.join(ROOT, rel)
        if not os.path.exists(pfad):
            continue
        src = open(pfad, encoding="utf-8").read()
        # Abgeschaltete Bloecke in HTML-Kommentaren zaehlen nicht mit.
        src = re.sub(r"<!--.*?-->", "", src, flags=re.S)

        treffer = []
        for m in MUSTER.finditer(src):
            eb = text(m.group(1))
            h = re.search(r"<(h[1-6])[^>]*>(.*?)</\1>", src[m.end():m.end() + 1200], re.S)
            treffer.append((eb,
                            h.group(1) if h else "-",
                            text(h.group(2)) if h else "(keine Ueberschrift)"))
        if not treffer:
            continue
        gesamt += len(treffer)
        zeilen.append("\n### `%s` — %d Fundstellen\n" % (rel, len(treffer)))
        zeilen.append("| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |")
        zeilen.append("|---|---|---|---|---|")
        n = 0
        for i, (eb, stufe, ht) in enumerate(treffer, 1):
            if stufe == "h1":
                neu = "**ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`)"
            else:
                n += 1
                neu = "Randziffer `%02d`" % n
            zeilen.append("| %d | %s | `%s` %s | %s | [ ] |" % (i, eb, stufe, ht[:70], neu))

    ziel = os.path.join(ROOT, "_design", "eyebrows.md")
    open(ziel, "w", encoding="utf-8").write(KOPF + "\n".join(zeilen) + "\n")
    print("%s geschrieben — %d Fundstellen auf %d Seiten"
          % (os.path.relpath(ziel, ROOT), gesamt,
             sum(1 for z in zeilen if z.startswith("\n### "))))


if __name__ == "__main__":
    sys.exit(main())
