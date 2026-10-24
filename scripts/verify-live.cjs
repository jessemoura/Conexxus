const https = require('https');

const pages = [
  'https://www.conexxus.co.uk/',
  'https://www.conexxus.co.uk/servicos.html',
  'https://www.conexxus.co.uk/sobre.html',
  'https://www.conexxus.co.uk/portfolio.html',
  'https://www.conexxus.co.uk/blog.html',
  'https://www.conexxus.co.uk/contato.html',
  'https://www.conexxus.co.uk/privacidade.html',
  'https://www.conexxus.co.uk/servicos/criacao-de-websites.html',
  'https://www.conexxus.co.uk/servicos/google-business-profile.html',
  'https://www.conexxus.co.uk/servicos/seo-local.html',
  'https://www.conexxus.co.uk/blog/digital-marketing-for-small-businesses.html',
  'https://www.conexxus.co.uk/blog/social-media-for-small-businesses.html',
  'https://www.conexxus.co.uk/blog/why-quality-website-hosting-matters.html',
  'https://www.conexxus.co.uk/blog/how-much-does-a-website-cost-in-swindon.html',
  'https://www.conexxus.co.uk/blog/website-design-for-small-businesses-in-swindon.html',
  'https://www.conexxus.co.uk/blog/local-seo-for-swindon-businesses.html',
  'https://www.conexxus.co.uk/blog/improve-google-business-profile-swindon.html',
  'https://www.conexxus.co.uk/sitemap.xml',
  'https://www.conexxus.co.uk/robots.txt'
];

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
    const req = https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, res => {
      resolve({ url, status: res.statusCode });
    });
    req.on('error', e => resolve({ url, status: 'ERROR: ' + e.message }));
  });
}

async function run() {
  console.log('=== VERIFYING LIVE PUBLIC PAGES (CONEXXUS UK) ===');
  let pagesOk = 0;
  for (const page of pages) {
    const res = await checkUrl(page);
    console.log((res.status === 200 ? '✓ 200' : '✗ ' + res.status) + ' ' + res.url);
    if (res.status === 200) pagesOk++;
  }

  console.log('\n=== VERIFYING LIVE PUBLIC ASSETS ===');
  let assetsOk = 0;
  for (const asset of assets) {
    const res = await checkUrl(asset);
    console.log((res.status === 200 ? '✓ 200' : '✗ ' + res.status) + ' ' + res.url);
    if (res.status === 200) assetsOk++;
  }

  console.log('\n========================================');
  console.log(`PAGES:  ${pagesOk}/${pages.length} ONLINE`);
  console.log(`ASSETS: ${assetsOk}/${assets.length} AVAILABLE`);
  console.log('========================================');
}

run();
