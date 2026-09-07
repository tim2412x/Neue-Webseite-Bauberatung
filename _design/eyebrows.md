# Abarbeitungsliste: Versalzeilen ueber Ueberschriften

REDESIGN §3: **Ueber einer Ueberschrift steht nie eine zweite, kleinere Ueberschrift.**
Die Klassen `.section-eyebrow`, `.svc-hero-eyebrow` und `.eyebrow` verschwinden
restlos, ebenso die Farbe `#4A5D3C`.

Erzeugt mit `python3 _design/tools/eyebrows.py`. HTML-Kommentare sind
ausgenommen — abgeschaltete Bloecke werden nicht mitgezaehlt.
Beim Umbau Zeile fuer Zeile abarbeiten; `pruefung.py` meldet, was offen ist.

Die Ziffern sind eine durchgehende Nummerierung von oben nach unten. Wo ein
Abschnitt fachlich Unterpunkte hat (Leistungen der Startseite), darf daraus
`02.1`, `02.2` … werden — siehe `_design/muster.html`.

### `index.html` — 6 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Bauberatung & Baubetreuung · Schwäbisch Hall | `h1` Ihr Bauprojekt. Sicher und stressfrei von Anfang an. | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Leistungen | `h2` Was ich für Sie tue | Randziffer `01` | [ ] |
| 3 | Warum Gehrke Bauberatung | `h2` Der Unterschied liegt in der Unabhängigkeit | Randziffer `02` | [ ] |
| 4 | Kundenstimmen | `h2` Was Kunden sagen | Randziffer `03` | [ ] |
| 5 | Referenzen | `h2` Ein Projekt, das für sich spricht | Randziffer `04` | [ ] |
| 6 | Kontakt | `h2` Lassen Sie uns über Ihr Projekt sprechen | Randziffer `05` | [ ] |

### `bauberatung/index.html` — 10 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Bauberatung & Kaufberatung | `h1` Bauberatung & Kaufberatung in Schwäbisch Hall, Heilbronn & Hohenlohe | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Warum Bauberatung? | `h2` Die teuersten Fehler entstehen vor dem ersten Hammerschlag | Randziffer `01` | [ ] |
| 3 | Was ich für Sie prüfe | `h2` Bauberatung, die Klarheit schafft | Randziffer `02` | [ ] |
| 4 | Kaufberatung | `h2` Kaufen Sie das Haus — nicht das Risiko | Randziffer `03` | [ ] |
| 5 | So läuft es ab | `h2` In vier Schritten zur Klarheit | Randziffer `04` | [ ] |
| 6 | Der entscheidende Unterschied | `h2` Warum unabhängige Beratung? | Randziffer `05` | [ ] |
| 7 | Lohnt sich das? | `h2` Was kostet eine Bauberatung? | Randziffer `06` | [ ] |
| 8 | Häufige Fragen | `h2` Was Käufer & Bauherren oft wissen wollen | Randziffer `07` | [ ] |
| 9 | Weitere Leistungen | `h2` Vielleicht auch interessant | Randziffer `08` | [ ] |
| 10 | Kontakt | `h2` Unsicher bei Kauf oder Sanierung? Fragen Sie mich. | Randziffer `09` | [ ] |

### `baubetreuung/index.html` — 10 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Baubetreuung & Baubegleitung | `h1` Baubetreuung in Schwäbisch Hall, Heilbronn & Hohenlohe | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Warum überhaupt Baubetreuung? | `h2` Ein Bauprojekt verzeiht keine Fehler | Randziffer `01` | [ ] |
| 3 | Was ich für Sie übernehme | `h2` Die Aufgaben eines Baubetreuers | Randziffer `02` | [ ] |
| 4 | Für welches Projekt? | `h2` Neubau oder Sanierung — ich begleite beides | Randziffer `03` | [ ] |
| 5 | So läuft es ab | `h2` In vier Schritten an Ihrer Seite | Randziffer `04` | [ ] |
| 6 | Der entscheidende Unterschied | `h2` Warum unabhängige Baubetreuung? | Randziffer `05` | [ ] |
| 7 | Lohnt sich das? | `h2` Was kostet Baubetreuung — und was spart sie? | Randziffer `06` | [ ] |
| 8 | Häufige Fragen | `h2` Was Bauherren oft wissen wollen | Randziffer `07` | [ ] |
| 9 | Weitere Leistungen | `h2` Vielleicht auch interessant | Randziffer `08` | [ ] |
| 10 | Kontakt | `h2` Lassen Sie uns über Ihr Bauprojekt sprechen | Randziffer `09` | [ ] |

### `bauprojektmanagement/index.html` — 10 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Für Kommunen · Bauträger · Hausverwaltungen & WEGs | `h1` Bauprojektmanagement für Kommunen, Bauträger & Hausverwaltungen | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Die Realität bei Bauprojekten | `h2` Sie haben Ihr Kerngeschäft — kein Bauleiter | Randziffer `01` | [ ] |
| 3 | Was ich für Ihre Objekte übernehme | `h2` Technische Projektsteuerung von A bis Z | Randziffer `02` | [ ] |
| 4 | Doppelter Nutzen | `h2` Gut für Sie — gut für Ihr Projekt | Randziffer `03` | [ ] |
| 5 | So läuft die Zusammenarbeit | `h2` So arbeiten wir zusammen | Randziffer `04` | [ ] |
| 6 | Warum Auftraggeber mit mir arbeiten | `h2` Ein Partner, der Sie absichert | Randziffer `05` | [ ] |
| 7 | Was kostet das die Verwaltung? | `h2` Für Sie eine Entlastung — kein Kostenfaktor | Randziffer `06` | [ ] |
| 8 | Häufige Fragen | `h2` Was Verwaltungen & Beiräte oft fragen | Randziffer `07` | [ ] |
| 9 | Weitere Leistungen | `h2` Vielleicht auch interessant | Randziffer `08` | [ ] |
| 10 | Kontakt | `h2` Geben Sie Ihre Baustellen ab — nicht die Kontrolle | Randziffer `09` | [ ] |

