# Redesign Gehrke Bauberatung und Betreuung

## 1. Auftrag

Der Webauftritt von Gehrke Bauberatung und Betreuung (Inhaber Jürgen Gehrke, Neuenstein, Kreis Hohenlohe) bekommt ein neues Design. **Der Inhalt bleibt.** Texte, Seitenstruktur, Adressen und Rankings sind vorhanden und belastbar — dieses Dokument beschreibt ausschließlich, wie die vorhandenen Inhalte künftig aussehen und ausgezeichnet werden.

Zielgruppen: private Bauherren zwischen 35 und 60 mit Sanierungs- oder Kaufvorhaben, Hausverwaltungen, Architekten, Immobilieninvestoren.
Wirkung: nüchtern, verlässlich, handwerklich, inhabergeführt. Ausdrücklich keine Agentur-Optik.

## 2. Technischer Rahmen

Der bestehende Unterbau bleibt unverändert: statische HTML-Dateien pro Seite, ein gemeinsames Stylesheet, kein Build-Schritt, kein Framework, kein Client-Routing. Kein Wechsel zu Astro, Eleventy oder Next.js.

- Ein zentrales Stylesheet mit Custom Properties und wenigen Klassen. Keine Inline-Styles im Ergebnis.
- Die Prototypen im Verzeichnis `design_handoff_gehrke_website/` arbeiten ausschließlich mit Inline-Styles, weil das Werkzeug es verlangt hat. Sie sind **visuelle Referenz, kein zu kopierender Code**.
- Schriften selbst hosten, keine Einbindung über Google Fonts.
- Reihenfolge der Arbeit: erst die bestehenden Seiten lesen und den vorhandenen Text, die Seitentitel, die Meta-Descriptions und die Adressen sichern, dann Markup und Stylesheet neu aufbauen, dann den gesicherten Text einsetzen. Die Texte in den Prototypen sind nachgebildet und dienen nur dort als Vorlage, wo im Bestand nichts Entsprechendes existiert.

## 3. Die eine harte Änderung gegenüber dem Prototyp

Im Prototyp steht über vielen Überschriften eine kleine, gesperrte Versalzeile in Barlow 11 Pixel — „Aufnahme 01 — Erstgespräch", „Aufnahme 03 — Der Berater", „Aufnahme 04 — Ablauf", „Haltung", „Nächster Schritt", „Anfrage mit Objektdaten", „Einsatzgebiet".

**Diese Abschnittsmarken entfallen vollständig und ersatzlos. Über einer Überschrift steht nie eine zweite, kleinere Überschrift.** Die Farbe `#4A5D3C` (Signalton) wird damit im gesamten Projekt nicht mehr verwendet.

Ersetzt wird nach diesen drei Regeln, damit kein Abschnitt nackt wirkt:

