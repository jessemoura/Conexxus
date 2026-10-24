const https = require('https');

// 1. All 17 Clean Production Pages (Expected: HTTP 200)
const cleanPages = [
  'https://www.conexxus.co.uk/',
  'https://www.conexxus.co.uk/services',
  'https://www.conexxus.co.uk/services/web-design',
  'https://www.conexxus.co.uk/services/local-seo',
  'https://www.conexxus.co.uk/services/google-business-profile',
  'https://www.conexxus.co.uk/about',
  'https://www.conexxus.co.uk/portfolio',
  'https://www.conexxus.co.uk/blog',
  'https://www.conexxus.co.uk/contact',
  'https://www.conexxus.co.uk/privacy',
  'https://www.conexxus.co.uk/blog/how-much-does-a-website-cost-in-swindon',
  'https://www.conexxus.co.uk/blog/website-design-for-small-businesses-in-swindon',
  'https://www.conexxus.co.uk/blog/local-seo-for-swindon-businesses',
  'https://www.conexxus.co.uk/blog/improve-google-business-profile-swindon',
  'https://www.conexxus.co.uk/blog/digital-marketing-for-small-businesses',
  'https://www.conexxus.co.uk/blog/social-media-for-small-businesses',
  'https://www.conexxus.co.uk/blog/why-quality-website-hosting-matters',
  'https://www.conexxus.co.uk/sitemap.xml',
  'https://www.conexxus.co.uk/robots.txt'
];

// 2. Legacy URLs (Expected: HTTP 301 -> clean URL)
const legacyRedirects = [
  { from: 'https://www.conexxus.co.uk/index.html', to: 'https://www.conexxus.co.uk/' },
  { from: 'https://www.conexxus.co.uk/portfolio.html', to: 'https://www.conexxus.co.uk/portfolio' },
  { from: 'https://www.conexxus.co.uk/blog.html', to: 'https://www.conexxus.co.uk/blog' },
  { from: 'https://www.conexxus.co.uk/sobre.html', to: 'https://www.conexxus.co.uk/about' },
  { from: 'https://www.conexxus.co.uk/servicos.html', to: 'https://www.conexxus.co.uk/services' },
  { from: 'https://www.conexxus.co.uk/contato.html', to: 'https://www.conexxus.co.uk/contact' },
  { from: 'https://www.conexxus.co.uk/privacidade.html', to: 'https://www.conexxus.co.uk/privacy' },
  { from: 'https://www.conexxus.co.uk/about.html', to: 'https://www.conexxus.co.uk/about' },
  { from: 'https://www.conexxus.co.uk/services.html', to: 'https://www.conexxus.co.uk/services' },
  { from: 'https://www.conexxus.co.uk/contact.html', to: 'https://www.conexxus.co.uk/contact' },
  { from: 'https://www.conexxus.co.uk/privacy.html', to: 'https://www.conexxus.co.uk/privacy' },
  { from: 'https://www.conexxus.co.uk/servicos/criacao-de-websites.html', to: 'https://www.conexxus.co.uk/services/web-design' },
  { from: 'https://www.conexxus.co.uk/servicos/seo-local.html', to: 'https://www.conexxus.co.uk/services/local-seo' },
  { from: 'https://www.conexxus.co.uk/servicos/google-business-profile.html', to: 'https://www.conexxus.co.uk/services/google-business-profile' },
  { from: 'https://www.conexxus.co.uk/blog/how-much-does-a-website-cost-in-swindon.html', to: 'https://www.conexxus.co.uk/blog/how-much-does-a-website-cost-in-swindon' },
  { from: 'https://www.conexxus.co.uk/blog/website-design-for-small-businesses-in-swindon.html', to: 'https://www.conexxus.co.uk/blog/website-design-for-small-businesses-in-swindon' },
  { from: 'https://www.conexxus.co.uk/blog/local-seo-for-swindon-businesses.html', to: 'https://www.conexxus.co.uk/blog/local-seo-for-swindon-businesses' },
  { from: 'https://www.conexxus.co.uk/blog/improve-google-business-profile-swindon.html', to: 'https://www.conexxus.co.uk/blog/improve-google-business-profile-swindon' },
  { from: 'https://www.conexxus.co.uk/portfolio/', to: 'https://www.conexxus.co.uk/portfolio' }
];