### `denkmalsanierung/index.html` — 10 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Denkmal & Altbau · Beratung & Betreuung | `h1` Denkmal- & Altbausanierung: Beratung & Betreuung in Schwäbisch Hall, H | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Warum Denkmal & Altbau besonders sind | `h2` Bei alter Substanz ist das Risiko ein anderes | Randziffer `01` | [ ] |
| 3 | Was ich für Sie tue | `h2` Vom Fachwerk bis zur energetischen Sanierung | Randziffer `02` | [ ] |
| 4 | Zwei Seiten derselben Aufgabe | `h2` Denkmalgerecht erhalten — energetisch zukunftsfähig machen | Randziffer `03` | [ ] |
| 5 | So läuft es ab | `h2` In vier Schritten zur sicheren Sanierung | Randziffer `04` | [ ] |
| 6 | Warum gerade ich | `h2` Der Zimmermeister für historische Bauten | Randziffer `05` | [ ] |
| 7 | Was kostet das? | `h2` Bei Denkmal & Altbau zahlt sich Ehrlichkeit aus | Randziffer `06` | [ ] |
| 8 | Häufige Fragen | `h2` Denkmal, Altbau & energetische Sanierung | Randziffer `07` | [ ] |
| 9 | Weitere Leistungen | `h2` Vielleicht auch interessant | Randziffer `08` | [ ] |
| 10 | Kontakt | `h2` Denkmal oder Altbau? Reden wir, bevor Sie loslegen. | Randziffer `09` | [ ] |

### `ueber-juergen/index.html` — 7 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Zimmermeister · Baubetreuer · Persönlich vor Ort in der Region | `h1` Jürgen Gehrke — 30 Jahre Bau­praxis. Jetzt ausschließlich für Sie. | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Meine Geschichte | `h2` Vom Zimmermeister zum Baubetreuer | Randziffer `01` | [ ] |
| 3 | Werdegang | `h2` 30 Jahre Bauerfahrung auf einen Blick | Randziffer `02` | [ ] |
| 4 | Meine Werte | `h2` Was meine Arbeit ausmacht | Randziffer `03` | [ ] |
| 5 | Engagement & Netzwerk | `h2` Verwurzelt in der Region | Randziffer `04` | [ ] |
| 6 | Häufige Fragen | `h2` Was Bauherren oft fragen | Randziffer `05` | [ ] |
| 7 | Jetzt anfragen | `h2` Lernen wir uns kennen — das Erstgespräch ist kostenlos | Randziffer `06` | [ ] |

### `kontakt/index.html` — 3 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Kontakt | `h1` Kostenloses Erstgespräch vereinbaren | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Anfrage stellen | `h2` Schreiben Sie mir | Randziffer `01` | [ ] |
| 3 | Ablauf | `h2` So geht es weiter | Randziffer `02` | [ ] |

### `impressum/index.html` — 1 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Rechtliches | `h1` Impressum | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |

### `datenschutz/index.html` — 1 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Rechtliches | `h1` Datenschutzerklärung | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |

### `agb/index.html` — 1 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Rechtliches | `h1` Allgemeine Geschäftsbedingungen | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |

### `bauabnahme/index.html` — 10 Fundstellen

| # | Bisherige Versalzeile | Folgende Ueberschrift | Neu | erledigt |
|---|---|---|---|---|
| 1 | Bauabnahme & Mängelprotokoll | `h1` Bauabnahme in Schwäbisch Hall, Heilbronn & Hohenlohe | **ersatzlos weg** — Seitenname steht im Kopf (`.kopf-seitenname`) | [ ] |
| 2 | Warum die Abnahme so heikel ist | `h2` Der wichtigste Moment — und der riskanteste | Randziffer `01` | [ ] |
| 3 | Was ich für Sie tue | `h2` Ihre Abnahme — fachlich begleitet | Randziffer `02` | [ ] |
| 4 | Was auf dem Spiel steht | `h2` Die Tragweite der Abnahme — und wie ich Sie absichere | Randziffer `03` | [ ] |
| 5 | So läuft es ab | `h2` In vier Schritten sicher abgenommen | Randziffer `04` | [ ] |
| 6 | Der entscheidende Unterschied | `h2` Warum unabhängige Abnahme? | Randziffer `05` | [ ] |
| 7 | Was kostet das? | `h2` Eine der günstigsten Absicherungen am Bau | Randziffer `06` | [ ] |
| 8 | Häufige Fragen | `h2` Was Bauherren zur Abnahme fragen | Randziffer `07` | [ ] |
| 9 | Weitere Leistungen | `h2` Vielleicht auch interessant | Randziffer `08` | [ ] |
| 10 | Kontakt | `h2` Abnahmetermin in Sicht? Holen Sie mich dazu. | Randziffer `09` | [ ] |
