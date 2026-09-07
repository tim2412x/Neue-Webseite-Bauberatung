# Handoff: Gehrke Bauberatung und Betreuung — visuelle Neuentwicklung der Website

## Overview
Vollständige visuelle Neuentwicklung des Webauftritts von **Gehrke Bauberatung und Betreuung** (Inhaber Jürgen Gehrke), Bauberatung und Baubetreuung im Kreis Hohenlohe / Schwäbisch Hall. Zielgruppen: private Bauherren 35–60 mit Sanierungs- oder Kaufvorhaben, professionelle Hausverwaltungen, Architekten, Immobilieninvestoren. Gewünschte Wirkung: nüchtern, verlässlich, handwerklich, inhabergeführt — ausdrücklich **keine Agentur-Optik**.

Die Vorlage definiert Motiv, Palette, Typografie, Raster und sechs Seitentypen. Der Entwickler baut daraus die vollständige Seite (alle Unterseiten folgen den hier gezeigten Mustern).

## About the Design Files
Die Dateien in diesem Bundle sind **Design-Referenzen in HTML** — Prototypen, die Aussehen und Verhalten zeigen, kein Produktionscode zum Kopieren. Aufgabe ist, diese Entwürfe in der Zielumgebung neu aufzubauen (Astro, Eleventy, Next.js, WordPress-Theme, statisches HTML/CSS — was für eine kleine, SEO-getriebene Firmenseite passt). Existiert noch kein Stack: eine statische Ausgabe ohne Client-Framework ist hier die richtige Wahl (Astro oder Eleventy), da die Seite fast vollständig aus Inhalt besteht.

Die Prototypen nutzen ausschließlich Inline-Styles, weil das Design-Werkzeug es verlangt. **Im Zielprojekt bitte in echtes CSS mit Custom Properties und wenigen Utility-Klassen übersetzen** — nicht die Inline-Styles übernehmen.

## Fidelity
**High-fidelity.** Farben, Typografie, Größen, Abstände und Spaltenverhältnisse sind final und exakt einzuhalten. Wo Inhalte fehlen (Telefon, E-Mail, Referenzen), ist das im Text markiert — Layout steht, Inhalt ist nachzuliefern.

## Gestaltungsmotiv (verbindlich, trägt alle Seiten)
**„Aufnahme" — Randziffern an einer durchlaufenden Protokolllinie.**
Jede Seite ist als Protokoll gedacht. Jeder Abschnitt trägt links außen eine Ordnungsziffer (`01`, `02.1`, `02.2`, `Schritt 1`, `seit 1998`) in Barlow, klein und gesperrt, in Akzentfarbe. Abschnitte werden von einer 1 px Haarlinie über die volle Satzbreite eingefasst; Zeilen innerhalb eines Abschnitts von einer Haarlinie mit 20 % Deckung. Ziffer und Linie sind die **einzige** Dekoration der Seite — es gibt keine Karten, keine Icons, keine Schmuckelemente.

Umsetzung: zwei-Spalten-Grid `grid-template-columns: auto 1fr; column-gap: 56px`, die Ziffer in Spalte 1, der Inhalt in Spalte 2 mit `border-bottom`. Der erste Abschnitt wird von einer 100 %-Linie eröffnet, der letzte von einer 100 %-Linie geschlossen.

## Harte Ausschlussliste (gilt weiter im Code)
1. Keine der Schriften Inter, Geist, Roboto, Open Sans, `system-ui`.
2. Keine Farbverläufe, keinerlei.
3. Kein Verlaufstext, keine Leucht- oder Textschatteneffekte.
4. `border-radius: 0` ausnahmslos (max. 4 px wären erlaubt — genutzt wird 0).
5. Keine `box-shadow`, kein `backdrop-filter`, kein Milchglas.
6. Kein zentrierter Hero, kein Badge über der Überschrift.
7. Keine Symbole in runden Kacheln, keine Icon-Sets.
8. Kein symmetrisches Drei-Spalten-Merkmalsraster.
9. Kein dunkler CTA-Block als vorletzter Abschnitt.
10. Keine Emojis, keine Stockfotografie (Handschlag, Bauhelm, lächelndes Team). Nur die echten Fotos aus `uploads/`.

## Design Tokens

