# CLAUDE.md — Gehrke Bauberatung Website

Diese Datei ist das verbindliche Regelwerk für alle Änderungen an der Website.
**Jede neue Session beginnt damit, diese Datei zu lesen.**

---

## Projektübersicht

- **Kunde:** Gehrke Bauberatung und -betreuung UG
- **Inhaber:** Jürgen Gehrke, Zimmermannsmeister
- **Domain:** https://gehrkebauberatung.de
- **Technologie:** Reines HTML/CSS/JS — kein Framework, kein Build-Tool
- **Hosting:** GitHub Pages
- **Repo:** [GitHub-URL eintragen]
- **Ziel:** Conversion, lokales SEO, Vertrauen durch Persönlichkeit

---

## Seitenstruktur

```
/                          → index.html                    (Startseite / Landing Page)
/ueber-juergen/            → ueber-juergen/index.html
/baubetreuung/             → baubetreuung/index.html
/bauberatung/              → bauberatung/index.html
/bauprojektmanagement/     → bauprojektmanagement/index.html (Kommunen, Bauträger, WEGs)
/denkmalsanierung/         → denkmalsanierung/index.html
/referenzen/               → referenzen/index.html
/kontakt/                  → kontakt/index.html
/impressum/                → impressum/index.html
/datenschutz/              → datenschutz/index.html
/agb/                      → agb/index.html
/hausverwaltung/           → hausverwaltung/index.html      (Redirect → /bauprojektmanagement/)
```

**HINWEIS:** `/bauabnahme/` wurde als Produkt entfernt. Die Seite existiert noch als Datei, ist aber nirgends verlinkt und nicht im Sitemap.

Jede neue Seite = eigener Ordner mit `index.html` darin.
Verlinkungen immer mit trailing slash: `href="/baubetreuung/"`.

---

## Asset-Struktur

Alle Bilder, Logos und Dokumente liegen in `/assets/`:

```
/assets/
  juergen-gehrke.jpg           ← Portrait (Jürgen mit Kappe)
  juergen-gehrke-beratung.jpg  ← Jürgen zeigt auf Fenster (Innenaufnahme)
  juergen-gehrke-aussen.jpg    ← Jürgen vor Fachwerkhaus (Außenaufnahme)
  juergen-gehrke-dach.jpg      ← Jürgen zeigt auf Deckenbalken
  bauplan-tablet.jpg           ← Baupläne auf Tisch mit Haftnotizen
  projektplanung.jpg           ← Hände über Bauplänen
  logo-dark.png                ← Logo weiß auf Navy (#0d1c2a)
  logo-light.png               ← Logo schwarz auf weiß
  logo-small.png               ← Kleines Logo für Nav / Favicon
  referenz-anbau.jpg           ← Fachwerkhaus + moderner Anbau
  referenz-poolhaus.jpg        ← Poolhaus innen mit Holzkonstruktion
  partner-drechsler.jpg
  partner-burk.jpg
  partner-strecker.jpg
  partner-podstawek.jpg
  partner-augsten.jpg
```

**Neue Bilder** immer in `/assets/` ablegen, Dateiname lowercase mit Bindestrichen.
Bilder nie in Unterordner — alle flat in `/assets/`.

---

## Design-System (VERBINDLICH — nie abweichen)

### Farben (CSS Custom Properties)

```css
:root {
  --navy:        #0d1c2a;   /* Primärhintergrund dunkel */
  --navy-mid:    #162534;   /* Dropdown, Karten auf Navy */
  --navy-light:  #1e3347;   /* Hover-Zustände auf Navy */
  --cream:       #f4efe6;   /* Karten-Hintergrund, Zitat-Boxen */
  --warm-white:  #f9f6f1;   /* Haupt-Seiten-Hintergrund */
  --stone:       #857d70;   /* Sekundäre Icons, dekorative Elemente */
  --stone-light: #c4bbb0;   /* Borders auf hellen Flächen */
  --accent:      #b8763a;   /* Primäre Akzentfarbe (Bronze/Amber) */
  --accent-h:    #c4854a;   /* Hover-State des Akzents */
  --text:        #18140f;   /* Primärer Body-Text */
  --text-mid:    #46403a;   /* Sekundärer Text, Fließtext */
  --serif: 'Libre Baskerville', Georgia, serif;
  --sans:  'Inter', system-ui, sans-serif;
}
```

