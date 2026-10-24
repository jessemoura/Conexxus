import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const buildDir = path.join(__dirname, '..', 'build');

console.log('====================================================');
console.log('   CONEXXUS UK — AUTOMATED AUDIT & VALIDATION SUITE  ');
console.log('====================================================\n');

function walk(dir) {
  let results = [];
  const list = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of list) {
    const fullPath = path.join(dir, item.name);
    if (item.isDirectory()) {
      results = results.concat(walk(fullPath));
    } else if (item.name.endsWith('.html') && item.name !== '404.html') {
      results.push(fullPath);
    }
  }
  return results;
}

const htmlFiles = walk(buildDir);
let totalErrors = 0;
let totalWarnings = 0;

console.log(`Found ${htmlFiles.length} HTML production pages to audit.\n`);

for (const file of htmlFiles) {
  const relPath = path.relative(buildDir, file).replace(/\\/g, '/');
  const content = fs.readFileSync(file, 'utf8');
  let errors = [];
  let warnings = [];

  // 1. Check exactly 1 H1
  const h1Matches = content.match(/<h1[^>]*>([\s\S]*?)<\/h1>/gi) || [];
  if (h1Matches.length === 0) {
    errors.push('Missing <h1> element');
  } else if (h1Matches.length > 1) {
    errors.push(`Multiple <h1> elements found (${h1Matches.length})`);
  }

  // 2. Check title tag
  const titleMatch = content.match(/<title>([\s\S]*?)<\/title>/i);
  if (!titleMatch || !titleMatch[1].trim()) {
    errors.push('Missing or empty <title>');
  }

  // 3. Check meta description
  const descMatch = content.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)["']/i);
  if (!descMatch || !descMatch[1].trim()) {
    errors.push('Missing or empty <meta name="description">');
  }

  // 4. Check canonical (must be valid, https, and NEVER contain .html)
  const canonMatch = content.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']*)["']/i);
  if (!canonMatch || !canonMatch[1].startsWith('https://www.conexxus.co.uk')) {
    errors.push('Missing or invalid <link rel="canonical">');
  } else if (canonMatch[1].includes('.html')) {
    errors.push(`Canonical MUST NOT contain .html: found "${canonMatch[1]}"`);
  }

  // 5. Check Favicon references
  if (!content.includes('href="/favicon.ico"') && !content.includes('href="/favicon-32x32.png"')) {
    errors.push('Missing official favicon link in <head>');
  }

  // 6. Check Open Graph & Social Preview
  const ogImg = content.match(/<meta[^>]+property=["']og:image["'][^>]+content=["']([^"']*)["']/i);
  if (!ogImg || (!ogImg[1].includes('conexxus-uk-social-preview.png') && !ogImg[1].includes('/06-imagens/'))) {
    errors.push('Missing or invalid og:image (must point to conexxus-uk-social-preview.png or /06-imagens/)');
  }
  if (!content.includes('property="og:title"')) errors.push('Missing og:title');
  
  const ogUrlMatch = content.match(/<meta[^>]+property=["']og:url["'][^>]+content=["']([^"']*)["']/i);
  if (!ogUrlMatch) {
    errors.push('Missing og:url');
  } else if (ogUrlMatch[1].includes('.html')) {
    errors.push(`og:url MUST NOT contain .html: found "${ogUrlMatch[1]}"`);
  }

  if (!content.includes('name="twitter:card"')) errors.push('Missing twitter:card');

  // 7. Check official logo
  if (!content.includes('/06-imagens/conexxus-uk-logo-transparent.png')) {
    errors.push('Missing official logo reference: /06-imagens/conexxus-uk-logo-transparent.png');
  }

  // 8. Check JSON-LD Structured Data
  const jsonLdBlocks = [...content.matchAll(/<script type=["']application\/ld\+json["']>([\s\S]*?)<\/script>/gi)];
  if (jsonLdBlocks.length === 0) {
    errors.push('Missing JSON-LD structured data');
  } else {
    jsonLdBlocks.forEach((block, idx) => {
      try {
        const parsed = JSON.parse(block[1]);
        const blockStr = JSON.stringify(parsed);
        if (blockStr.includes('.html')) {
          errors.push(`JSON-LD block #${idx + 1} contains .html in URL or property`);
        }
        if (blockStr.includes('/sobre') || blockStr.includes('/servicos') || blockStr.includes('/contato') || blockStr.includes('/privacidade')) {
          errors.push(`JSON-LD block #${idx + 1} contains legacy Portuguese path`);
        }
      } catch (err) {
        errors.push(`Invalid JSON-LD syntax in block #${idx + 1}: ${err.message}`);
      }
    });
  }

  // 9. Check script.js inclusion
  if (!content.includes('/assets/js/script.js')) {
    errors.push('Missing core analytics /assets/js/script.js');
  }

  // 10. Check Internal Links for .html
  const hrefMatches = [...content.matchAll(/href=["']([^"']+)["']/gi)];
  for (const match of hrefMatches) {
    const target = match[1];
    // Check if internal link
    const isInternal = target.startsWith('/') || target.startsWith('..') || (!target.startsWith('http') && !target.startsWith('mailto:') && !target.startsWith('tel:') && !target.startsWith('#') && !target.startsWith('javascript:'));
    const isSameDomain = target.startsWith('https://www.conexxus.co.uk') || target.startsWith('http://www.conexxus.co.uk') || target.startsWith('https://conexxus.co.uk');
    
    if (isInternal || isSameDomain) {
      if (target.includes('.html')) {
        errors.push(`Internal link points to .html: "${target}"`);
      }
    }
  }

  // 11. Check Mojibake
  if (/Ã[¡-ÿ]|Ãƒ|Ã‚|â€/.test(content)) {
    warnings.push('Possible Mojibake / encoding corruption detected');
  }

  // Log per-file results
  if (errors.length === 0 && warnings.length === 0) {
    console.log(`✓ [PASS] ${relPath}`);
  } else {
    console.log(`✗ [FAIL] ${relPath}`);
    errors.forEach(e => console.log(`    ERROR: ${e}`));
    warnings.forEach(w => console.log(`    WARN:  ${w}`));
  }

  totalErrors += errors.length;
  totalWarnings += warnings.length;
}

// 12. Check Required Files Exist
const requiredFiles = [
  'favicon.ico',
  'favicon-16x16.png',
  'favicon-32x32.png',
  'favicon-48x48.png',
  'apple-touch-icon.png',
  'site.webmanifest',
  'robots.txt',
  'sitemap.xml',
  '404.html',
  '06-imagens/conexxus-uk-logo-transparent.png',
  '06-imagens/conexxus-uk-social-preview.png',
  '06-imagens/conexxus-uk-favicon.png',
  '06-imagens/portfolio-cover-michelly-correa.webp',
  '06-imagens/portfolio-cover-nikki-studio.webp',
  '06-imagens/portfolio-cover-sos-aberturas.webp',
  '06-imagens/portfolio-cover-oxford-barber.webp',
  '06-imagens/portfolio-cover-nicolas-furoni.webp',
  '06-imagens/portfolio-cover-lumora-cleaning.webp',
  '06-imagens/portfolio-cover-crafix.webp',
  '06-imagens/portfolio-cover-little-pet.webp',
  '06-imagens/portfolio-cover-aroma-oak.webp',
  '06-imagens/signs-your-business-website-needs-a-redesign.webp',
  '06-imagens/seo-vs-google-ads-small-business-uk.webp',
  '06-imagens/how-long-does-local-seo-take.webp',
  '06-imagens/mobile-website-speed-local-businesses.webp',
  '06-imagens/get-more-local-customers-through-google.webp',
  '06-imagens/why-small-business-needs-professional-website.webp',
  'assets/js/script.js',
  'assets/css/style.css'
];

console.log('\n--- Checking Required Build Assets ---');
for (const req of requiredFiles) {
  const fullReq = path.join(buildDir, req);
  if (fs.existsSync(fullReq)) {
    console.log(`✓ [FOUND] ${req}`);
  } else {
    console.log(`✗ [MISSING] ${req}`);
    totalErrors++;
  }
}

// 13. Audit sitemap.xml for Clean URLs
console.log('\n--- Checking Sitemap for Clean URLs ---');
const sitemapPath = path.join(buildDir, 'sitemap.xml');
if (fs.existsSync(sitemapPath)) {
  const sitemapXml = fs.readFileSync(sitemapPath, 'utf8');
  const locMatches = [...sitemapXml.matchAll(/<loc>([^<]+)<\/loc>/gi)].map(m => m[1]);
  console.log(`Sitemap contains ${locMatches.length} URLs.`);
  
  if (locMatches.length === 0) {
    console.log('✗ [ERROR] Sitemap is empty!');
    totalErrors++;
  }

  for (const loc of locMatches) {
    if (loc.includes('.html')) {
      console.log(`✗ [ERROR] Sitemap contains .html URL: ${loc}`);
      totalErrors++;
    } else if (loc !== 'https://www.conexxus.co.uk/' && loc.endsWith('/')) {
      console.log(`✗ [ERROR] Sitemap contains trailing slash URL: ${loc}`);
      totalErrors++;
    } else {
      console.log(`✓ [CLEAN] ${loc}`);
    }
  }
} else {
  console.log('✗ [MISSING] sitemap.xml');
  totalErrors++;
}

console.log('\n====================================================');
console.log(`VALIDATION RESULT: ${totalErrors === 0 ? 'SUCCESS' : 'FAILED'}`);
console.log(`Errors: ${totalErrors} | Warnings: ${totalWarnings}`);
console.log('====================================================\n');

if (totalErrors > 0) {
  process.exit(1);
}
