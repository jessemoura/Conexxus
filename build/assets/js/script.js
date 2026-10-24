/* ===== CONEXXUS — Main JavaScript & Analytics Module ===== */
/* Frameworks: Alpine.js for mobile menu + FAQ accordion */
/* Compliance: Google Consent Mode v2 + UK GDPR Consent */

// ── Google Consent Mode v2 — Default Denied ──
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'wait_for_update': 500
});

// ── GA4 Loader (Supports UK GA4 Measurement ID) ──
const GA4_ID = window.GA4_MEASUREMENT_ID || '';
if (GA4_ID && GA4_ID !== 'G-XXXXXXXXXX') {
  const script = document.createElement('script');
  script.async = true;
  script.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`;
  document.head.appendChild(script);
  script.onload = function() {
    gtag('js', new Date());
    gtag('config', GA4_ID, {
      send_page_view: true
    });
  };
}

// ── Event Deduplication Cache (600ms debounce) ──
const recentEvents = new Map();
const DEDUPLICATION_WINDOW_MS = 600;

/**
 * Dispatches an event securely to GA4 / dataLayer without duplicate triggers
 */
function sendAnalyticsEvent(eventName, rawParams = {}) {
  try {
    const now = Date.now();
    const eventSig = `${eventName}::${rawParams.button_name || ''}::${rawParams.destination_url || ''}::${rawParams.target || ''}`;
    const lastTime = recentEvents.get(eventSig);
    if (lastTime && (now - lastTime) < DEDUPLICATION_WINDOW_MS) {
      return; // Skip duplicate trigger within debounce window
    }
    recentEvents.set(eventSig, now);

    // Garbage collect debounce cache periodically
    if (recentEvents.size > 50) {
      for (const [key, ts] of recentEvents.entries()) {
        if (now - ts > 5000) recentEvents.delete(key);
      }
    }

    const sanitizedParams = {
      page_location: window.location.pathname || '/',
      page_title: document.title || 'CONEXXUS',
      ...rawParams
    };

    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, sanitizedParams);
    }
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: eventName,
      ...sanitizedParams
    });

    if (window.__CONEXXUS_DEBUG__) {
      console.log('[Analytics Event]', eventName, sanitizedParams);
    }
  } catch (err) {
    console.warn('[CONEXXUS Analytics] Error sending event:', err);
  }
}
window.sendAnalyticsEvent = sendAnalyticsEvent;

// ── Delegated Commercial Event Tracking ──
document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('click', function(e) {
    const link = e.target.closest('a, button');
    if (!link) return;

    const href = link.getAttribute('href') || '';
    const text = (link.textContent || '').trim().replace(/\s+/g, ' ');
    const isWaFloat = link.classList.contains('whatsapp-float');
    const ariaLabel = link.getAttribute('aria-label') || '';
    const buttonName = ariaLabel || (isWaFloat ? 'WhatsApp Floating Button' : (text.slice(0, 50) || 'Action Button'));

    // 1. WhatsApp Clicks
    if (href.includes('wa.me') || href.includes('whatsapp.com') || isWaFloat) {
      sendAnalyticsEvent('whatsapp_click', {
        button_name: buttonName,
        destination_url: href
      });
      return;
    }

    // 2. Telephone Clicks
    if (href.startsWith('tel:')) {
      sendAnalyticsEvent('phone_click', {
        button_name: buttonName,
        phone_number: href.replace('tel:', '')
      });
      return;
    }

    // 3. Email Clicks
    if (href.startsWith('mailto:')) {
      sendAnalyticsEvent('email_click', {
        button_name: buttonName,
        email_address: href.replace('mailto:', '').split('?')[0]
      });
      return;
    }

    // 4. Contact Clicks
    if (href.includes('contact') || href.includes('contato')) {
      sendAnalyticsEvent('contact_click', {
        button_name: buttonName,
        destination_url: href
      });
      return;
    }

    // 5. Portfolio Project Clicks
    if (link.closest('.portfolio-card') || link.closest('.portfolio-premium-card') || href.includes('portfolio') || href.includes('nicolasfuroni') || href.includes('oxfordbarber') || href.includes('lumoracleaning') || href.includes('crafix') || href.includes('littlepet')) {
      sendAnalyticsEvent('portfolio_click', {
        button_name: buttonName,
        destination_url: href
      });
      return;
    }

    // 6. Service Pages Clicks
    if (href.includes('services') || href.includes('servicos') || href.includes('web-design') || href.includes('criacao-de-websites') || href.includes('local-seo') || href.includes('seo-local') || href.includes('google-business-profile')) {
      sendAnalyticsEvent('service_click', {
        button_name: buttonName,
        destination_url: href
      });
      return;
    }

    // 7. Generic CTA Clicks
    if (link.classList.contains('btn-primary') || link.classList.contains('btn-secondary') || link.classList.contains('btn-outline')) {
      sendAnalyticsEvent('cta_click', {
        button_name: buttonName,
        destination_url: href
      });
      return;
    }
  });

  // 8. Form Submissions
  document.addEventListener('submit', function(e) {
    const form = e.target;
    const formId = form.getAttribute('id') || form.getAttribute('name') || 'contact_form';
    sendAnalyticsEvent('form_submit', {
      form_id: formId
    });
  });
});

// ── Header scroll behavior ──
document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('.site-header');
  if (header) {
    function handleScroll() {
      if (window.scrollY > 50) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
  }
});

// ── Alpine.js Store for Consent (UK GDPR compliant) ──
document.addEventListener('alpine:init', () => {
  if (typeof Alpine !== 'undefined' && Alpine.store) {
    Alpine.store('consent', {
      show: false,
      init() {
        const choice = localStorage.getItem('cnx_consent');
        if (!choice) {
          setTimeout(() => { this.show = true; }, 1500);
        }
      },
      accept() {
        gtag('consent', 'update', {
          'ad_storage': 'granted',
          'ad_user_data': 'granted',
          'ad_personalization': 'granted',
          'analytics_storage': 'granted'
        });
        localStorage.setItem('cnx_consent', 'granted');
        this.show = false;
      },
      decline() {
        localStorage.setItem('cnx_consent', 'denied');
        this.show = false;
      }
    });
  }
});

// ── Smooth scroll for anchor links ──
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId && targetId !== '#') {
        const target = document.querySelector(targetId);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });
});
