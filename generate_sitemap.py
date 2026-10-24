import os
import glob
from datetime import datetime

base_url = "https://www.conexxus.co.uk"
current_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(current_dir, 'build')

# 1. Create robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""
with open(os.path.join(build_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

# 2. Create sitemap.xml with Clean Extensionless URLs
today = datetime.now().strftime('%Y-%m-%d')

CLEAN_PAGES = [
    # Homepage
    ("", "1.0", "weekly"),
    # Core Services
    ("services", "0.9", "monthly"),
    ("services/web-design", "0.9", "monthly"),
    ("services/local-seo", "0.9", "monthly"),
    ("services/google-business-profile", "0.9", "monthly"),
    # Institutional
    ("about", "0.8", "monthly"),
    ("portfolio", "0.8", "monthly"),
    ("blog", "0.8", "monthly"),
    ("contact", "0.8", "monthly"),
    ("privacy", "0.8", "monthly"),
    # Blog Posts
    ("blog/how-much-does-a-website-cost-in-swindon", "0.7", "monthly"),
    ("blog/website-design-for-small-businesses-in-swindon", "0.7", "monthly"),
    ("blog/local-seo-for-swindon-businesses", "0.7", "monthly"),
    ("blog/improve-google-business-profile-swindon", "0.7", "monthly"),
    ("blog/digital-marketing-for-small-businesses", "0.7", "monthly"),
    ("blog/social-media-for-small-businesses", "0.7", "monthly"),
    ("blog/why-quality-website-hosting-matters", "0.7", "monthly"),
]

sitemap_urls = []
for rel_path, priority, changefreq in CLEAN_PAGES:
    url_loc = f"{base_url}/{rel_path}" if rel_path else f"{base_url}/"
    url_tag = f"""  <url>
    <loc>{url_loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
    sitemap_urls.append(url_tag)

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>
"""

with open(os.path.join(build_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated robots.txt and sitemap.xml with {len(sitemap_urls)} clean URLs.")

