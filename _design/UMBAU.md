# Umbauplan — Redesign „Aufnahme"

**Für das Modell, das die Umsetzung macht. Von oben nach unten arbeiten.**

Auftrag: Das Design wird vollständig ersetzt. **Der Inhalt bleibt Wort für Wort
derselbe.** Kein Framework, kein Build-Schritt, statisches HTML wie bisher.

---

## 0. In dieser Reihenfolge lesen

| # | Datei | Rolle |
|---|---|---|
| 1 | `_design/REDESIGN.md` | **Der Style Guide. Verbindlich. Bei Widerspruch gewinnt er immer.** |
| 2 | `CLAUDE.md` | Das Regelwerk für dieses Repo, bereits auf das neue Design umgeschrieben |
| 3 | diese Datei | Der Arbeitsplan Schritt für Schritt |
| 4 | `assets/site.css` | Das fertige Stylesheet. Es ist geschrieben und im Browser geprüft. |
| 5 | `_design/muster.html` | Bausteinkatalog: jeder Baustein als kopierfähiges Markup |
| 6 | `_design/inventar/*.md` | Der Bestandsinhalt je Seite, verbatim. **Die Textquelle.** |
| 7 | `_design/referenz/` | Der Prototyp aus dem ZIP. **Nur Inspiration, kein Code zum Kopieren.** |

Rangfolge bei Widersprüchen: **REDESIGN.md > CLAUDE.md > diese Datei > Prototyp.**
Der Prototyp arbeitet mit Inline-Styles, weil das Werkzeug es verlangte, hat
eine falsche Adresse (Neuenstein statt Schwäbisch Hall) und erfundene Texte.
Er zeigt, wie es aussehen soll — nichts davon wird übernommen.

---

## 1. Was schon fertig ist (nicht noch einmal machen)

- [x] `assets/site.css` — das vollständige Stylesheet. Alle Bausteine, Mobil,
      Fokus, Druck. Besteht die eigene Prüfung (`pruefung.py`) fehlerfrei.
- [x] Schriften selbst gehostet: `assets/fonts/spectral-*.woff2`,
      `assets/fonts/barlow-*.woff2` (latin + latin-ext, 10 Dateien).
      Nachladen mit `bash _design/tools/schriften_holen.sh`.
- [x] `_design/muster.html` — Bausteinkatalog, im Browser geprüft.
- [x] `_design/inventar/` — Inhalt aller Seiten extrahiert.
      Neu erzeugen mit `python3 _design/tools/extract_content.py`.
- [x] `_design/tools/pruefung.py` — die Abnahmeprüfung aus REDESIGN §17 als Skript.
- [x] `assets/juergen-gehrke-bauberatung.jpg` — das einzige Bild, das nur als
      base64 im Markup steckte, ist als Datei ausgelagert.
- [x] `robots.txt` sperrt `/_design/`.
- [x] `.claude/launch.json` — Vorschauserver auf Port 8787.
- [x] `favicon.svg` und `site.webmanifest` auf die neue Palette umgestellt
      (Navy `#0d1c2a` und Bronze `#b8763a` kommen dort nicht mehr vor).

---

## 2. Die Ausgangslage im Bestand (wichtig, bevor du anfängst)

Zahlen aus `_design/inventar/` und `_design/tools/pruefung.py`:

| Befund | Menge | Folge für den Umbau |
|---|---|---|
| Bilder als base64 im HTML | 5 verschiedene, 108 KB Logo auf **jeder** Seite doppelt | Alle als Datei ausliefern. Das allein macht `index.html` von 821 KB auf ~40 KB. Ohne das ist LCP < 2,0 s nicht erreichbar. |
| `<style>`-Block je Seite | 4–20 KB, 12× dupliziert | Ersatzlos. Alles steckt in `assets/site.css`. |
| `.section-eyebrow` / `.svc-hero-eyebrow` / `.eyebrow` | 69 Fundstellen (53 ohne `/bauabnahme/`) | Die verbotene Versalzeile über der Überschrift. Auflösung siehe Abschnitt 4. |
| Überschriftensprünge h2→h4 / h2→h5 | auf 8 Seiten | Beim Neuaufbau lückenlos setzen. |
| `/referenzen/` | **existiert nicht**, wird aber verlinkt (`/#referenzen`) | Bleibt ein Anker auf der Startseite. Keine eigene Seite anlegen. |
| `/bauabnahme/` | existiert, nirgends verlinkt, nicht im Sitemap | Verwaist. Nicht umbauen, nicht löschen. Siehe Abschnitt 9. |
| `/hausverwaltung/` | 393 Byte Weiterleitung auf `/bauprojektmanagement/` | Bleibt unverändert. |
| Formular | `POST https://api.web3forms.com/submit`, Honigtopf `botcheck` | Bleibt. Erfüllt REDESIGN §12 bereits. Siehe Abschnitt 7. |
| `cookie-consent.js` | lädt GA4 nach Einwilligung, `defer` | Bleibt unverändert eingebunden. Nicht im kritischen Pfad. |
| PDF-Banner auf `index.html` (Zeile ~718) | in einen HTML-Kommentar gelegt, wartet auf `/checkliste.pdf` | **Als Kommentar mitnehmen, nicht löschen.** Beim Reaktivieren gilt §3 wie überall: `.pdf-eyebrow` wird zur Randziffer. |

