# CLAUDE.md — Gehrke Bauberatung

Verbindliches Regelwerk für alle Änderungen an dieser Website.
**Jede Session beginnt damit, diese Datei zu lesen.**

Das Design wurde vollständig ersetzt (Motiv „Aufnahme"). Alle früheren
Gestaltungsregeln — Navy `#0d1c2a`, Bronze `#b8763a`, Inter, Libre Baskerville,
feste Navigationsleiste, Karten mit Bronzelinie — **gelten nicht mehr.**

---

## Die drei Quellen, in dieser Rangfolge

| Rang | Datei | Rolle |
|---|---|---|
| 1 | `_design/REDESIGN.md` | **Der Style Guide. Bei jedem Widerspruch gewinnt er.** |
| 2 | diese Datei | Projektregeln, Umsetzung des Style Guides in diesem Repo |
| 3 | `_design/UMBAU.md` | Arbeitsplan für den laufenden Umbau |
| — | `_design/referenz/` | Der Prototyp aus dem Kundenpaket. **Nur Inspiration.** Sein Code, seine Texte und seine Adresse (Neuenstein) werden nicht übernommen. |

Weitere Arbeitsdateien:

- `_design/muster.html` — Bausteinkatalog, jeder Baustein als kopierfähiges Markup
- `_design/inventar/*.md` — der Bestandsinhalt je Seite, verbatim
- `_design/eyebrows.md` — Abarbeitungsliste der gestrichenen Versalzeilen
- `_design/tools/` — Prüf- und Extraktionsskripte

---

## Projektübersicht

- **Kunde:** Gehrke Bauberatung und -betreuung UG
- **Inhaber:** Jürgen Gehrke, Zimmermeister
- **Domain:** https://gehrkebauberatung.de
- **Technik:** reines HTML/CSS/JS. Kein Framework, kein Build-Schritt, kein Client-Routing.
- **Hosting:** GitHub Pages (`.nojekyll`, `CNAME`)
- **Wirkung:** nüchtern, verlässlich, handwerklich, inhabergeführt. Ausdrücklich keine Agentur-Optik.
- **Zielgruppen:** private Bauherren 35–60 mit Sanierungs- oder Kaufvorhaben,
  Hausverwaltungen, Architekten, Immobilieninvestoren.

---

## Seitenstruktur

```
/                          → index.html
/bauberatung/              → bauberatung/index.html
/baubetreuung/             → baubetreuung/index.html
/bauprojektmanagement/     → bauprojektmanagement/index.html  (Kommunen, Bauträger, WEGs)
/denkmalsanierung/         → denkmalsanierung/index.html
/ueber-juergen/            → ueber-juergen/index.html
/kontakt/                  → kontakt/index.html
/impressum/                → impressum/index.html
/datenschutz/              → datenschutz/index.html
/agb/                      → agb/index.html
/hausverwaltung/           → Weiterleitung auf /bauprojektmanagement/
404.html
```

- **`/referenzen/` gibt es nicht.** Referenzen sind ein Abschnitt auf der
  Startseite, verlinkt als `/#referenzen`. Keine eigene Seite anlegen.
- **`/bauabnahme/` ist verwaist:** die Datei existiert, ist nirgends verlinkt
  und nicht im Sitemap. Nicht ohne Rücksprache löschen.
- Neue Seite = eigener Ordner mit `index.html`. Verlinkung **immer mit
  abschließendem Schrägstrich**: `href="/baubetreuung/"`.
- **Keine Adresse ändern.** Ändert sich doch ein Pfad, braucht er eine
  dauerhafte Weiterleitung (301). Der Bestand rankt regional.

---

## Stylesheet

**Genau ein Stylesheet: `/assets/site.css`.** Es enthält Schriften, Merkmale,
alle Bausteine, Mobil, Fokus und Druck.

```html
<link rel="stylesheet" href="/assets/site.css">
```

- **Keine `<style>`-Blöcke in Seiten.** Keine `style="…"`-Attribute im Markup.
  Einzige Ausnahme wären echte Laufzeitwerte — die gibt es hier nicht.
- Kein CSS-Framework, keine externe CDN-Abhängigkeit.
- Braucht eine Seite etwas, das es noch nicht gibt: **Klasse in `site.css`
  ergänzen**, nicht inline schreiben.

---

## Merkmale (Design-Tokens)

Genau vier Farben. Keine Zwischenstufen erfinden, keine fünfte Farbe hinzufügen.

```css
:root{
  --grund:#F7F5F0;   /* Seitenhintergrund */
  --flaeche:#E8E2D6; /* abgesetzte Abschnitte, Fußband */
  --text:#17171A;    /* Text, Linien, Rahmen */
  --akzent:#8A3B12;  /* Randziffern, Links, primäre Handlungsaufforderung */
}
```

Erlaubte Transparenzen, immer auf Textton, und **nie schwächer als hier**:

| Zweck | Wert | Variable |
|---|---|---|
| Zeilentrenner | `rgba(23,23,26,.2)` | `--linie-fein` |
| sekundärer Fließtext | `.8` / `.78` | `--text-2` / `--text-3` |
| Bildlegende, Platzhalter | `.7` | `--legende` |
| Formular-Label | `.6` | `--label` |

**`#4A5D3C` ist gestrichen.** Der Signalton ist mit den Abschnittsmarken
entfallen und kommt im Projekt nicht mehr vor.

`theme-color` ist `#F7F5F0`, nicht mehr Navy.

---

## Schrift

Genau zwei Familien, beide selbst gehostet aus `/assets/fonts/`:

- **Spectral** (Serif) trägt den Inhalt: Titel, Fließtext, Zitate. Schnitte 300, 400, 300 kursiv.
- **Barlow** (Grotesk) trägt nur die Ordnung: Randziffern, Navigation, Wortmarke,
  Legenden, Tabellen, Formulare. Schnitte 400, 500.

```html
<link rel="preload" href="/assets/fonts/spectral-300-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/barlow-500-latin.woff2" as="font" type="font/woff2" crossorigin>
```

**Kein Aufruf von Google Fonts oder einer anderen fremden Domain.**
Nachladen der Dateien: `bash _design/tools/schriften_holen.sh`.

| Rolle | Familie | Größe / Zeile | Klasse |
|---|---|---|---|
| Seitentitel `h1` | Spectral 300 | 54 / 1.14 | — |
| Seitentitel Über-Seite | Spectral 300 | 48 / 1.14 | `.t-h1-klein` |
| Abschnittstitel `h2` | Spectral 400 | 30 / 1.2 | — |
| Untertitel `h3` | Spectral 400 | 26 / 1.25 | — |
| Listentitel | Spectral 300 | 22 / 1.35 | `.t-listentitel` |
| Vorspann | Spectral 300 | 19 / 1.8 | `.vorspann` |
| Fließtext Serif | Spectral 300 | 17–18 / 1.75–1.8 | `.fliess`, `.fliess-gross` |
| Fließtext Grotesk | Barlow 400 | 15 / 1.75–1.85 | `.fliess-grotesk` |
| Zitat | Spectral 300 kursiv | 32–34 / 1.4 | `.zitat` |
| Randziffer | Barlow 400 | 13 / 1, `.16em` | `.ziffer` |
| Navigation | Barlow 400 | 12 / 1, `.16em`, Versalien | `.nav` |
| Wortmarke | Barlow 500 | 12 / 1, `.28em`, Versalien | `.wortmarke` |
| Bildlegende | Barlow 400 | 12 / 1.5, `.1em`, Versalien | `.legende` |

Versalien nur bis 13 px. Keine Schriftgröße unter 11 px.

---

## Das Motiv: Randziffern an einer Protokolllinie

Jede Seite ist ein Protokoll. Jeder Abschnitt trägt links außen eine
Ordnungsziffer in Barlow, klein und gesperrt, in Akzentfarbe. Abschnitte werden
von Haarlinien eingefasst. **Ziffer und Linie sind die einzige Dekoration.**

```html
<div class="gruppe">
  <section class="abschnitt">
    <span class="ziffer" aria-hidden="true">02.1</span>
    <div class="inhalt">
      <h2>Beratung vor dem Kauf</h2>
      <p class="fliess">…</p>
    </div>
  </section>
</div>
```

- Die Gruppe öffnet mit einer Linie voller Deckung, der letzte Abschnitt
  schließt mit einer Linie voller Deckung. Dazwischen 20 % Deckung.
- Die Randziffer sitzt auf der Grundlinie der ersten Inhaltszeile — das macht
  `align-items:baseline` von selbst, es gibt nichts zu kalibrieren.
- **Randziffern sind immer `aria-hidden="true"` und ersetzen nie eine Überschrift.**

---

## Raster

- Satzspiegel 1180 px, Außenrand 64 px, `column-gap: 56px`.
- Abstand zwischen Abschnitten 96–104 px, innerhalb 26–34 px.
- **Erlaubte Spaltenverhältnisse — und nur diese:**
  `.v-7-5`, `.v-5-7`, `.v-9-3`, `.v-3-9`, `.v-4-8`, `.v-6-6`, `.v-auto-1`
  (jeweils zusammen mit `.v`).
- **Drei gleiche Spalten sind verboten.** Es gibt bewusst keine Klasse dafür.
- **Asymmetrieregel:** auf jeder Seite tragen mindestens drei Abschnitte ein
  anderes Verhältnis als die übrigen.
- Bilder laufen randlos über die volle Breite (`.band`) oder exakt spaltenbreit.
  `object-fit: cover`, feste Höhen, keine Rundung, keine Rahmen, kein Text im Foto.

---

## Bausteine

| Zweck | Klasse |
|---|---|
| Kopf, Startseite | `.kopf` + `.wortmarke` + `.kopf-linie` + `.nav` |
| Kopf, Unterseite | `.kopf.kopf--unterseite` + `.kopf-seitenname` (Seitenname in Akzent statt Navigation) |
| Mobiles Menü | `.menue`, geöffnet über das Wort „Menü", geschlossen über das Wort „Zu" |
| Primäre Handlungsaufforderung | `.cta` — Akzent, Unterlinie, `padding-bottom:7px` |
| Textlink im Abschnitt | `.cta-text` |
| Sekundäre Handlungsaufforderung | `.cta-2` — 1 px Rahmen, füllt sich beim Überfahren |
| Formularfeld | `.feld` — nur `border-bottom`, Label darüber |
| Fehler am Feld | `.feld[data-fehler]` + `.feld-fehler` |
| Ablauf in Schritten | `.ablauf` |
| Tabelle | `.tabelle`, Wert rechts in Akzent |
| Aufklappbare Frage | `.faq` mit nativem `<details>` |
| Zitat | `.zitat` + `.zitat-quelle` |
| Randnotiz an senkrechter Linie | `.randnotiz` |
| Rechtstext | `.rechtstext` |
| Partnerlogos | `.partner` |
| Senkrechter Rhythmus | `.stapel` |

Zustände und Übergänge:

```css
transition: color 120ms linear, background-color 120ms linear, border-color 120ms linear;
```

Mehr nicht. Keine Bewegung, keine Skalierung, keine Einblendungen beim Scrollen.

---

## Mobil (ab 900 px abwärts, Zielbreite 390 px)

- Einspaltig, Außenrand 20 px, `h1` 34 px.
- **Die Randziffer steht in derselben Zeile vor dem Titel, niemals darüber.**
  Das macht `.abschnitt{display:block}` plus `.ziffer{float:left}` — kein zweites Markup.
- Kopf: Marke zweizeilig links, „Menü" in Akzent rechts. **Kein Hamburger-Symbol.**
- Kein waagerechter Überlauf.

---

## Verhalten

Die Seite ist ein Dokument, keine Anwendung.

- Client-Zustand nur: mobiles Menü offen/zu, Formularwerte, Formularstatus.
- Kein Store, kein Client-Routing, harte Seitenwechsel.
- `cookie-consent.js` bleibt unverändert eingebunden (`defer`), lädt GA4 erst
  nach Einwilligung.
- Formular: `POST https://api.web3forms.com/submit`, Honigtopf statt Captcha,
  Prüfung erst beim Absenden, DSGVO-Zeile mit Kontrollkästchen über dem Knopf.

---

## SEO (Pflicht für jede Seite)

- Titel und Meta-Description **aus dem Bestand übernehmen**, nicht neu erfinden.
  Sie stehen in `_design/inventar/<seite>.md`.
- `lang="de"`, `canonical`, vollständige Open-Graph- und Twitter-Angaben.
- **Ein `h1` pro Seite. Überschriftenebenen lückenlos** — kein Sprung h2 → h4.
- JSON-LD: `LocalBusiness`/`ProfessionalService` auf jeder Seite,
  `BreadcrumbList` auf Unterseiten, `Service` je Leistungsseite,
  `FAQPage` bei Frageabschnitten, `Person` auf der Über-Seite.
- Ortsbezug im Text halten: Schwäbisch Hall, Heilbronn, Hohenlohe, Crailsheim,
  Landkreis Schwäbisch Hall, Öhringen, Künzelsau, Waldenburg, Bretzfeld,
  Ilshofen, Langenburg, Neuenstein. Träger ist die Ortsliste auf der Kontaktseite.
- Leistungsbegriffe wörtlich: Bauberatung, Baubetreuung, Baubegleitung,
  Fachwerksanierung, Sanierungsberatung, Kaufberatung Immobilie, Bauherrenberatung,
  Bauprojektmanagement, Denkmalsanierung.
- Zielwert: Largest Contentful Paint unter 2,0 s auf dem Mobilgerät.

### Bilder

Jedes `<img>` braucht:

- `alt` mit beschreibendem Text — **wörtlich aus dem Bestand**, die alt-Texte
  tragen Suchbegriffe
- `width` und `height` (echte Pixelmaße: `python3 _design/tools/bildmasse.py`)
- `loading="lazy"`, außer beim Hero-Bild der Seite:
  `loading="eager" fetchpriority="high"`

**Nie als `data:`-URI einbetten.** Alle Bilder liegen als Datei in `/assets/`,
flach, Dateiname klein und mit Bindestrichen.

---

## Barrierefreiheit

- Fokus immer sichtbar: 2 px Akzent-Umriss, 2 px Abstand. **Nie `outline:none`.**
- Formularlabels als echte `<label for>`.
- Randziffern dekorativ und `aria-hidden="true"`.
- Platzhalter nie unter 70 %, Labels nie unter 60 % Textton.
- Links im Fließtext sind unterstrichen — Farbe allein reicht nicht.
- Tastaturbedienung vollständig, mobiles Menü mit Escape schließbar.

---

## Kontaktdaten (immer diese)

```
Name:     Jürgen Gehrke
Firma:    Gehrke Bauberatung und -betreuung UG
Adresse:  Stauferstraße 122, 74523 Schwäbisch Hall
Tel:      +49 172 7410650
E-Mail:   info@gehrkebauberatung.de
WhatsApp: https://wa.me/491727410650
```

Die Wortmarke im Kopf lautet **„Gehrke Bauberatung"** (Platzgründe, siehe
`_design/UMBAU.md` D-1). Die vollständige Firmierung steht im Fuß, im Impressum
und in den strukturierten Daten.