### Farbe — genau fünf Werte, keine Zwischenstufen erfinden
| Rolle | Hex | Verwendung |
|---|---|---|
| Grundton | `#F7F5F0` | Seitenhintergrund, Text auf dunklen Flächen |
| Flächenton | `#E8E2D6` | abgesetzte Abschnitte, Footer-Band |
| Textton | `#17171A` | Text, Linien, Rahmen |
| Akzent | `#8A3B12` | Ordnungsziffern, Links, primärer CTA |
| Signalton | `#4A5D3C` | ausschließlich Abschnittsmarken („Aufnahme 01 — …") |

Einzige erlaubte Transparenzen, jeweils auf Textton: `rgba(23,23,26,.2)` Zeilentrenner, `.78`/`.8` sekundärer Fließtext, `.7` Bildlegenden, `.6` Formular-Labels, `.7` Platzhalter (verbindlich, nie schwächer). Sonst nichts.

```css
:root{
  --grund:#F7F5F0; --flaeche:#E8E2D6; --text:#17171A;
  --akzent:#8A3B12; --signal:#4A5D3C;
  --linie:#17171A; --linie-fein:rgba(23,23,26,.2);
  --rand:64px; --spalte-gap:56px; --radius:0;
}
```

### Schrift — genau zwei Familien, selbst hostbar
- **Spectral** (Serif, ausgeprägter Charakter) — Inhalt: Seitentitel, Abschnittstitel, Fließtext, Zitate. Schnitte: 300, 400, 300 italic. SIL Open Font License, selbst hostbar.
- **Barlow** (Grotesk, nur in dienender Rolle) — Ordnung: Ziffern, Navigation, Marke, Legenden, Tabellen, Formulare. Schnitte: 400, 500. SIL Open Font License, selbst hostbar.

Im Prototyp werden sie von Google Fonts geladen. **Im Zielprojekt selbst hosten**: WOFF2 der genannten Schnitte in `/fonts`, `@font-face` mit `font-display: swap`, latin + latin-ext Subset, `preload` für Spectral 300 und Barlow 500.

### Typografische Skala
| Rolle | Familie | Größe / Zeile | Weitere |
|---|---|---|---|
| Seitentitel (h1) | Spectral 300 | 54 / 1.14 | `letter-spacing:-.01em`, `max-width:24–26ch` |
| Seitentitel Über-Seite | Spectral 300 | 48 / 1.14 | |
| Abschnittstitel (h2) | Spectral 400 | 30 / 1.2 | |
| Untertitel (h3) | Spectral 400 | 26 / 1.25 | |
| Listentitel | Spectral 300 | 22 / 1.35 | |
| Vorspann | Spectral 300 | 19 / 1.8 | `max-width:56ch` |
| Fließtext Serif | Spectral 300 | 17–18 / 1.75–1.8 | `max-width:70ch` |
| Fließtext Sans | Barlow 400 | 15 / 1.75–1.85 | sekundär, Aufzählungen, Tabellen |
| Zitat | Spectral 300 italic | 32–34 / 1.4 | `max-width:34–36ch` |
| Abschnittsmarke | Barlow 500 | 11 / 1 | `letter-spacing:.28em`, uppercase, Signalton |
| Ordnungsziffer | Barlow 400 | 13 / 1 | `letter-spacing:.16em`, Akzent |
| Navigation | Barlow 400 | 12 / 1 | `letter-spacing:.16em`, uppercase |
| Wortmarke | Barlow 500 | 12 / 1 | `letter-spacing:.28em`, uppercase |
| Bildlegende | Barlow 400 | 12 / 1.5 | `letter-spacing:.1em`, uppercase, 70 % Textton |
| CTA-Label | Barlow 500 | 12–13 / 1 | `letter-spacing:.18–.2em`, uppercase |

Versalien nur bis 13 px. Keine Schriftgröße unter 11 px.

### Raster, Abstände, Rhythmus
- Satzspiegel 1180 px, Außenrand 64 px, Zwölfspalter, `column-gap: 56px`.
- Abschnittsabstand 96–104 px; innerhalb eines Abschnitts 26–34 px; Zeilenpolster 24–34 px.
- Erlaubte Spaltenverhältnisse: `7fr 5fr`, `5fr 7fr`, `9fr 3fr`, `3fr 9fr`, `4fr 8fr`, `6fr 6fr`, `auto 1fr`. **Verboten: drei gleiche Spalten.**
- **Asymmetrie-Regel:** auf jeder Seite müssen mindestens drei Abschnitte ein anderes Verhältnis tragen als die übrigen. Startseite z. B. 7/5 (Hero) → auto/1fr (Leistungen) → randlos (Bild) → 4/8 (Zitat) → 9/3 (Ablauf).
- Bilder laufen randlos über die volle Breite oder exakt spaltenbreit; `object-fit: cover`, feste Höhen (siehe Screens), keine Rundungen, keine Rahmen, kein Overlay-Text auf Fotos.

### Zustände
- Link / primärer CTA: Akzent, `border-bottom:1px solid` Akzent, `padding-bottom:7px`. Hover: Farbe und Linie auf Textton. Kein Unterstrich-Wackeln, keine Transition über 120 ms.
- Sekundärer CTA: `1px solid` Textton, `padding:12–14px 20–24px`, Radius 0. Hover: Fläche Textton, Schrift Grundton.
- Formularfeld: nur `border-bottom:1px solid` Textton, Label darüber in Barlow 500 / 11 px uppercase, Platzhalter Textton 70 % (keine schwächere Stufe — Kontrastuntergrenze). Fokus: Linie 2 px Akzent, kein Glow, kein Ring.
- Navigation aktiv: Akzent. Inaktiv: Textton.

## Screens / Views
Alle im Prototyp `Gehrke Website Vorlage.dc.html` enthalten, jeweils mit `data-screen-label`.

### 00 Bauteilkatalog
Kein Seitentyp, sondern die Referenz: Motiv-Erklärung (9/3), Palette als fünf Felder, Typografie-Vergleich (7/5), Bausteine (5/7: CTAs und Formularfeld links, Bild mit Legende rechts), Rasterregeln im Flächenton-Band (3/9). Nicht ausliefern.

### 01 Startseite
Zweck: Erstkontakt über Empfehlung und Suche; Einstieg in die vier Leistungen, Vertrauen über Person.
Aufbau von oben:
1. **Kopf** — Wortmarke links, Haarlinie dehnend, Navigation rechts (Bauberatung, Baubetreuung, Fachwerk, Über mich, Kontakt in Akzent). `padding:30px 64px 22px`.
2. **Hero 7/5**, links Abschnittsmarke „Aufnahme 01 — Erstgespräch", h1 „Jede Begehung endet schriftlich.", Vorspann, sekundärer Absatz, CTA + „Rückruf am selben Tag"; rechts Foto 430 px hoch mit Legende. Kein Zentrieren, kein Badge.
3. **Leistungen auto/1fr** — vier Abschnitte mit Randziffern 02.1–02.4, Titel Spectral 30 px, Text 17 px, Textlink „Zur Bauberatung" usw.
4. **Randloses Bild** 400 px, Fassade.
5. **Zitat 4/8** auf Flächenton, links Adresse, rechts Zitat + Rolle + Absatz zu Inhaberführung.
6. **Ablauf 9/3** — vier Schritte in einer Zeile, getrennt durch Haarlinien (kein Kartenraster), rechts Einsatzgebiet-Notiz an vertikaler Linie.
7. **Footer** — Haarlinie oben, Marke links, Kontakt/Impressum/Datenschutz rechts.

### 02 Leistungsseite (Muster für Bauberatung, Baubetreuung, Fachwerk und Sanierung)
Kopf mit Seitenname in Akzent statt Navigation → Titelzeile 9/3 mit Brotkrume „Startseite / Bauberatung" → Einleitung 5/7 (Bild links 360 px, Text rechts) → Leistungsumfang auto/1fr, jede Zeile intern 5/7 (Begriff Spectral 22 px | Erläuterung Barlow 15 px) → Abschluss 3/9 auf Flächenton mit Satz und CTA → Footer. Für Baubetreuung und Fachwerk dieselbe Struktur mit eigenen Inhalten und gespiegeltem Bild (7/5).

### 05 Für Verwaltungen und Investoren
Sachlichste Seite. Hero 7/5 mit Preis-/Leistungstabelle rechts (vier Zeilen, Wert in Akzent) → zwei gleich starke Blöcke 6/6, getrennt durch vertikale Haarlinie (die einzige Stelle mit 6/6) → Anfrageblock 4/8 mit vierfeldigem Formular → Footer im Flächenton.

### 06 Über Jürgen Gehrke
Bild 5/7 randlos links (520 px, Porträt, `object-position:center 18%`), rechts Herkunftstext und Faktenliste als auto/1fr mit den Ziffern „seit 1998", „1 : 1", „Region" → Haltungsblock 3/9 auf Flächenton mit Zitat und Vergütungs-Aussage → Footer.

### 08 Kontakt und Anfrage
Hero 7/5: links Titel und Formular (2×2 Felder, dann ein breites Feld, dann sekundärer CTA + Antwortzeit); rechts Kontaktblock an Oberlinie und Foto 260 px → Einsatzgebiet 3/9 auf Flächenton mit Ortsliste (SEO-relevant) → Footer.
**Offen:** Telefonnummer und E-Mail sind Platzhalter („Telefon und E-Mail bitte ergänzen") und müssen vom Kunden geliefert werden.

### 10 Mobil (390 px)
Einspaltig, Außenrand 20 px, h1 34 px, Randziffern bleiben — sie stehen dann über dem Titel statt daneben. Kopf: Marke zweizeilig links, „Menü" in Akzent rechts. Leistungen als Haarlinienliste. Kontakt als Flächenton-Band am Fuß.

### Noch anzulegen (gleiche Muster, kein neues Layout nötig)
- **03 Baubetreuung**, **04 Fachwerk und Sanierung** → Muster 02, Bildseite gespiegelt.
- **07 Referenzen** → Muster 02, Leistungsliste ersetzt durch Objektliste: Randziffer = Jahr, 5/7 (Objekt/Ort | Maßnahme). Braucht echte Objektdaten und Fotos.
- **09 Impressum und Datenschutz** → einspaltig 9/3, Fließtext Barlow 15/1.85, Randziffern als Paragraphennummern.

## Interactions & Behavior
Bewusst minimal — die Seite ist ein Dokument, keine Anwendung.
- Navigation: harte Seitenwechsel, keine Übergangsanimationen.
- Hover: nur Farbwechsel auf Textton bzw. Flächenfüllung beim sekundären CTA, `transition: color 120ms linear, background-color 120ms linear`. Keine Bewegung, kein Skalieren, keine Einblende-Animationen beim Scrollen (`prefers-reduced-motion` wird damit ohnehin erfüllt).
- Mobiles Menü: Vollflächen-Overlay im Grundton, Einträge als Haarlinienliste in Spectral 26 px mit Randziffern, Schließen als „Zu" in Akzent. Kein Hamburger-Icon — das Wort „Menü".
- Anfrageformular: Pflichtfelder Name, Telefon oder E-Mail, Ort, Anlass. Validierung erst bei Absenden; Fehler als Textzeile unter dem Feld in Akzent, Feldlinie 2 px Akzent — keine roten Flächen, kein Icon. Erfolg: Seitenwechsel auf eine Bestätigungsseite mit Muster 02 (Randziffer „Aufnahme 02 — Eingang bestätigt"), nicht als Toast.
- Versand serverseitig (Mail an den Inhaber), Honeypot-Feld plus Zeitstempel-Prüfung statt Captcha. DSGVO-Hinweis mit Link auf Datenschutz als Checkbox-Zeile über dem Absenden-Button, in Barlow 13 px.

## State Management
Kein Client-State außer: mobiles Menü offen/zu, Formularwerte, Formularstatus (`idle | invalid | sending | sent | error`). Kein Store, kein Client-Routing nötig.

## SEO — muss erhalten bleiben und ausgebaut werden
Der bisherige Auftritt rankt regional; die Neuentwicklung darf keine Substanz verlieren.
- **URLs unverändert übernehmen.** Wo sich Pfade ändern, 301 auf die neue Adresse. Bestehende Seitentitel und Meta-Descriptions vom alten Stand übernehmen, nicht neu erfinden, dann behutsam schärfen.
- Ein `h1` pro Seite, Abschnittstitel als `h2`, Unterpunkte als `h3`. Die Ordnungsziffern sind `<span aria-hidden="true">` und dürfen keine Überschriften ersetzen.
- Ortsbezug im Text halten: Kreis Hohenlohe, Schwäbisch Hall, Neuenstein, Öhringen, Künzelsau, Waldenburg, Bretzfeld, Ilshofen, Langenburg. Die Ortsliste auf der Kontaktseite ist dafür der Träger.
- Leistungsbegriffe wörtlich: Bauberatung, Baubetreuung, Baubegleitung, Fachwerksanierung, Sanierungsberatung, Kaufberatung Immobilie, Bauherrenberatung.
- `LocalBusiness`-JSON-LD auf jeder Seite (`name`, `address`, `areaServed`, `telephone`, `founder`), `BreadcrumbList` auf Unterseiten, `Service` je Leistungsseite.
- Alle Bilder mit den vorhandenen, beschreibenden `alt`-Texten (siehe unten) übernehmen; Dateinamen beibehalten — sie enthalten Keywords. Als WebP mit JPEG-Fallback ausliefern, `width`/`height` gesetzt, `loading="lazy"` außer Hero.
- Sitemap, `robots.txt`, sprechende `lang="de"`, `canonical` je Seite.
- Zielwerte: LCP < 2,0 s auf Mobil. Erreichbar, da keine Skripte im kritischen Pfad — Schriften selbst hosten und `preload`en.

## Barrierefreiheit
Kontrast (gemessen): Textton auf Grundton 16,42:1, Akzent auf Grundton 7,10:1, Akzent auf Flächenton 6,00:1, Signalton auf Grundton 6,60:1, Platzhalter Textton 70 % auf Grundton 6,3:1 — alle über 4,5:1. Platzhalter- und Label-Deckung nie unter 70 % bzw. 60 % setzen; darunter fällt der Wert unter die Grenze. Fokus sichtbar: 2 px Akzent-Outline mit 2 px Offset, nie `outline: none`. Formularlabels echte `<label for>`. Ordnungsziffern dekorativ, `aria-hidden`.

## Assets
Alle Bilder liegen in `uploads/` und stammen vom Kunden (echte Objekte und Person — keine Stockfotografie):
| Datei | Verwendung | `alt` |
|---|---|---|
| `juergen-gehrke-beratung-fachwerk.png` | Hero Startseite, Hero Mobil | Jürgen Gehrke erklärt ein saniertes Fachwerkfenster |
| `baubetreuung-fachwerk-fassade.png` | randloses Band Startseite | Baubetreuung an einer Fachwerkfassade im Kreis Hohenlohe |
| `bauberatung-fachwerk-begehung.png` | Leistungsseite Bauberatung | Begehung eines Fachwerk-Innenraums vor dem Kauf |
| `bauberatung-begehung.jpg` | Kontaktseite, Bauteilkatalog | Ortsbegehung mit Aufmaß im Bestand |
| `juergen-gehrke.jpg` | Über-Seite, Porträt | Jürgen Gehrke, Inhaber der Gehrke Bauberatung und Betreuung |
| `logo-dark.png` | Wortmarke für dunkle Flächen; im aktuellen Entwurf wird die typografische Wortmarke in Barlow verwendet | Gehrke Bauberatung |

Fehlt für die Referenzenseite: Objektfotos plus Ort, Jahr, Maßnahme.

## Inhalt — Status
Die Texte in den Prototypen sind aus den bekannten Angaben zum Unternehmen formuliert und inhaltlich belastbar, aber **nicht der Originalwortlaut der Bestandsseite** — der lag beim Erstellen nicht vor (der Upload enthielt nur Bilder). Vor dem Livegang: Originaltexte der bestehenden Seite gegen die Entwurfstexte legen, bestehende Formulierungen und Keywords übernehmen. Ebenfalls offen: Telefon, E-Mail, vollständige Firmierung und Rechtsform, Honorarangaben, Referenzobjekte.

## Files
- `Gehrke Website Vorlage.dc.html` — die Vorlage: Bauteilkatalog (00), Startseite (01), Leistungsseite (02), Verwaltungen (05), Über (06), Kontakt (08), Mobil (10). Öffnet direkt im Browser.
- `Richtungen.dc.html` — die drei Entwurfsrunden und die gewählte Richtung 3a, als Begründungsspur. Nicht umsetzen, nur zum Verständnis.
- `uploads/` — die Bilder in Originalauflösung.
