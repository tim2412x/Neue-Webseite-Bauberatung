# `_design/` — Arbeitsmaterial für das Redesign

Dieser Ordner wird **nicht ausgeliefert** (`robots.txt` sperrt ihn).
Er enthält alles, was für den Umbau gebraucht wird, und sonst nichts.

## Einstieg

Wer hier neu anfängt, liest in dieser Reihenfolge:

1. **`REDESIGN.md`** — der Style Guide vom Kunden. Verbindlich, gewinnt jeden Widerspruch.
2. **`../CLAUDE.md`** — das Regelwerk für dieses Repo.
3. **`UMBAU.md`** — der Arbeitsplan, Schritt für Schritt, mit allen bereits
   getroffenen Entscheidungen (D-1 bis D-6).

## Inhalt

| Pfad | Was |
|---|---|
| `REDESIGN.md` | Style Guide (Kopie von `~/Desktop/REDESIGN.md`) |
| `UMBAU.md` | Arbeitsplan, Seitenabbildung, Entscheidungen, Abnahme |
| `muster.html` | Bausteinkatalog — jeder Baustein aus `site.css` als kopierfähiges Markup |
| `eyebrows.md` | Abarbeitungsliste der 69 gestrichenen Versalzeilen |
| `inventar/*.md` | Der Bestandsinhalt je Seite, verbatim. **Die Textquelle.** |
| `referenz/` | Der Prototyp aus dem Kundenpaket. **Nur Inspiration, kein Code zum Kopieren.** |
| `tools/*.py`, `tools/*.sh` | Prüf- und Extraktionsskripte |

## Werkzeuge

Alle aus dem Projektwurzelverzeichnis aufrufen.

```bash
# Abnahmeprüfung aus REDESIGN §17. 0 Fehler = fertig.
python3 _design/tools/pruefung.py
python3 _design/tools/pruefung.py kontakt/index.html

# Inhaltsinventar neu erzeugen (nach Textänderungen im Bestand)
python3 _design/tools/extract_content.py

# Abarbeitungsliste der Versalzeilen neu erzeugen
python3 _design/tools/eyebrows.py

# Echte Pixelmaße aller Bilder — für width/height an jedem <img>
python3 _design/tools/bildmasse.py

# Spectral und Barlow als WOFF2 nach assets/fonts/ laden (einmalig, schon geschehen)
bash _design/tools/schriften_holen.sh
```

## Vorschau

```bash
python3 -m http.server 8787
```

Dann `http://localhost:8787/_design/muster.html` für den Bausteinkatalog,
`http://localhost:8787/` für die Seite.

## Was der Prototyp in `referenz/` falsch hat

Bewusst nicht übernehmen:

- Adresse „74632 Neuenstein" — richtig ist **Stauferstraße 122, 74523 Schwäbisch Hall**
- „Telefon und E-Mail bitte ergänzen" — beides ist vorhanden
- Alle Fließtexte — sie sind nachgebildet, nicht der Wortlaut des Bestands
- Alle Inline-Styles — sie sind Werkzeugzwang, nicht Vorgabe
- Die Abschnittsmarken („Aufnahme 01 — Erstgespräch") und die Farbe `#4A5D3C` —
  von REDESIGN §3 ersatzlos gestrichen
- Google Fonts — die Schriften werden selbst gehostet
- Die Randziffer über dem Titel auf Mobil — REDESIGN §11 verlangt sie **davor**
