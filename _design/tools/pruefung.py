#!/usr/bin/env python3
"""Abnahmepruefung aus REDESIGN.md §17, als laufendes Skript.

Aufruf:  python3 _design/tools/pruefung.py            (alle Seiten)
         python3 _design/tools/pruefung.py kontakt/index.html

Rueckgabewert 0 = alles gruen, 1 = mindestens ein Fehler.
Warnungen (WARN) blockieren nicht, sind aber anzusehen.

Waehrend des Umbaus schlagen noch nicht umgebaute Seiten an — das ist
gewollt: die Liste ist die Fortschrittsanzeige.
"""
import glob
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# "Helvetica Neue", Georgia und Arial sind reine Rueckfallschriften — erlaubt.
VERBOTENE_SCHRIFTEN = ("inter", "geist", "roboto", "open sans", "system-ui",
                       "libre baskerville")

ERLAUBTE_VERHAELTNISSE = {"v-7-5", "v-5-7", "v-9-3", "v-3-9", "v-4-8", "v-6-6", "v-auto-1"}

# Seiten, die es geben muss, und ihre kanonische Adresse.
SEITEN = {
    "index.html": "https://gehrkebauberatung.de/",
    "bauberatung/index.html": "https://gehrkebauberatung.de/bauberatung/",
    "baubetreuung/index.html": "https://gehrkebauberatung.de/baubetreuung/",
    "bauprojektmanagement/index.html": "https://gehrkebauberatung.de/bauprojektmanagement/",
    "denkmalsanierung/index.html": "https://gehrkebauberatung.de/denkmalsanierung/",
    "ueber-juergen/index.html": "https://gehrkebauberatung.de/ueber-juergen/",
    "kontakt/index.html": "https://gehrkebauberatung.de/kontakt/",
    "impressum/index.html": "https://gehrkebauberatung.de/impressum/",
    "datenschutz/index.html": "https://gehrkebauberatung.de/datenschutz/",
    "agb/index.html": "https://gehrkebauberatung.de/agb/",
}