---

## 3. Seitenabbildung Prototyp → Bestand

Der Prototyp beschreibt eine Seitenstruktur, die nicht deckungsgleich mit dem
Bestand ist. **Der Bestand gewinnt** — Adressen bleiben unverändert (REDESIGN §13).

| Prototyp-Screen | Muster | Reale Seite |
|---|---|---|
| 01 Startseite | Startseite | `index.html` |
| 02 Leistungsseite | Leistungsmuster | `bauberatung/index.html` |
| 03 Baubetreuung | Leistungsmuster, Bild gespiegelt (7/5) | `baubetreuung/index.html` |
| 04 Fachwerk und Sanierung | Leistungsmuster, Bild gespiegelt (7/5) | `denkmalsanierung/index.html` |
| 05 Verwaltungen und Investoren | Verwaltungsmuster | `bauprojektmanagement/index.html` |
| 06 Über Jürgen Gehrke | Übermuster | `ueber-juergen/index.html` |
| 07 Referenzen | — | **entfällt.** Bleibt der Abschnitt `#referenzen` auf der Startseite. |
| 08 Kontakt und Anfrage | Kontaktmuster | `kontakt/index.html` |
| 09 Impressum und Datenschutz | Rechtsmuster | `impressum/`, `datenschutz/`, `agb/` |
| — | 404 | `404.html` — Kopf, eine Überschrift, Fuß. Sonst nichts. |

**Keine neuen Adressen. Keine Weiterleitungen nötig**, weil sich kein Pfad ändert.
`sitemap.xml` bleibt wie er ist.

---

## 4. Die harte Änderung: die Versalzeile über der Überschrift (REDESIGN §3)

Sie entfällt vollständig. Im Bestand heißt sie `.section-eyebrow` bzw.
`.svc-hero-eyebrow`. **Alle 69 Fundstellen sind reine Ordnung oder Dekoration** —
keine trägt Information, die nicht schon in der Überschrift daneben steht.
Daraus folgt eine mechanische Regel:

> **Eyebrow im Hero (direkt über dem `h1`) → ersatzlos weg.**
> Der Seitenname, den er trug, steht künftig im Kopf in Akzentfarbe
> (`.kopf-seitenname`) — er geht also nicht verloren.
>
> **Jeder andere Eyebrow → wird zur Randziffer** des Abschnitts, der ihm folgt.
> Durchnummeriert von oben nach unten: `01`, `02`, `03`, … Bei Unterpunkten
> `02.1`, `02.2`. Ausgabe immer als
> `<span class="ziffer" aria-hidden="true">02</span>`.

Die vollständige Liste aller Fundstellen mit Zielziffer steht in
`_design/eyebrows.md`. Diese Liste ist beim Umbau abzuarbeiten und abzuhaken.

Danach darf `pruefung.py` auf keiner Seite mehr `Abschnittsmarke .section-eyebrow`
melden, und `#4A5D3C` kommt im Projekt nicht mehr vor.

---

## 5. Aufbau einer Seite — das Gerüst

