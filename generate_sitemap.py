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

# 2. Create sitemap.xml
html_files = glob.glob(os.path.join(build_dir, '**/*.html'), recursive=True)
today = datetime.now().strftime('%Y-%m-%d')

sitemap_urls = []
for file in sorted(html_files):
    rel_path = os.path.relpath(file, build_dir).replace('\\', '/')
    if rel_path == "404.html":
        continue
    
    # Priority & frequency rules
    priority = "0.8"
    changefreq = "monthly"
    if rel_path == "index.html":
        rel_path = ""
        priority = "1.0"
        changefreq = "weekly"
    elif "servicos/" in rel_path or rel_path == "servicos.html":
        priority = "0.9"
        changefreq = "monthly"
    elif "blog/" in rel_path:
        priority = "0.7"
        changefreq = "monthly"
        
    url_tag = f"""  <url>
    <loc>{base_url}/{rel_path}</loc>
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

print(f"Generated robots.txt and sitemap.xml with {len(sitemap_urls)} URLs.")