1. **Trug die Marke nur Ordnung** (Aufnahme-Nummerierung), wird sie zur reinen Randziffer in Spalte 1 des Abschnitts — Barlow 400, 13 Pixel, Sperrung `.16em`, Akzentfarbe, auf gleicher Grundlinie wie die erste Zeile des Inhalts.
2. **Trug sie eigene Information** („Haltung", „Anfrage mit Objektdaten", „Einsatzgebiet"), wird sie zur echten Überschrift in Spectral 400 nach der Skala in Abschnitt 7 — als `h2` oder `h3`, gemischte Groß- und Kleinschreibung, keine Sperrung.
3. **War sie reine Dekoration** (Hero-Zeilen wie „Aufnahme 01 — Erstgespräch"), fällt sie weg. Die Überschrift beginnt dann unmittelbar unter der Kopf-Haarlinie mit 64 Pixel Abstand.

Konkret pro Fundstelle:

| Seite | Bisherige Marke | Neu |
|---|---|---|
| Startseite, Hero | Aufnahme 01 — Erstgespräch | ersatzlos weg |
| Startseite, Zitatblock | Aufnahme 03 — Der Berater | Randziffer `03` |
| Startseite, Ablauf | Aufnahme 04 — Ablauf | Randziffer `04` |
| Leistungsseite, Abschluss | Nächster Schritt | ersatzlos weg, der Satz trägt sich selbst |
| Verwaltungen, Hero | Aufnahme 01 — Auftraggeber mit Bestand | ersatzlos weg |
| Verwaltungen, Formular | Anfrage mit Objektdaten | Überschrift Spectral 400, 30 Pixel |
| Über-Seite, Hero | Aufnahme 01 — Herkunft | ersatzlos weg |
| Über-Seite, Haltungsblock | Haltung | Überschrift Spectral 400, 30 Pixel |
| Kontakt, Hero | Aufnahme 01 — Anfrage | ersatzlos weg |
| Kontakt, Ortsliste | Einsatzgebiet | Überschrift Spectral 400, 26 Pixel |

Nicht betroffen und bleiben unverändert: die Wortmarke im Kopf, die Navigation, die Bildlegenden unter den Fotos, die Labels über Formularfeldern, die Schrittziffern im Ablauf und die Randziffern selbst. Diese Elemente stehen nie über einer Überschrift.

## 4. Gestaltungsmotiv

**Aufnahme — Randziffern an einer durchlaufenden Protokolllinie.**

Jede Seite ist als Protokoll gedacht. Jeder Abschnitt trägt links außen eine Ordnungsziffer (`01`, `02.1`, `Schritt 1`, `seit 1998`) in Barlow, klein und gesperrt, in Akzentfarbe. Abschnitte werden von einer Haarlinie über die volle Satzbreite eingefasst, Zeilen innerhalb eines Abschnitts von einer Haarlinie mit 20 Prozent Deckung. Ziffer und Linie sind die einzige Dekoration der Seite. Keine Karten, keine Symbole, keine Schmuckelemente.

Aufbau eines Abschnitts:

```html
<section class="abschnitt">
  <span class="ziffer" aria-hidden="true">02.1</span>
  <div class="inhalt">
    <h2>Beratung vor dem Kauf</h2>
    <p>…</p>
  </div>
</section>
```

```css
.abschnitt{display:grid;grid-template-columns:auto 1fr;column-gap:var(--spalte-gap)}
.inhalt{border-bottom:1px solid var(--linie-fein);padding-bottom:28px}
```

Der erste Abschnitt einer Gruppe wird von einer Linie mit voller Deckung eröffnet, der letzte von einer Linie mit voller Deckung geschlossen.

## 5. Ausschlussliste

1. Keine der Schriften Inter, Geist, Roboto, Open Sans, `system-ui`.
2. Keine Farbverläufe, keinerlei.
3. Kein Verlaufstext, keine Leucht- oder Textschatteneffekte.
4. `border-radius: 0` ausnahmslos.
5. Kein `box-shadow`, kein `backdrop-filter`, kein Milchglas.
6. Kein zentrierter Hero, keine Auszeichnungsmarke über der Überschrift, keine kleine Versalzeile über einer Überschrift (siehe Abschnitt 3).
7. Keine Symbole in runden Kacheln, keine Symbolsätze.
8. Kein symmetrisches Merkmalsraster aus drei gleichen Spalten.
9. Kein dunkler Handlungsaufforderungs-Block als vorletzter Abschnitt.
10. Keine Emojis, keine Stockfotografie. Nur die echten Fotos aus `uploads/`.

## 6. Farben

Genau fünf Werte, keine Zwischenstufen erfinden. Der Signalton entfällt mit den Abschnittsmarken und wird nicht ersetzt.

| Rolle | Hex | Verwendung |
|---|---|---|
| Grundton | `#F7F5F0` | Seitenhintergrund, Text auf dunklen Flächen |
| Flächenton | `#E8E2D6` | abgesetzte Abschnitte, Fußband |
| Textton | `#17171A` | Text, Linien, Rahmen |
| Akzent | `#8A3B12` | Randziffern, Links, primäre Handlungsaufforderung |

Erlaubte Transparenzen, jeweils auf Textton: `rgba(23,23,26,.2)` Zeilentrenner, `.78` und `.8` sekundärer Fließtext, `.7` Bildlegenden, `.6` Formular-Labels, `.7` Platzhalter. Die Werte für Platzhalter und Labels sind Kontrastuntergrenzen und dürfen nicht schwächer gesetzt werden. Sonst nichts.

```css
:root{
  --grund:#F7F5F0; --flaeche:#E8E2D6; --text:#17171A; --akzent:#8A3B12;
  --linie:#17171A; --linie-fein:rgba(23,23,26,.2);
  --rand:64px; --spalte-gap:56px; --radius:0;
}
```

## 7. Schrift

Genau zwei Familien, beide unter der SIL Open Font License, beide selbst gehostet.

- **Spectral** (Serif) trägt den Inhalt: Seitentitel, Abschnittstitel, Fließtext, Zitate. Schnitte 300, 400 und 300 kursiv.
- **Barlow** (Grotesk) trägt nur die Ordnung: Randziffern, Navigation, Wortmarke, Legenden, Tabellen, Formulare. Schnitte 400 und 500.

Auslieferung als WOFF2 in `/fonts`, `@font-face` mit `font-display: swap`, Teilmengen latin und latin-ext, `preload` für Spectral 300 und Barlow 500.

| Rolle | Familie | Größe / Zeilenhöhe | Weiteres |
|---|---|---|---|
| Seitentitel `h1` | Spectral 300 | 54 / 1.14 | `letter-spacing:-.01em`, `max-width:24–26ch` |
| Seitentitel Über-Seite | Spectral 300 | 48 / 1.14 | |
| Abschnittstitel `h2` | Spectral 400 | 30 / 1.2 | |
| Untertitel `h3` | Spectral 400 | 26 / 1.25 | |
| Listentitel | Spectral 300 | 22 / 1.35 | |
| Vorspann | Spectral 300 | 19 / 1.8 | `max-width:56ch` |
| Fließtext Serif | Spectral 300 | 17–18 / 1.75–1.8 | `max-width:70ch` |
| Fließtext Grotesk | Barlow 400 | 15 / 1.75–1.85 | sekundär, Aufzählungen, Tabellen |
| Zitat | Spectral 300 kursiv | 32–34 / 1.4 | `max-width:34–36ch` |
| Randziffer | Barlow 400 | 13 / 1 | `letter-spacing:.16em`, Akzent |
| Navigation | Barlow 400 | 12 / 1 | `letter-spacing:.16em`, Versalien |
| Wortmarke | Barlow 500 | 12 / 1 | `letter-spacing:.28em`, Versalien |
| Bildlegende | Barlow 400 | 12 / 1.5 | `letter-spacing:.1em`, Versalien, Textton 70 Prozent |
| Label Handlungsaufforderung | Barlow 500 | 12–13 / 1 | `letter-spacing:.18–.2em`, Versalien |

Versalien nur bis 13 Pixel. Keine Schriftgröße unter 11 Pixel.

## 8. Raster und Rhythmus

- Satzspiegel 1180 Pixel, Außenrand 64 Pixel, Zwölfspalter, `column-gap: 56px`.
- Abstand zwischen Abschnitten 96 bis 104 Pixel, innerhalb eines Abschnitts 26 bis 34 Pixel, Zeilenpolster 24 bis 34 Pixel.
- Erlaubte Spaltenverhältnisse: `7fr 5fr`, `5fr 7fr`, `9fr 3fr`, `3fr 9fr`, `4fr 8fr`, `6fr 6fr`, `auto 1fr`. Drei gleiche Spalten sind verboten.
- **Asymmetrieregel:** auf jeder Seite tragen mindestens drei Abschnitte ein anderes Verhältnis als die übrigen.
- Bilder laufen randlos über die volle Breite oder exakt spaltenbreit, `object-fit: cover`, feste Höhen, keine Rundungen, keine Rahmen, kein Text über dem Foto.

## 9. Bausteine und Zustände

- **Link und primäre Handlungsaufforderung:** Akzent, `border-bottom:1px solid` in Akzent, `padding-bottom:7px`. Beim Überfahren wechseln Schrift und Linie auf Textton.
- **Sekundäre Handlungsaufforderung:** `1px solid` Textton, `padding:12–14px 20–24px`, Radius 0. Beim Überfahren Fläche Textton, Schrift Grundton.
- **Formularfeld:** nur `border-bottom:1px solid` Textton. Label darüber in Barlow 500, 11 Pixel, Versalien. Platzhalter Textton 70 Prozent. Im Fokus Linie 2 Pixel Akzent, kein Schein, kein Ring.
- **Navigation:** aktiver Eintrag in Akzent, inaktiver in Textton.
- Übergänge ausschließlich `transition: color 120ms linear, background-color 120ms linear`. Keine Bewegung, keine Skalierung, keine Einblendungen beim Scrollen.

## 10. Seiten

Die Nummern verweisen auf `data-screen-label` in `Gehrke Website Vorlage.dc.html`. Der dortige Bauteilkatalog (00) ist reine Referenz und wird nicht ausgeliefert.

### Startseite (01)

1. **Kopf** — Wortmarke links, dehnende Haarlinie, Navigation rechts (Bauberatung, Baubetreuung, Fachwerk, Über mich, Kontakt in Akzent), `padding:30px 64px 22px`.
2. **Hero 7/5** — links `h1`, Vorspann, sekundärer Absatz, Handlungsaufforderung mit dem Zusatz „Rückruf am selben Tag"; rechts Foto 430 Pixel hoch mit Legende. Keine Marke darüber.
3. **Leistungen `auto`/`1fr`** — vier Abschnitte mit den Randziffern 02.1 bis 02.4, Titel Spectral 30 Pixel, Text 17 Pixel, Textlink je Leistung.
4. **Randloses Bild** 400 Pixel hoch, Fachwerkfassade.
5. **Zitatblock 4/8** auf Flächenton — links Randziffer `03` und Adresse, rechts Zitat, Rolle und Absatz zur Inhaberführung.
6. **Ablauf 9/3** — Randziffer `04`, vier Schritte in einer Zeile durch Haarlinien getrennt, kein Kartenraster; rechts die Einsatzgebiet-Notiz an einer senkrechten Linie.
7. **Fuß** — Haarlinie oben, Marke links, Kontakt, Impressum und Datenschutz rechts.

### Leistungsseiten (02 bis 04): Bauberatung, Baubetreuung, Fachwerk und Sanierung

Ein Muster für alle drei. Kopf mit Seitenname in Akzent statt Navigation → Titelzeile 9/3 mit Brotkrume „Startseite / Bauberatung" → Einleitung 5/7 (Bild links 360 Pixel, Text rechts) → Leistungsumfang `auto`/`1fr`, jede Zeile intern 5/7 (Begriff in Spectral 22 Pixel, Erläuterung in Barlow 15 Pixel) → Abschlussblock 3/9 auf Flächenton mit Satz und Handlungsaufforderung → Fuß. Bei Baubetreuung und Fachwerk das Bild spiegeln (7/5).

### Verwaltungen und Investoren (05)

Sachlichste Seite. Hero 7/5 mit Leistungs- und Preistabelle rechts (vier Zeilen, Wert in Akzent) → zwei gleich starke Blöcke 6/6, getrennt durch eine senkrechte Haarlinie, die einzige Stelle mit 6/6 → Anfrageblock 4/8 mit vier Feldern unter einer echten Überschrift → Fuß auf Flächenton.

### Über Jürgen Gehrke (06)

Bild 5/7 randlos links, 520 Pixel, Porträt mit `object-position:center 18%`; rechts Herkunftstext und Faktenliste als `auto`/`1fr` mit den Randziffern „seit 1998", „1 : 1", „Region" → Haltungsblock 3/9 auf Flächenton unter echter Überschrift, mit Zitat und Aussage zur Vergütung → Fuß.

### Referenzen (07)

Muster der Leistungsseite, Leistungsliste ersetzt durch Objektliste: Randziffer ist das Jahr, Zeile intern 5/7 (Objekt und Ort, Maßnahme). Nur anlegen, wenn echte Objektdaten und Fotos vorliegen, sonst als Gerüst mit sichtbarem Platzhalterhinweis und ohne Verlinkung in der Navigation.

### Kontakt und Anfrage (08)

Hero 7/5 — links Titel und Formular (zweimal zwei Felder, dann ein breites Feld, dann sekundäre Handlungsaufforderung mit Antwortzeit); rechts Kontaktblock an der Oberlinie und Foto 260 Pixel → Ortsliste 3/9 auf Flächenton unter echter Überschrift → Fuß.

### Impressum und Datenschutz (09)

Einspaltig 9/3, Fließtext Barlow 15 / 1.85, Randziffern als Paragraphennummern. Rechtstexte unverändert aus dem Bestand übernehmen.

## 11. Mobil (390 Pixel)

- Einspaltig, Außenrand 20 Pixel, `h1` 34 Pixel.
- **Die Randziffer steht in derselben Zeile vor dem Titel, niemals darüber.** Umsetzung ohne zweites Markup: `.abschnitt{display:block}` und `.ziffer{float:left;margin-right:12px}`. Die erste Zeile der Überschrift beginnt damit rechts neben der Ziffer, Folgezeilen laufen über die volle Breite.
- Kopf: Marke zweizeilig links, „Menü" in Akzent rechts.
- Leistungen als Haarlinienliste, Kontakt als Band im Flächenton am Fuß.

## 12. Verhalten

Die Seite ist ein Dokument, keine Anwendung. Client-Zustand nur: mobiles Menü offen oder zu, Formularwerte, Formularstatus (`idle | invalid | sending | sent | error`). Kein Store, kein Client-Routing.

- Navigation: harte Seitenwechsel, keine Übergänge.
- Mobiles Menü: vollflächige Überlagerung im Grundton, Einträge als Haarlinienliste in Spectral 26 Pixel mit Randziffern, Schließen als Wort „Zu" in Akzent. Kein Hamburger-Symbol, sondern das Wort „Menü".
- Anfrageformular: Pflichtfelder Name, Telefon oder E-Mail, Ort, Anlass. Prüfung erst beim Absenden. Fehler als Textzeile unter dem Feld in Akzent und Feldlinie 2 Pixel Akzent, keine roten Flächen, kein Symbol. Erfolg als Wechsel auf eine Bestätigungsseite im Muster der Leistungsseite, nicht als Einblendung.
- Versand serverseitig als Mail an den Inhaber, Honigtopf-Feld und Zeitstempelprüfung statt Captcha. Hinweis zur Datenschutz-Grundverordnung mit Link auf die Datenschutzseite als Zeile mit Kontrollkästchen über dem Absenden-Knopf, Barlow 13 Pixel.

## 13. Suchmaschinenoptimierung

Der Bestand rankt regional. Das Redesign darf keine Substanz verlieren.

- **Adressen unverändert übernehmen.** Wo sich ein Pfad ändert, dauerhafte Weiterleitung (301) auf die neue Adresse.
- Bestehende Seitentitel und Meta-Descriptions übernehmen, nicht neu erfinden, danach behutsam schärfen.
- Ein `h1` pro Seite, Abschnittstitel als `h2`, Unterpunkte als `h3`. Die Randziffern sind `<span aria-hidden="true">` und ersetzen keine Überschrift. Die gestrichenen Abschnittsmarken waren nie Überschriften — durch ihren Wegfall darf keine Ebene verlorengehen.
- Ortsbezug im Text halten: Kreis Hohenlohe, Schwäbisch Hall, Neuenstein, Öhringen, Künzelsau, Waldenburg, Bretzfeld, Ilshofen, Langenburg. Träger ist die Ortsliste auf der Kontaktseite.
- Leistungsbegriffe wörtlich: Bauberatung, Baubetreuung, Baubegleitung, Fachwerksanierung, Sanierungsberatung, Kaufberatung Immobilie, Bauherrenberatung.
- Strukturierte Daten als JSON-LD: `LocalBusiness` auf jeder Seite mit `name`, `address`, `areaServed`, `telephone`, `founder`; `BreadcrumbList` auf Unterseiten; `Service` je Leistungsseite.
- Bilder mit den vorhandenen beschreibenden `alt`-Texten und den bestehenden Dateinamen ausliefern, sie enthalten Suchbegriffe. WebP mit JPEG-Rückfall, `width` und `height` gesetzt, `loading="lazy"` außer im Hero.
- Sitemap, `robots.txt`, `lang="de"`, `canonical` je Seite.
- Zielwert: Largest Contentful Paint unter 2,0 Sekunden auf dem Mobilgerät. Erreichbar, da kein Skript im kritischen Pfad liegt und die Schriften selbst gehostet und vorgeladen werden.

## 14. Barrierefreiheit

Gemessene Kontraste: Textton auf Grundton 16,42 zu 1, Akzent auf Grundton 7,10 zu 1, Akzent auf Flächenton 6,00 zu 1, Platzhalter mit 70 Prozent Textton auf Grundton 6,3 zu 1. Alle über der Grenze von 4,5 zu 1. Deckung von Platzhaltern nie unter 70 Prozent, von Labels nie unter 60 Prozent.

Fokus immer sichtbar: 2 Pixel Akzent-Umriss mit 2 Pixel Abstand, niemals `outline: none`. Formularlabels als echte `<label for>`. Randziffern dekorativ und `aria-hidden`.

## 15. Bilder

Alle Dateien liegen in `uploads/` und stammen vom Kunden. Keine Stockfotografie.

| Datei | Verwendung | `alt` |
|---|---|---|
| `juergen-gehrke-beratung-fachwerk.png` | Hero Startseite und Mobil | Jürgen Gehrke erklärt ein saniertes Fachwerkfenster |
| `baubetreuung-fachwerk-fassade.png` | randloses Band Startseite | Baubetreuung an einer Fachwerkfassade im Kreis Hohenlohe |
| `bauberatung-fachwerk-begehung.png` | Leistungsseite Bauberatung | Begehung eines Fachwerk-Innenraums vor dem Kauf |
| `bauberatung-begehung.jpg` | Kontaktseite | Ortsbegehung mit Aufmaß im Bestand |
| `juergen-gehrke.jpg` | Über-Seite, Porträt | Jürgen Gehrke, Inhaber der Gehrke Bauberatung und Betreuung |
| `logo-dark.png` | Wortmarke auf dunklen Flächen; im Entwurf wird die typografische Wortmarke in Barlow verwendet | Gehrke Bauberatung |

Für die Referenzenseite fehlen Objektfotos samt Ort, Jahr und Maßnahme.

## 16. Offene Punkte

Vom Kunden zu liefern, bis dahin als sichtbarer Platzhalter im Markup und nicht als erfundener Wert:

1. Telefonnummer und E-Mail-Adresse für Kontaktseite, Fuß und `LocalBusiness`-Daten.
2. Vollständige Firmierung und Rechtsform für Impressum und strukturierte Daten.
3. Honorarangaben für die Tabelle auf der Seite für Verwaltungen und Investoren.
4. Referenzobjekte mit Fotos, Ort, Jahr und Maßnahme.

## 17. Abnahmeprüfung

- [ ] Keine kleine Versalzeile über irgendeiner Überschrift, auf keiner Seite, auch nicht auf Mobil.
- [ ] Die Farbe `#4A5D3C` kommt im Stylesheet nicht mehr vor.
- [ ] Jede Seite hat genau ein `h1`, die Überschriftenebenen sind lückenlos.
- [ ] Kein `border-radius`, kein `box-shadow`, kein Farbverlauf, keine der verbotenen Schriften im Stylesheet.
- [ ] Auf jeder Seite tragen mindestens drei Abschnitte ein abweichendes Spaltenverhältnis, nirgends drei gleiche Spalten.
- [ ] Randziffern sind `aria-hidden` und stehen auf Mobil vor, nie über dem Titel.
- [ ] Alle Adressen des Bestands sind erreichbar oder dauerhaft weitergeleitet, Titel und Meta-Descriptions übernommen.
- [ ] Schriften lokal eingebunden, kein Aufruf externer Domains.
- [ ] Tastaturbedienung vollständig, Fokus überall sichtbar.
- [ ] Largest Contentful Paint unter 2,0 Sekunden auf dem Mobilgerät.