Jede Seite hat exakt diesen Rahmen. Kopie aus `_design/muster.html`.

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- 1:1 aus _design/inventar/<seite>.md, Abschnitt "Kopfdaten" -->
  <title>…</title>
  <meta name="description" content="…">
  <link rel="canonical" href="https://gehrkebauberatung.de/…/">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="author" content="Jürgen Gehrke">
  <meta name="geo.region" content="DE-BW">
  <meta name="geo.placename" content="Schwäbisch Hall">
  <meta name="theme-color" content="#F7F5F0">   <!-- NEU: Grundton, nicht mehr Navy -->

  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="Gehrke Bauberatung">
  <meta property="og:url" content="…">
  <meta property="og:title" content="…">
  <meta property="og:description" content="…">
  <meta property="og:image" content="https://gehrkebauberatung.de/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="…">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="…">
  <meta name="twitter:description" content="…">
  <meta name="twitter:image" content="https://gehrkebauberatung.de/assets/og-image.jpg">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <link rel="preload" href="/assets/fonts/spectral-300-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/barlow-500-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css">

  <script type="application/ld+json">{ … }</script>
</head>
<body>
  <a class="zum-inhalt" href="#inhalt">Zum Inhalt springen</a>
  <header class="kopf"> … </header>
  <div class="menue" id="menue"> … </div>
  <main id="inhalt" class="seite"> … </main>
  <footer class="fuss"> … </footer>
  <script> /* mobiles Menü, siehe muster.html */ </script>
  <script src="/cookie-consent.js" defer></script>
</body>
</html>
```

**`theme-color` wechselt von `#0d1c2a` auf `#F7F5F0`.** Das alte Navy gibt es
im neuen Design nicht mehr. `site.webmanifest` und `favicon.svg` sind bereits
umgestellt.

### Kopf

- Startseite: Wortmarke + Haarlinie + Navigation.
- Alle Unterseiten: Wortmarke + Haarlinie + **Seitenname in Akzent** statt Navigation
  (REDESIGN §10). Die volle Navigation steckt dort nur im mobilen Menü — sie ist
  auf jeder Seite über das Wort „Menü" erreichbar, das ab 900 px Breite erscheint.
  **Entscheidung D-2, siehe Abschnitt 10.**

### Fuß

Der Prototyp-Fuß ist eine Zeile: Marke links, Impressum/Datenschutz rechts.
Der Bestandsfuß hat drei Spalten mit Leistungslinks. **Die Links sind Inhalt und
bleiben** — sie wandern in `.fuss-links`, ergänzt um Kontakt und AGB. Die beiden
`h5`-Überschriften („Leistungen", „Unternehmen") entfallen; sie waren Gliederung
einer Kartenstruktur, die es nicht mehr gibt, und erzeugen den Sprung h2→h5.

---

## 6. Bausteine, die es im Prototyp nicht gibt

Der Bestand hat mehr Inhaltstypen als der Prototyp zeigt. Für jeden gibt es eine
Klasse in `site.css` und ein Beispiel in `muster.html`:

| Bestandsbaustein | Bisher | Neu |
|---|---|---|
| FAQ (`<details>`, 40 Stück) | `.faq-item` | `.faq` — natives `details`, kein Symbol, kein Pfeil. `FAQPage`-JSON-LD bleibt. |
| Kundenstimmen | `.testimonial-*`, Karten | Abschnitte mit Randziffer. Zitat in `.zitat.zitat-klein`, Quelle in `.zitat-quelle`. |
| Sterne `★★★★★` | Dekoration | **Inhalt** (die Bewertung). Bleibt, als `.sterne` mit `aria-label`. Kein Emoji im Sinn von §5.10. |
| Partnerlogos (5) | `.partner-item` | `.partner` — Graustufe, 75 % Deckung, damit die Fremdfarben das Motiv nicht brechen. |
| Ablauf in vier Schritten | `.ablauf-step`, Karten | `.ablauf` — vier Spalten, nur Haarlinien. Erlaubt: es ist eine Zeitachse, kein Merkmalsraster. |
| „Warum"-Kacheln 01–04 | `.warum-cell` + `.warum-cell-num` | Abschnitte mit Randziffer. Die Nummer ist schon da. |
| „Vielleicht auch interessant" | `.cross-card` | Abschnittsgruppe mit Randziffern, Textlink je Zeile. |
| Preis-/Leistungstabelle | `.split-*` | `.tabelle`, Wert rechts in Akzent. |
| Zeitleiste Werdegang | `.timeline-item` + `.timeline-year` | Abschnitte, Randziffer = Jahr. |
| Vertrauenszahlen (30+, 100+) | `.svc-hero-trust-num` | Abschnitte mit Randziffer, wie die Faktenliste der Über-Seite. |
| Buttons `.btn-primary` / `.btn-ghost` / `.btn-whatsapp` | drei Sorten | Zwei: `.cta` (primär, Akzentlinie) und `.cta-2` (sekundär, Rahmen). WhatsApp ist ein normaler Link, kein grüner Knopf. |