class Sammler(HTMLParser):
    """Sammelt Ueberschriften, Bilder, Klassen und Randziffern einer Seite."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ueberschriften = []      # (stufe, text)
        self.bilder = []              # dict der Attribute
        self.klassen = []
        self.ziffern = []             # (text, aria_hidden)
        self.inline_styles = 0
        self.in_body = False
        self.h = None
        self.buf = []
        self.ziffer_offen = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "body":
            self.in_body = True
        if not self.in_body:
            return
        if "style" in a:
            self.inline_styles += 1
        cls = (a.get("class") or "").split()
        self.klassen.extend(cls)
        if "ziffer" in cls:
            self.ziffer_offen = [a.get("aria-hidden"), []]
        if tag == "img":
            self.bilder.append(a)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.h = int(tag[1])
            self.buf = []

    def handle_endtag(self, tag):
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self.h:
            self.ueberschriften.append(
                (self.h, re.sub(r"\s+", " ", "".join(self.buf)).strip()))
            self.h = None
        if tag == "span" and self.ziffer_offen is not None:
            self.ziffern.append(
                ("".join(self.ziffer_offen[1]).strip(), self.ziffer_offen[0]))
            self.ziffer_offen = None

    def handle_data(self, d):
        if self.h:
            self.buf.append(d)
        if self.ziffer_offen is not None:
            self.ziffer_offen[1].append(d)


def pruefe_stylesheet(fehler, warnung):
    pfad = os.path.join(ROOT, "assets", "site.css")
    if not os.path.exists(pfad):
        fehler.append("assets/site.css fehlt")
        return
    css = open(pfad, encoding="utf-8").read()
    ohne_kommentare = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    tief = ohne_kommentare.lower()

    if "#4a5d3c" in tief:
        fehler.append("site.css: Signalton #4A5D3C kommt noch vor (§3, §17)")
    for wort in VERBOTENE_SCHRIFTEN:
        # Wortgrenzen, sonst schlaegt "cursor:pointer" auf "inter" an.
        if re.search(r"\b%s\b" % re.escape(wort), tief):
            fehler.append("site.css: verbotene Schrift '%s' (§5.1)" % wort)
    for eigenschaft, paragraf in (("box-shadow", "§5.5"),
                                  ("backdrop-filter", "§5.5"),
                                  ("gradient", "§5.2"),
                                  ("text-shadow", "§5.3")):
        if eigenschaft in tief:
            fehler.append("site.css: %s verwendet (%s)" % (eigenschaft, paragraf))
    for treffer in re.findall(r"border-radius:\s*([^;}]+)", tief):
        wert = treffer.strip()
        if wert not in ("0", "0px", "var(--radius)"):
            fehler.append("site.css: border-radius %s (§5.4)" % wert)
    if "fonts.googleapis" in tief or "fonts.gstatic" in tief:
        fehler.append("site.css: laedt Schriften extern (§2, §17)")
    if "repeat(3,1fr)" in tief.replace(" ", "") or "1fr 1fr 1fr" in tief:
        warnung.append("site.css: drei gleiche Spalten gefunden (§8) — pruefen")


def pruefe_seite(pfad, fehler, warnung):
    rel = os.path.relpath(pfad, ROOT)
    src = open(pfad, encoding="utf-8").read()
    s = Sammler()
    s.feed(src)
    f = lambda t: fehler.append("%s: %s" % (rel, t))
    w = lambda t: warnung.append("%s: %s" % (rel, t))

    # --- Kopfdaten ---
    if '<html lang="de"' not in src:
        f('lang="de" fehlt (§13)')
    if 'rel="canonical"' not in src:
        f("canonical fehlt (§13)")
    elif rel in SEITEN:
        m = re.search(r'<link rel="canonical" href="([^"]+)"', src)
        if m and m.group(1) != SEITEN[rel]:
            f("canonical %s statt %s" % (m.group(1), SEITEN[rel]))
    if not re.search(r'<meta name="description" content="[^"]{50,}"', src):
        f("meta description fehlt oder ist zu kurz (§13)")
    if "application/ld+json" not in src:
        f("JSON-LD fehlt (§13)")
    else:
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', src, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                f("JSON-LD ungueltig: %s" % e)

    # --- Stylesheet statt Inline-Styles ---
    if '/assets/site.css' not in src:
        f("bindet assets/site.css nicht ein (§2)")
    if re.search(r"<style[\s>]", src):
        f("enthaelt einen <style>-Block — alles gehoert in site.css (§2)")
    if s.inline_styles:
        f("%d Inline-Styles im Markup (§2)" % s.inline_styles)

    # --- Schriften lokal ---
    for treffer in re.findall(r'https?://([a-z0-9.-]+)', src):
        if treffer.endswith("fonts.googleapis.com") or treffer.endswith("fonts.gstatic.com"):
            f("laedt Schriften von %s (§2, §17)" % treffer)

    # --- Ueberschriftenhierarchie ---
    stufen = [h[0] for h in s.ueberschriften]
    anzahl_h1 = stufen.count(1)
    if anzahl_h1 != 1:
        f("%d h1 statt genau einem (§13, §17)" % anzahl_h1)
    letzte = 0
    for stufe, text in s.ueberschriften:
        if letzte and stufe > letzte + 1:
            f("Ueberschriftensprung h%d -> h%d bei %r (§13)" % (letzte, stufe, text[:48]))
        letzte = stufe

    # --- Randziffern ---
    for text, aria in s.ziffern:
        if aria != "true":
            f("Randziffer %r ohne aria-hidden=\"true\" (§13, §17)" % text[:24])

    # --- Abschnittsmarken (die gestrichene Versalzeile) ---
    for klasse in ("section-eyebrow", "svc-hero-eyebrow", "eyebrow", "marke-oben"):
        if klasse in s.klassen:
            f("Abschnittsmarke .%s noch im Markup (§3, §17)" % klasse)

    # --- Spaltenverhaeltnisse ---
    verwendet = [k for k in s.klassen if k.startswith("v-")]
    unbekannt = sorted(set(verwendet) - ERLAUBTE_VERHAELTNISSE)
    if unbekannt:
        f("unerlaubtes Spaltenverhaeltnis: %s (§8)" % ", ".join(unbekannt))
    eindeutig = set(verwendet)
    if verwendet and len(eindeutig) < 3:
        w("nur %d verschiedene Spaltenverhaeltnisse, gefordert sind >= 3 (§8 Asymmetrieregel)"
          % len(eindeutig))

    # --- Bilder ---
    hero_gesehen = False
    for b in s.bilder:
        quelle = b.get("src", "")
        if quelle.startswith("data:"):
            f("Bild als base64 eingebettet (%s) — als Datei ausliefern (§13)"
              % (b.get("alt", "")[:30] or quelle[:30]))
        if not b.get("alt", "").strip():
            f("Bild ohne alt: %s (§13)" % quelle[:60])
        if not (b.get("width") and b.get("height")):
            f("Bild ohne width/height: %s (§13)" % quelle[:60])
        laden = b.get("loading")
        if laden == "eager" or b.get("fetchpriority") == "high":
            hero_gesehen = True
        elif laden != "lazy":
            w("Bild ohne loading=\"lazy\": %s (§13)" % quelle[:60])
    if s.bilder and not hero_gesehen:
        w("kein Bild mit loading=\"eager\" — das Hero-Bild braucht es (§13)")

    # --- Formular ---
    if "<form" in src:
        felder = re.findall(r'<(?:input|select|textarea)[^>]*id="([^"]+)"', src)
        labels = re.findall(r'<label[^>]*for="([^"]+)"', src)
        for feld in felder:
            if feld not in labels:
                f('Formularfeld id="%s" ohne <label for> (§14)' % feld)
        if "honigtopf" not in src and "botcheck" not in src:
            w("Formular ohne Honigtopf-Feld (§12)")
        if "/datenschutz/" not in src:
            f("Formular ohne Hinweis auf die Datenschutzseite (§12)")

    # --- Fokus ---
    if "outline:none" in src.replace(" ", "") or "outline: none" in src:
        f("outline:none im Markup (§14)")


def main(argv):
    ziele = argv[1:] or [p for p in SEITEN if os.path.exists(os.path.join(ROOT, p))]
    fehler, warnung = [], []

    pruefe_stylesheet(fehler, warnung)
    for rel in ziele:
        pfad = os.path.join(ROOT, rel)
        if not os.path.exists(pfad):
            fehler.append("%s fehlt" % rel)
            continue
        pruefe_seite(pfad, fehler, warnung)

    for t in warnung:
        print("WARN  %s" % t)
    for t in fehler:
        print("FEHL  %s" % t)
    print("\n%d Fehler, %d Warnungen, %d Seiten geprueft"
          % (len(fehler), len(warnung), len(ziele)))
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
