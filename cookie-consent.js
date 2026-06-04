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

  /* ---------- Consent anwenden (GA-Hook) ---------- */
  function applyConsent(consent) {
    if (consent && consent.analytics) loadAnalytics();
  }

  function loadAnalytics() {
    if (window.__gehrkeAnalyticsLoaded) return;
    window.__gehrkeAnalyticsLoaded = true;
    /* TODO: Google Analytics hier laden, sobald gewünscht
       (empfohlen via Google Consent Mode v2 / gtag.js).
       Aktuell bewusst leer — es wird noch kein Tracking aktiviert. */
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
  var CSS = '' +
    '.gc-banner{position:fixed;left:0;right:0;bottom:0;z-index:9998;background:#0d1c2a;border-top:2px solid #b8763a;color:#fff;font-family:Inter,system-ui,sans-serif;padding:22px 6vw;box-shadow:0 -10px 40px rgba(0,0,0,.3);}' +
    '.gc-banner-inner{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:32px;flex-wrap:wrap;}' +
    '.gc-text{flex:1;min-width:280px;font-size:13.5px;line-height:1.65;font-weight:300;color:rgba(255,255,255,.72);}' +
    '.gc-text strong{display:block;font-family:"Libre Baskerville",Georgia,serif;font-weight:400;font-size:16px;color:#fff;margin-bottom:6px;}' +
    '.gc-text a{color:#b8763a;text-decoration:none;}' +
    '.gc-text a:hover{text-decoration:underline;}' +
    '.gc-actions{display:flex;gap:10px;align-items:center;flex-wrap:wrap;}' +
    '.gc-btn{font-family:inherit;font-size:13px;font-weight:500;padding:13px 24px;border:none;cursor:pointer;white-space:nowrap;transition:background .2s,border-color .2s,color .2s;}' +
    '.gc-btn-accept{background:#b8763a;color:#fff;}' +
    '.gc-btn-accept:hover{background:#c4854a;}' +
    '.gc-btn-reject{background:transparent;color:rgba(255,255,255,.82);border:1px solid rgba(255,255,255,.3);}' +
    '.gc-btn-reject:hover{border-color:rgba(255,255,255,.7);color:#fff;}' +
    '.gc-btn-settings{background:transparent;color:rgba(255,255,255,.6);border:none;text-decoration:underline;padding:13px 6px;font-weight:400;cursor:pointer;}' +
    '.gc-btn-settings:hover{color:#fff;}' +
    '.gc-overlay{position:fixed;inset:0;z-index:9999;background:rgba(13,28,42,.62);display:flex;align-items:center;justify-content:center;padding:24px;}' +
    '.gc-modal{background:#162534;border:1px solid rgba(255,255,255,.1);border-top:3px solid #b8763a;max-width:540px;width:100%;padding:38px 36px;color:#fff;font-family:Inter,system-ui,sans-serif;max-height:90vh;overflow:auto;}' +
    '.gc-modal h2{font-family:"Libre Baskerville",Georgia,serif;font-weight:400;font-size:23px;margin:0 0 10px;}' +
    '.gc-modal>p{font-size:13.5px;line-height:1.7;color:rgba(255,255,255,.6);font-weight:300;margin:0 0 26px;}' +
    '.gc-cat{display:flex;gap:18px;align-items:flex-start;padding:18px 0;border-top:1px solid rgba(255,255,255,.08);}' +
    '.gc-cat:last-of-type{border-bottom:1px solid rgba(255,255,255,.08);margin-bottom:26px;}' +
    '.gc-cat-info{flex:1;}' +
    '.gc-cat-info h3{font-size:14px;font-weight:500;margin:0 0 4px;color:#fff;}' +
    '.gc-cat-info p{font-size:12.5px;line-height:1.6;color:rgba(255,255,255,.5);font-weight:300;margin:0;}' +
    '.gc-switch{position:relative;width:44px;height:24px;flex-shrink:0;}' +
    '.gc-switch input{opacity:0;width:0;height:0;position:absolute;}' +
    '.gc-slider{position:absolute;inset:0;background:rgba(255,255,255,.18);transition:.2s;cursor:pointer;display:block;}' +
    '.gc-slider::before{content:"";position:absolute;height:18px;width:18px;left:3px;top:3px;background:#fff;transition:.2s;}' +
    '.gc-switch input:checked+.gc-slider{background:#b8763a;}' +
    '.gc-switch input:checked+.gc-slider::before{transform:translateX(20px);}' +
    '.gc-switch input:disabled+.gc-slider{opacity:.5;cursor:not-allowed;}' +
    '.gc-modal-actions{display:flex;gap:10px;flex-wrap:wrap;}' +
    '.gc-reopen{cursor:pointer;}' +
    '@media(max-width:680px){.gc-banner-inner{gap:18px;}.gc-actions{width:100%;}.gc-btn-accept,.gc-btn-reject{flex:1;text-align:center;}}';

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