**Pfeile `→` in Linktexten** („Mehr →", „Ihr Projekt besprechen →") entfallen.
Sie sind Dekoration, nicht Inhalt; der Linktext bleibt vollständig erhalten.
`↳` in der mobilen Navigation entfällt ebenfalls — die Verschachtelung zeigt sich
im neuen Menü über die Randziffern.

---

## 7. Formular (Kontaktseite)

Bleibt technisch unverändert: `POST https://api.web3forms.com/submit`, Feldnamen
`Vorname`, `Nachname`, `email`, `Telefon`, `Leistung`, `Nachricht`, Honigtopf
`botcheck`, `access_key` unverändert. Das erfüllt REDESIGN §12 („serverseitig als
Mail an den Inhaber, Honigtopf statt Captcha") bereits.

Neu nur die Gestalt:

- Nur `border-bottom`, kein Rahmen, kein Radius, kein Schatten.
- Jedes Feld ein echtes `<label for>`, Label darüber in Barlow 500 / 11 px Versalien.
- Platzhalter bei 70 % Textton — **nie schwächer** (Kontrastuntergrenze).
- Fokus: Linie 2 px Akzent. Kein Schein, kein Ring.
- Fehler: Textzeile unter dem Feld in Akzent, Feldlinie 2 px. Keine rote Fläche,
  kein Symbol. Markup: `<p class="feld" data-fehler>` plus `<span class="feld-fehler">`,
  verknüpft über `aria-describedby`.
- DSGVO-Zeile mit Kontrollkästchen über dem Absenden-Knopf (`.zustimmung`).
- Prüfung erst beim Absenden (`novalidate` am Formular, Prüfung im vorhandenen
  Skript). Der bestehende Erfolgs- und Fehlertext bleibt wörtlich erhalten.

---

## 8. Bilder

Alle Bilder sind bereits als Datei in `/assets/` vorhanden. Beim Umbau
**jedes `src="data:image/…"` durch den Dateipfad ersetzen.** Zuordnung:

| base64 im Bestand (alt-Text) | Datei | Maße |
|---|---|---|
| Gehrke Bauberatung (Logo, Kopf + Fuß) | entfällt — Wortmarke ist Typografie (REDESIGN §15) | — |
| Jürgen Gehrke bei der Bauberatung | `/assets/juergen-gehrke-bauberatung.jpg` | 952×1288 |
| Jürgen Gehrke | `/assets/juergen-gehrke.jpg` | 700×1036 |
| Fachwerkhaus mit modernem Anbau | `/assets/referenz-fachwerk-anbau.jpg` | 1100×825 |
| Jürgen Gehrke begutachtet bei einer Begehung | `/assets/bauberatung-begehung.jpg` | 930×620 |
| Jürgen Gehrke begutachtet mit einem Bauherrn | `/assets/baubetreuung-beratung.jpg` | 930×620 |
| Denkmalgeschütztes Fachwerkhaus | `/assets/denkmal-altbau-sanierung.jpg` | 1040×780 |

Weitere vorhandene Bilder: `juergen-gehrke-beratung-fachwerk.png` (1252×975),
`baubetreuung-fachwerk-fassade.png` (930×620), `bauberatung-fachwerk-begehung.png`
(930×620), die fünf Partnerlogos.

Regeln je `<img>`:
- `alt` **wörtlich aus dem Bestand übernehmen** — die alt-Texte tragen Suchbegriffe.
- `width` und `height` gesetzt (echte Pixelmaße, siehe `python3 _design/tools/bildmasse.py`).
- `loading="lazy"` überall außer dem Hero-Bild der Seite; dort
  `loading="eager" fetchpriority="high"`.
- Keine Rundung, kein Rahmen, kein Text über dem Foto.

**Das Logo verschwindet aus Kopf und Fuß.** REDESIGN §15 sagt ausdrücklich: „im
Entwurf wird die typografische Wortmarke in Barlow verwendet". `logo-dark.png`
bleibt als Datei liegen (für `og-image` und Fremdverwendung), wird aber nicht mehr
eingebunden. Das spart 216 KB pro Seitenaufruf.

**Offene Nacharbeit (nicht blockierend):** `juergen-gehrke-beratung-fachwerk.png`
ist 2,0 MB. Als JPEG oder WebP bei gleicher Kantenlänge neu ausspielen, sonst ist
LCP < 2,0 s auf Mobil knapp. Dasselbe für `baubetreuung-fachwerk-fassade.png` und
`bauberatung-fachwerk-begehung.png` (je ~950 KB).

---

## 9. Arbeitsreihenfolge

Eine Seite nach der anderen, jede vollständig fertig, bevor die nächste beginnt.
Nach jeder Seite: `python3 _design/tools/pruefung.py <pfad>` muss 0 Fehler melden.

1. **`kontakt/index.html`** — zuerst. Kleinste Seite mit Formular, deckt fast alle
   Bausteine ab und ist der beste Test für das Stylesheet.
2. **`index.html`** — Startseite. Hero, Abschnittsgruppe, Bildband, Zitat, Ablauf,
   Kundenstimmen, Referenzanker `#referenzen`, Partnerlogos.
3. **`bauberatung/index.html`** — legt das Leistungsmuster fest.
4. **`baubetreuung/index.html`**, **`denkmalsanierung/index.html`** — dasselbe
   Muster, Bild gespiegelt (5/7 statt 7/5).
5. **`bauprojektmanagement/index.html`** — Verwaltungsmuster mit Tabelle und dem
   einzigen 6/6 der ganzen Seite.
6. **`ueber-juergen/index.html`** — Porträt randlos links 5/7, Faktenliste,
   Haltungsblock.
7. **`impressum/`, `datenschutz/`, `agb/`** — Rechtsmuster, einspaltig 9/3,
   Randziffern als Paragraphennummern. **Rechtstexte wortgleich übernehmen.**
8. **`404.html`** — Kopf, `h1`, ein Satz, Link zur Startseite, Fuß.
9. **`bauabnahme/index.html`** — verwaist. Zwei Möglichkeiten, beide vertretbar:
   entweder ebenfalls umbauen (Rechtsmuster genügt nicht, es ist eine Leistungsseite),
   oder unverändert liegen lassen. Sie ist nirgends verlinkt und nicht im Sitemap.
   **Empfehlung: unverändert liegen lassen**, dann aber `<meta name="robots"
   content="noindex, follow">` setzen, damit sie nicht mit altem Design im Index steht.
   Vor dem Löschen den Kunden fragen.
10. **Aufräumen, erst ganz am Ende:**
    - `assets/fonts.css` löschen (Inter / Libre Baskerville — nach dem Umbau ungenutzt).
    - `assets/fonts/inter-*.woff2` und `assets/fonts/librebaskerville-*.woff2` löschen.
    - Doppelte Bilddateien prüfen: `Augsten .png`/`partner-augsten.png`,
      `Bürk.jpg`/`partner-burk.jpg`, `Drechsler.jpeg`, `Podstawek.jpg`,
      `Strecker.png` sind byteweise identisch. Die Varianten ohne `partner-`-Präfix
      entfernen, sobald keine Seite sie mehr referenziert.
    - `.DS_Store` aus dem Repo nehmen und in `.gitignore` eintragen.

---

## 10. Entscheidungen, die schon getroffen sind

**D-1 — Wortmarke im Kopf lautet „Gehrke Bauberatung", nicht „Gehrke — Bauberatung
und Betreuung".** Grund: gemessen. Die lange Fassung ist 347 px breit, die
Navigation braucht 644 px; bei 1180 px Satzspiegel bleiben für die Haarlinie 5 px
übrig — die Linie verschwindet faktisch. Mit der kurzen Fassung (188 px) bleiben
128 px Linie. Die vollständige Firmierung steht weiterhin im Fuß, im Impressum und
in den strukturierten Daten. Falls der Kunde die lange Fassung im Kopf will: einen
Navigationspunkt streichen, nicht die Sperrung reduzieren.

**D-2 — Auf Unterseiten steht im Kopf der Seitenname statt der Navigation**
(so schreibt es REDESIGN §10 für Leistungsseiten). Damit die Seite von jeder
Unterseite aus navigierbar bleibt, ist der „Menü"-Knopf **auf allen Breiten**
sichtbar, wenn keine Navigation im Kopf steht — nicht nur unter 900 px. Das ist
eine Ergänzung, kein Widerspruch: REDESIGN §12 kennt das vollflächige Menü bereits,
und Tastaturbedienung muss vollständig sein (§14, §17).
Umsetzung: `<header class="kopf kopf--unterseite">` — die Regel steht bereits
in `site.css`.

**D-3 — Randziffern werden je Seite von oben nach unten neu durchnummeriert.**
Sie sind `aria-hidden` und tragen keine Bedeutung außer Ordnung. Vorlage:
Startseite `01` Hero (entfällt sichtbar), `02.1`–`02.n` Leistungen, `03` Zitat,
`04` Ablauf, `05.x` Kundenstimmen.

**D-4 — Die Adresse ist Stauferstraße 122, 74523 Schwäbisch Hall.**
Der Prototyp zeigt „74632 Neuenstein". Das ist falsch und wird nicht übernommen.
Ebenso: Telefon `+49 172 7410650` und `info@gehrkebauberatung.de` sind vorhanden —
die „offenen Punkte" in REDESIGN §16 Nr. 1 und 2 sind damit erledigt.

**D-5 — Formular-Labels auf dem Flächenton stehen bei 66 %, nicht 60 %.**
Nachgerechnet: Textton mit 60 % Deckung ergibt auf `#F7F5F0` 4,53:1 (knapp über
der Grenze), auf `#E8E2D6` aber nur 4,29:1 — darunter. REDESIGN §14 misst nur
gegen den Grundton, der Anfrageblock der Verwaltungsseite liegt aber auf dem
Flächenton (§10). `site.css` setzt `--label` innerhalb von `.flaeche` deshalb auf
66 % → 5,16:1. Das ist stärker als die Untergrenze, verletzt sie also nicht.
Die übrigen gemessenen Werte aus §14 stimmen exakt: Textton auf Grundton 16,42:1,
Akzent auf Grundton 7,10:1, Akzent auf Flächenton 6,00:1, Platzhalter 6,33:1.

**D-6 — Ortsbezug (REDESIGN §13).** Der Prototyp nennt Hohenlohe-Orte, der Bestand
rankt auf Schwäbisch Hall, Heilbronn, Hohenlohe, Crailsheim. **Der Bestand gewinnt.**
Die Ortsliste auf der Kontaktseite darf die Prototyp-Orte (Öhringen, Künzelsau,
Waldenburg, Bretzfeld, Ilshofen, Langenburg, Neuenstein) **ergänzen** — sie sind
echtes Einsatzgebiet und stärken das lokale Ranking. Keinen bestehenden Ort streichen.

---

## 11. Offene Punkte für den Kunden

Nicht erfinden. Wenn nötig als sichtbarer Platzhalter im Markup.

1. Honorarangaben für die Tabelle auf `/bauprojektmanagement/`. Bis dahin steht
   dort weiterhin „Auf Anfrage" — so wie im Bestand.
2. Referenzobjekte mit Fotos, Ort, Jahr, Maßnahme. Bis dahin bleibt der
   Referenzabschnitt auf der Startseite mit dem einen vorhandenen Projekt.
3. Soll `/bauabnahme/` bleiben, umgebaut oder gelöscht werden?
4. Sollen die drei großen PNG (zusammen 3,9 MB) neu ausgespielt werden?
5. **Rasterbilder mit alter Palette:** `favicon.ico`, `apple-touch-icon.png`,
   `icon-192.png`, `icon-512.png` und `assets/og-image.jpg` tragen noch Navy
   und Bronze. `favicon.svg` deckt moderne Browser ab; die PNG-Fassungen müssen
   aus der SVG neu gerendert werden (ImageMagick oder Grafikprogramm). Nicht
   blockierend, aber vor dem Livegang zu erledigen.

---

## 12. Abnahme

```bash
python3 _design/tools/pruefung.py
```

muss **0 Fehler** melden. Zusätzlich von Hand:

- [ ] Keine kleine Versalzeile über irgendeiner Überschrift, auch nicht mobil.
- [ ] `#4A5D3C` kommt im ganzen Projekt nicht mehr vor.
- [ ] Auf jeder Seite mindestens drei verschiedene Spaltenverhältnisse,
      nirgends drei gleiche Spalten.
- [ ] Randziffern stehen mobil **vor**, nie über dem Titel.
- [ ] Tastaturbedienung vollständig, Fokus überall sichtbar, mobiles Menü mit
      Escape schließbar.
- [ ] Alle Bestandsadressen erreichbar, Titel und Meta-Descriptions übernommen.
- [ ] Keine externe Domain außer `api.web3forms.com` (Formular),
      `wa.me` (WhatsApp) und dem, was `cookie-consent.js` nach Einwilligung lädt.
- [ ] LCP unter 2,0 s auf Mobil.

Vorschau während der Arbeit:

```bash
python3 -m http.server 8787
```
