/* ===== Conexxus — Main JavaScript ===== */
/* Alpine.js for mobile menu + FAQ accordion */
/* Google Consent Mode v2 + LGPD Consent Bar */

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

// ── GA4 Conditional (uncomment and add your ID when ready) ──
// const GA4_ID = ''; // e.g. 'G-XXXXXXXXXX'
// if (GA4_ID) {
//   const script = document.createElement('script');
//   script.async = true;
//   script.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`;
//   document.head.appendChild(script);
//   script.onload = function() {
//     gtag('js', new Date());
//     gtag('config', GA4_ID);
//   };
// }

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

// ── Alpine.js Store for Consent ──
document.addEventListener('alpine:init', () => {
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
});

// ── Smooth scroll for anchor links ──
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
