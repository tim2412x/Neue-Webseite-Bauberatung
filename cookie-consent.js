/* ============================================================
   Gehrke Bauberatung – Cookie-Consent
   DSGVO-konformes Cookie-Banner (Opt-in).
   Aktuell wird KEIN Tracking geladen – die Einwilligung wird nur
   gespeichert. Google Analytics kann später in loadAnalytics()
   eingebunden werden (siehe TODO).
   ============================================================ */
(function () {
  'use strict';

  var STORAGE_KEY = 'gehrke_cookie_consent';
  var CONSENT_VERSION = 1;
  var GA_ID = 'G-JZ021LWWW9';

  /* ---------- Consent anwenden (GA-Hook) ---------- */
  function applyConsent(consent) {
    if (consent && consent.analytics) {
      window['ga-disable-' + GA_ID] = false;
      loadAnalytics();
    } else {
      /* Bei Ablehnung/Widerruf: Tracking deaktivieren (Googles Opt-out-Flag).
         Wirkt auch, wenn gtag in dieser Sitzung bereits geladen wurde. */
      window['ga-disable-' + GA_ID] = true;
    }
  }

  function loadAnalytics() {
    if (window.__gehrkeAnalyticsLoaded) return;
    window.__gehrkeAnalyticsLoaded = true;

    /* Google Analytics 4 (gtag.js) — wird ausschließlich nach
       ausdrücklicher Einwilligung über applyConsent() geladen. */
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }

  /* ---------- Speicherung ---------- */
  function getConsent() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var c = JSON.parse(raw);
      if (!c || c.v !== CONSENT_VERSION) return null;
      return c;
    } catch (e) { return null; }
  }

  function saveConsent(analytics) {
    var c = { v: CONSENT_VERSION, analytics: !!analytics, ts: new Date().toISOString() };
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(c)); } catch (e) {}
    applyConsent(c);
    return c;
  }

  /* ---------- Styles ---------- */
  /* Palette "Aufnahme" (REDESIGN §6): Grundton #F7F5F0, Flaechenton #E8E2D6,
     Textton #17171A, Akzent #8A3B12. Schriften Spectral und Barlow, beide
     bereits ueber assets/site.css selbst gehostet. Kein Radius, kein Schatten. */
  var CSS = '' +
    '.gc-banner{position:fixed;left:0;right:0;bottom:0;z-index:9998;background:#F7F5F0;border-top:1px solid #17171A;color:#17171A;font-family:Barlow,"Helvetica Neue",Arial,sans-serif;padding:22px 6vw;}' +
    '.gc-banner-inner{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:32px;flex-wrap:wrap;}' +
    '.gc-text{flex:1;min-width:280px;font-size:14px;line-height:1.7;font-weight:400;color:rgba(23,23,26,.8);}' +
    '.gc-text strong{display:block;font-family:Spectral,Georgia,serif;font-weight:400;font-size:20px;line-height:1.3;color:#17171A;margin-bottom:8px;}' +
    '.gc-text a{color:#8A3B12;text-decoration:underline;text-underline-offset:3px;}' +
    '.gc-text a:hover{color:#17171A;}' +
    '.gc-actions{display:flex;gap:12px;align-items:center;flex-wrap:wrap;}' +
    '.gc-btn{font-family:inherit;font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;padding:14px 24px;border:1px solid transparent;border-radius:0;cursor:pointer;white-space:nowrap;transition:background-color 120ms linear,border-color 120ms linear,color 120ms linear;}' +
    '.gc-btn:focus-visible{outline:2px solid #8A3B12;outline-offset:2px;}' +
    '.gc-btn-accept{background:#8A3B12;border-color:#8A3B12;color:#F7F5F0;}' +
    '.gc-btn-accept:hover{background:#17171A;border-color:#17171A;}' +
    '.gc-btn-reject{background:transparent;color:#17171A;border-color:#17171A;}' +
    '.gc-btn-reject:hover{background:#17171A;color:#F7F5F0;}' +
    '.gc-btn-settings{background:transparent;color:rgba(23,23,26,.7);border:none;text-decoration:underline;text-underline-offset:3px;padding:14px 6px;font-weight:400;letter-spacing:.1em;cursor:pointer;}' +
    '.gc-btn-settings:hover{color:#8A3B12;}' +
    '.gc-overlay{position:fixed;inset:0;z-index:9999;background:rgba(23,23,26,.62);display:flex;align-items:center;justify-content:center;padding:24px;}' +
    '.gc-modal{background:#F7F5F0;border:1px solid #17171A;max-width:540px;width:100%;padding:38px 36px;color:#17171A;font-family:Barlow,"Helvetica Neue",Arial,sans-serif;max-height:90vh;overflow:auto;}' +
    '.gc-modal h2{font-family:Spectral,Georgia,serif;font-weight:400;font-size:28px;line-height:1.25;margin:0 0 12px;}' +
    '.gc-modal>p{font-size:14px;line-height:1.75;color:rgba(23,23,26,.8);font-weight:400;margin:0 0 26px;}' +
    '.gc-cat{display:flex;gap:18px;align-items:flex-start;padding:18px 0;border-top:1px solid rgba(23,23,26,.2);}' +
    '.gc-cat:last-of-type{border-bottom:1px solid rgba(23,23,26,.2);margin-bottom:26px;}' +
    '.gc-cat-info{flex:1;}' +
    '.gc-cat-info h3{font-family:Spectral,Georgia,serif;font-size:18px;font-weight:400;margin:0 0 6px;color:#17171A;}' +
    '.gc-cat-info p{font-size:13px;line-height:1.65;color:rgba(23,23,26,.78);font-weight:400;margin:0;}' +
    '.gc-switch{position:relative;width:44px;height:24px;flex-shrink:0;}' +
    '.gc-switch input{opacity:0;width:0;height:0;position:absolute;}' +
    '.gc-slider{position:absolute;inset:0;background:rgba(23,23,26,.2);transition:background-color 120ms linear;cursor:pointer;display:block;}' +
    '.gc-slider::before{content:"";position:absolute;height:18px;width:18px;left:3px;top:3px;background:#17171A;transition:transform 120ms linear,background-color 120ms linear;}' +
    '.gc-switch input:checked+.gc-slider{background:#8A3B12;}' +
    '.gc-switch input:checked+.gc-slider::before{transform:translateX(20px);background:#F7F5F0;}' +
    '.gc-switch input:focus-visible+.gc-slider{outline:2px solid #8A3B12;outline-offset:2px;}' +
    '.gc-switch input:disabled+.gc-slider{opacity:.5;cursor:not-allowed;}' +
    '.gc-modal-actions{display:flex;gap:12px;flex-wrap:wrap;}' +
    '.gc-reopen{cursor:pointer;}' +
    '@media(max-width:680px){.gc-banner{padding:18px 20px;}.gc-banner-inner{gap:18px;}.gc-actions{width:100%;}.gc-btn-accept,.gc-btn-reject{flex:1;text-align:center;}}';

  function injectStyles() {
    var s = document.createElement('style');
    s.id = 'gc-styles';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  /* ---------- Banner ---------- */
  var bannerEl = null;

  function buildBanner() {
    var b = document.createElement('div');
    b.className = 'gc-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', 'Cookie-Hinweis');
    b.innerHTML =
      '<div class="gc-banner-inner">' +
        '<div class="gc-text">' +
          '<strong>Datenschutz ist uns wichtig</strong>' +
          'Wir verwenden notwendige Cookies für den Betrieb der Website. Mit Ihrer Einwilligung nutzen wir zusätzlich Statistik-Cookies (Google&nbsp;Analytics), um unser Angebot zu verbessern. Sie können Ihre Auswahl jederzeit ändern. Mehr dazu in unserer <a href="/datenschutz/">Datenschutzerklärung</a>.' +
        '</div>' +
        '<div class="gc-actions">' +
          '<button type="button" class="gc-btn gc-btn-settings" data-gc="settings">Einstellungen</button>' +
          '<button type="button" class="gc-btn gc-btn-reject" data-gc="reject">Ablehnen</button>' +
          '<button type="button" class="gc-btn gc-btn-accept" data-gc="accept">Alle akzeptieren</button>' +
        '</div>' +
      '</div>';
    return b;
  }

  function showBanner() {
    if (bannerEl) { bannerEl.style.display = 'block'; return; }
    bannerEl = buildBanner();
    document.body.appendChild(bannerEl);
    bannerEl.querySelector('[data-gc="accept"]').addEventListener('click', function () { saveConsent(true); hideBanner(); });
    bannerEl.querySelector('[data-gc="reject"]').addEventListener('click', function () { saveConsent(false); hideBanner(); });
    bannerEl.querySelector('[data-gc="settings"]').addEventListener('click', openModal);
  }

  function hideBanner() { if (bannerEl) bannerEl.style.display = 'none'; }

  /* ---------- Einstellungen-Modal ---------- */
  var overlayEl = null;

  function openModal() {
    var existing = getConsent();
    var analyticsOn = existing ? existing.analytics : false;

    overlayEl = document.createElement('div');
    overlayEl.className = 'gc-overlay';
    overlayEl.innerHTML =
      '<div class="gc-modal" role="dialog" aria-modal="true" aria-label="Cookie-Einstellungen">' +
        '<h2>Cookie-Einstellungen</h2>' +
        '<p>Entscheiden Sie selbst, welche Cookies wir verwenden dürfen. Notwendige Cookies sind für den Betrieb der Website erforderlich und immer aktiv.</p>' +
        '<div class="gc-cat">' +
          '<div class="gc-cat-info"><h3>Notwendig</h3><p>Erforderlich für grundlegende Funktionen der Website. Diese Cookies können nicht deaktiviert werden.</p></div>' +
          '<label class="gc-switch"><input type="checkbox" checked disabled><span class="gc-slider"></span></label>' +
        '</div>' +
        '<div class="gc-cat">' +
          '<div class="gc-cat-info"><h3>Statistik &middot; Google Analytics</h3><p>Hilft uns zu verstehen, wie die Website genutzt wird, um sie zu verbessern. Wird erst nach Ihrer Einwilligung geladen.</p></div>' +
          '<label class="gc-switch"><input type="checkbox" data-gc="analytics-toggle"' + (analyticsOn ? ' checked' : '') + '><span class="gc-slider"></span></label>' +
        '</div>' +
        '<div class="gc-modal-actions">' +
          '<button type="button" class="gc-btn gc-btn-reject" data-gc="save">Auswahl speichern</button>' +
          '<button type="button" class="gc-btn gc-btn-accept" data-gc="accept-all">Alle akzeptieren</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(overlayEl);

    overlayEl.querySelector('[data-gc="save"]').addEventListener('click', function () {
      var on = overlayEl.querySelector('[data-gc="analytics-toggle"]').checked;
      saveConsent(on); closeModal(); hideBanner();
    });
    overlayEl.querySelector('[data-gc="accept-all"]').addEventListener('click', function () {
      saveConsent(true); closeModal(); hideBanner();
    });
    overlayEl.addEventListener('click', function (e) { if (e.target === overlayEl) closeModal(); });
    document.addEventListener('keydown', escClose);
  }

  function escClose(e) { if (e.key === 'Escape') closeModal(); }

  function closeModal() {
    if (overlayEl) { overlayEl.remove(); overlayEl = null; }
    document.removeEventListener('keydown', escClose);
  }

  /* öffentliche API (z. B. für Footer-Link „Cookie-Einstellungen") */
  window.openCookieSettings = openModal;

  /* ---------- Footer-Link zum Widerruf einfügen ---------- */
  function injectReopenLink() {
    var legal = document.querySelector('.footer-legal');
    if (!legal || legal.querySelector('.gc-reopen')) return;
    var a = document.createElement('a');
    a.href = '#';
    a.className = 'gc-reopen';
    a.textContent = 'Cookie-Einstellungen';
    a.addEventListener('click', function (e) { e.preventDefault(); openModal(); });
    legal.appendChild(a);
  }

  /* ---------- Init ---------- */
  function init() {
    injectStyles();
    injectReopenLink();
    var consent = getConsent();
    if (consent) { applyConsent(consent); }
    else { showBanner(); }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