Der WhatsApp-Link gehört auf jede Seite — er ist der wichtigste
Conversion-Kanal. Er ist ein normaler Link, **kein grüner Knopf**.

---

## Was nicht gemacht werden darf

- ❌ Eine fünfte Farbe, eine Zwischenstufe oder `#4A5D3C` verwenden
- ❌ Eine andere Schrift als Spectral und Barlow (nie Inter, Geist, Roboto,
  Open Sans, `system-ui`, Libre Baskerville)
- ❌ Schriften von einer fremden Domain laden
- ❌ `border-radius`, `box-shadow`, `backdrop-filter`, Farbverlauf, Textschatten
- ❌ Eine kleine Versalzeile über einer Überschrift
- ❌ Zentrierter Hero, Auszeichnungsmarke über der Überschrift
- ❌ Symbole in runden Kacheln, Symbolsätze, Karten, Schmuckelemente
- ❌ Ein symmetrisches Merkmalsraster aus drei gleichen Spalten
- ❌ Ein dunkler Handlungsaufforderungs-Block als vorletzter Abschnitt
- ❌ Emojis, Stockfotografie
- ❌ Bewegung, Skalierung, Einblendungen beim Scrollen
- ❌ Inline-Styles oder `<style>`-Blöcke statt `site.css`
- ❌ Bilder als base64 einbetten
- ❌ Bilder ohne `alt`, `width`, `height`
- ❌ CSS- oder JS-Frameworks, externe CDN-Abhängigkeiten
- ❌ Adressen ändern, Titel oder Meta-Descriptions neu erfinden
- ❌ Neue Seiten ohne abschließenden Schrägstrich

---

## Vor jedem Commit

```bash
python3 _design/tools/pruefung.py
```

muss **0 Fehler** melden. Dazu von Hand:

- [ ] Mobil bei 390 px angesehen, kein waagerechter Überlauf
- [ ] Randziffer steht mobil vor, nie über dem Titel
- [ ] Tastaturbedienung vollständig, Fokus überall sichtbar
- [ ] Mindestens drei verschiedene Spaltenverhältnisse auf der Seite
- [ ] Fuß und Kopf identisch zu den anderen Seiten
- [ ] Text unverändert gegenüber `_design/inventar/`

Vorschau:

```bash
python3 -m http.server 8787
```