// 3. Core Public Assets (Expected: HTTP 200)
const assets = [
  'https://www.conexxus.co.uk/06-imagens/conexxus-uk-logo-transparent.png',
  'https://www.conexxus.co.uk/06-imagens/conexxus-uk-social-preview.png',
  'https://www.conexxus.co.uk/06-imagens/how-much-does-a-website-cost-in-swindon.webp',
  'https://www.conexxus.co.uk/06-imagens/website-design-for-small-businesses-in-swindon.webp',
  'https://www.conexxus.co.uk/06-imagens/local-seo-for-swindon-businesses.webp',
  'https://www.conexxus.co.uk/06-imagens/improve-google-business-profile-swindon.webp',
  'https://www.conexxus.co.uk/favicon.ico',
  'https://www.conexxus.co.uk/apple-touch-icon.png',
  'https://www.conexxus.co.uk/assets/js/script.js',
  'https://www.conexxus.co.uk/assets/css/style.css'
];

async function checkUrl(url) {
  return new Promise(resolve => {
    const req = https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' } }, res => {
      resolve({ url, status: res.statusCode, location: res.headers.location || null });
    });
    req.on('error', e => resolve({ url, status: 'ERROR: ' + e.message, location: null }));
  });
}

async function run() {
  console.log('====================================================');
  console.log('   CONEXXUS UK — LIVE PRODUCTION DEPLOY VERIFICATION ');
  console.log('====================================================\n');

  console.log('=== 1. VERIFYING CLEAN PRODUCTION PAGES (Target: HTTP 200) ===');
  let cleanPagesOk = 0;
  for (const page of cleanPages) {
    const res = await checkUrl(page);
    const pass = res.status === 200;
    console.log(`${pass ? '✓ 200' : '✗ ' + res.status} ${res.url}`);
    if (pass) cleanPagesOk++;
  }

  console.log(`\n=== 2. VERIFYING 301 REDIRECTS FROM LEGACY URLs (Target: HTTP 301) ===`);
  let redirectsOk = 0;
  for (const item of legacyRedirects) {
    const res = await checkUrl(item.from);
    const is301 = res.status === 301;
    const destMatch = res.location === item.to || res.location === new URL(item.to).pathname;
    const pass = is301 && destMatch;
    console.log(`${pass ? '✓ 301' : '✗ ' + res.status} ${item.from}`);
    console.log(`      → Location: ${res.location} (Expected: ${item.to})`);
    if (pass) redirectsOk++;
  }

  console.log(`\n=== 3. VERIFYING PUBLIC ASSETS (Target: HTTP 200) ===`);
  let assetsOk = 0;
  for (const asset of assets) {
    const res = await checkUrl(asset);
    const pass = res.status === 200;
    console.log(`${pass ? '✓ 200' : '✗ ' + res.status} ${res.url}`);
    if (pass) assetsOk++;
  }

  console.log('\n====================================================');
  console.log(`CLEAN PAGES:  ${cleanPagesOk}/${cleanPages.length} ONLINE (200)`);
  console.log(`301 REDIRECTS:${redirectsOk}/${legacyRedirects.length} REDIRECTING CORRECTLY (301)`);
  console.log(`ASSETS:       ${assetsOk}/${assets.length} AVAILABLE (200)`);
  console.log('====================================================');

  if (cleanPagesOk !== cleanPages.length || redirectsOk !== legacyRedirects.length || assetsOk !== assets.length) {
    console.log('\nWarning: Some live checks did not match expectations. Check if Hostinger deployment finished.');
    process.exitCode = 1;
  }
}

run();