**Wichtig:** `--accent` (#b8763a) ist IMMER die Akzentfarbe. Nie durch Blau, Grün o.ä. ersetzen.

### Typografie

| Verwendung | Font | Größe | Gewicht |
|---|---|---|---|
| Section-Überschriften (h2) | Libre Baskerville | clamp(26px, 3vw, 38px) | 400 |
| Karten-Titel (h3/h4) | Libre Baskerville | 18px | 400 |
| Body-Text | Inter | 14–15px | 300 |
| Eyebrow-Labels | Inter | 11px | 500, uppercase, 0.18em spacing |
| Nav-Links | Inter | 13px | 400 |
| Zahlen / KPIs | Inter | 28px+ | 600 |

**Regel:** Serif (Libre Baskerville) für emotionale / vertrauensbildende Überschriften.
Sans (Inter) für alles Funktionale (Nav, Labels, Body, Buttons).

### Font-Einbindung (immer im `<head>`)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Abstände & Layout

- Section-Padding: `padding: 88px 10vw`
- Nav-Höhe: `64px` (fixed)
- Body-Padding-Top immer `64px` (wegen fixed Nav)
- Gap für Grids: `24px` (Karten), `64px` (große Layouts)
- Border-Radius: Keiner — alle Ecken sind **sharp** (0px). Das ist Absicht.
- Buttons: Keine Rundungen, keine Schatten — flat und direkt

### Buttons

```html
<!-- Primär (Akzent) -->
<a href="..." class="btn-primary">Jetzt anfragen</a>

<!-- Sekundär (Ghost auf Navy) -->
<a href="..." class="btn-ghost">Mehr erfahren</a>

<!-- WhatsApp -->
<a href="https://wa.me/491727410650" class="btn-whatsapp">...</a>
```

```css
.btn-primary {
  background: var(--accent); color: #fff;
  padding: 14px 28px; font-size: 14px; font-weight: 500;
  font-family: var(--sans); text-decoration: none;
  transition: background 0.2s; display: inline-block;
}
.btn-primary:hover { background: var(--accent-h); }
.btn-ghost {
  border: 1px solid rgba(255,255,255,0.3); color: rgba(255,255,255,0.75);
  padding: 13px 27px; font-size: 13px; font-weight: 400;
  font-family: var(--sans); text-decoration: none;
  transition: border-color 0.2s, color 0.2s; display: inline-block;
}
.btn-ghost:hover { border-color: rgba(255,255,255,0.7); color: #fff; }
```

---

## Navigation (identisch auf allen Seiten)

Die Nav ist **immer fixed, immer Navy, immer dieselbe Struktur**.
Aktive Seite: `class="active"` am entsprechenden `<a>`-Tag → zeigt orangen Unterstrich.

```html
<nav>
  <div class="nav-logo">
    <a href="/"><img src="/assets/logo-dark.png" alt="Gehrke Bauberatung" height="44"></a>
  </div>
  <ul class="nav-links">
    <li><a href="/" [class="active"]>Start</a></li>
    <li>
      <a href="/baubetreuung/">Leistungen <span class="nav-chevron">▾</span></a>
      <div class="nav-dropdown">
        <a href="/baubetreuung/">Baubetreuung</a>
        <a href="/bauberatung/">Bauberatung</a>
        <a href="/bauprojektmanagement/">Bauprojektmanagement</a>
        <a href="/denkmalsanierung/">Betreuung Denkmalsanierung</a>
      </div>
    </li>
    <li><a href="/ueber-juergen/" [class="active"]>Über mich</a></li>
    <li><a href="/referenzen/">Referenzen</a></li>
    <li><a href="/kontakt/">Kontakt</a></li>
  </ul>
  <a href="/kontakt/" class="nav-cta">Kostenloses Erstgespräch</a>
  <button class="nav-burger" onclick="toggleMobile()" aria-label="Menü öffnen">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-mobile-menu" id="mobileMenu">
  <a href="/">Start</a>
  <a href="/baubetreuung/">Leistungen</a>
  <a class="indent" href="/baubetreuung/">↳ Baubetreuung</a>
  <a class="indent" href="/bauberatung/">↳ Bauberatung</a>
  <a class="indent" href="/bauprojektmanagement/">↳ Bauprojektmanagement</a>
  <a class="indent" href="/denkmalsanierung/">↳ Betreuung Denkmalsanierung</a>
  <a href="/ueber-juergen/">Über mich</a>
  <a href="/referenzen/">Referenzen</a>
  <a href="/kontakt/">Kontakt →</a>
</div>
```

Nav-JavaScript (identisch auf allen Seiten, ans Ende vor `</body>`):
```html
<script>
function toggleMobile() {
  document.getElementById('mobileMenu').classList.toggle('open');
}
document.addEventListener('click', function(e) {
  const m = document.getElementById('mobileMenu');
  if (m.classList.contains('open') && !m.contains(e.target) && !e.target.closest('.nav-burger')) {
    m.classList.remove('open');
  }
});
</script>
```

---

## Footer (identisch auf allen Seiten)

```html
<footer>
  <div class="footer-grid">
    <div class="footer-logo">
      <img src="/assets/logo-dark.png" alt="Gehrke Bauberatung">
      <p>Unabhängige Bauberatung &amp;<br>Baubetreuung in der Region<br>Schwäbisch Hall.</p>
    </div>
    <div class="footer-col">
      <h5>Leistungen</h5>
      <a href="/baubetreuung/">Baubetreuung</a>
      <a href="/bauberatung/">Bauberatung</a>
      <a href="/bauprojektmanagement/">Bauprojektmanagement</a>
      <a href="/denkmalsanierung/">Betreuung Denkmalsanierung</a>
    </div>
    <div class="footer-col">
      <h5>Unternehmen</h5>
      <a href="/ueber-juergen/">Über mich</a>
      <a href="/referenzen/">Referenzen</a>
      <a href="/kontakt/">Kontakt</a>
      <address>Stauferstraße 122<br>74523 Schwäbisch Hall</address>
    </div>
  </div>
  <div class="footer-bottom">
    <p>© 2026 Gehrke Bauberatung und -betreuung UG</p>
    <div class="footer-legal">
      <a href="/impressum/">Impressum</a>
      <a href="/datenschutz/">Datenschutz</a>
    </div>
  </div>
</footer>
```

---

## SEO-Regeln (PFLICHT für jede Seite)

### Meta-Tags Template

Jede Seite braucht **alle** dieser Tags, angepasst auf den Inhalt:

```html
<title>[Seitenspezifisch] | Gehrke Bauberatung</title>
<meta name="description" content="[150–160 Zeichen. Lokale Keywords + Mehrwert. Kein Keyword-Stuffing.]">
<link rel="canonical" href="https://gehrkebauberatung.de/[pfad]/">
<meta name="theme-color" content="#0d1c2a">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Jürgen Gehrke">
<meta name="geo.region" content="DE-BW">
<meta name="geo.placename" content="Schwäbisch Hall">

<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="Gehrke Bauberatung">
<meta property="og:url" content="https://gehrkebauberatung.de/[pfad]/">
<meta property="og:title" content="[Gleich wie <title>, ohne Suffix]">
<meta property="og:description" content="[Gleich wie meta description]">
<meta property="og:image" content="https://gehrkebauberatung.de/assets/juergen-gehrke.jpg">
<meta property="og:image:alt" content="Jürgen Gehrke, Bauberater aus Schwäbisch Hall">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Gleich wie og:title]">
<meta name="twitter:description" content="[Gleich wie og:description]">
<meta name="twitter:image" content="https://gehrkebauberatung.de/assets/juergen-gehrke.jpg">
```

### Structured Data (JSON-LD)

**Jede Seite** braucht das `ProfessionalService`-Schema als Basis.
**Leistungsseiten** bekommen zusätzlich `Service`-Schema.
**FAQ-Abschnitte** bekommen `FAQPage`-Schema.
**Über-Mich-Seite** bekommt `Person`-Schema.

Das vollständige `ProfessionalService`-Schema aus `index.html` / `ueber-juergen/index.html` als Vorlage verwenden.

### Heading-Hierarchie

```
H1: Einmal pro Seite. Enthält Primär-Keyword + Ortsname wenn möglich.
H2: Abschnittsüberschriften (section-headline Klasse).
H3/H4: Karten, Unterpunkte, FAQ-Fragen.
```

Beispiele für gute H1:
- Startseite: "Unabhängige Bauberatung in Schwäbisch Hall"
- Baubetreuung: "Baubetreuung in Schwäbisch Hall & Heilbronn"
- Bauabnahme: "Professionelle Bauabnahme — Mängel erkennen, bevor Sie zahlen"

### Lokale Keywords (immer einbauen wo relevant)

Primär: Schwäbisch Hall, Heilbronn, Hohenlohe, Crailsheim
Sekundär: Landkreis Schwäbisch Hall, Baden-Württemberg, Franken
Services: Baubetreuung, Bauberatung, Bauabnahme, Baugutachter, Baubetreuer

### Bilder (SEO)

Jedes `<img>` braucht:
- `alt`-Attribut mit beschreibendem Text (keine Dateinamen!)
- `loading="lazy"` außer Hero-Bilder (diese: `loading="eager"`)
- `width` und `height` Attribute (Core Web Vitals)

Beispiel:
```html
<img src="/assets/juergen-gehrke-beratung.jpg"
     alt="Jürgen Gehrke erklärt einem Bauherrn Details beim Fachwerkhaus-Fenster"
     loading="lazy" width="800" height="1067">
```

---

## Kontaktdaten (immer diese verwenden)

```
Name:     Jürgen Gehrke
Firma:    Gehrke Bauberatung und -betreuung UG
Adresse:  Stauferstraße 122, 74523 Schwäbisch Hall
Tel:      +49 172 7410650
E-Mail:   info@gehrkebauberatung.de
WhatsApp: https://wa.me/491727410650
```

**WhatsApp-Button** auf jeder Seite einbauen — das ist der wichtigste Conversion-Kanal.

---

## Wiederkehrende UI-Muster

### Section Eyebrow + Headline

```html
<p class="section-eyebrow">Kurzes Label</p>
<h2 class="section-headline">Die eigentliche Überschrift</h2>
```

Eyebrow: uppercase, klein, Bronze, mit Strich davor (via CSS ::before).

### Karten (cream-farbig, scharf)

```html
<div class="wert-card">
  <div class="wert-num">01</div>
  <h3 class="wert-title">Titel</h3>
  <p class="wert-text">Beschreibung</p>
</div>
```

Karten haben oben links eine 3px Bronze-Linie (via CSS ::before). Keine Rundungen.

### Testimonials / Zitate

Zitate immer in Libre Baskerville, kursiv, auf Navy-Hintergrund oder in `.story-quote`.
Autor immer mit Name + Ort/Kontext.

### FAQ

Nutzt natives `<details>` + `<summary>` HTML — kein JavaScript nötig.
Jede FAQ-Seite braucht `FAQPage` JSON-LD.

---

## Was NICHT gemacht werden darf

- ❌ Farben aus dem Design-System ändern oder neue hinzufügen
- ❌ Andere Fonts einbinden (kein Roboto, kein Montserrat etc.)
- ❌ Border-Radius hinzufügen (alles bleibt sharp)
- ❌ Bootstrap, Tailwind oder andere CSS-Frameworks einbinden
- ❌ Bilder ohne `alt`-Attribut
- ❌ Seiten ohne vollständige Meta-Tags und Structured Data deployen
- ❌ JavaScript-Frameworks (React, Vue etc.) — reines Vanilla JS
- ❌ Externe CDN-Abhängigkeiten außer Google Fonts
- ❌ Neue Seiten ohne trailing slash in der URL
- ❌ Inline-Styles statt CSS-Klassen (außer für dynamische Werte)

---

## Checkliste vor jedem Commit

- [ ] Alle Meta-Tags vollständig und seitenspezifisch?
- [ ] Canonical URL korrekt?
- [ ] JSON-LD vorhanden und valide?
- [ ] Alle Bilder haben `alt`, `loading`, `width`, `height`?
- [ ] Nav zeigt die richtige Seite als `active`?
- [ ] Footer identisch mit anderen Seiten?
- [ ] Mobile-View getestet (max-width: 768px)?
- [ ] Keine hardcodierten Farben (alles via CSS-Variablen)?
- [ ] WhatsApp-Link vorhanden?
