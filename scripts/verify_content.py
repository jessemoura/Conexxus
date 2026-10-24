# -*- coding: utf-8 -*-
import os
import re

slugs = [
    'signs-your-business-website-needs-a-redesign',
    'seo-vs-google-ads-small-business-uk',
    'how-long-does-local-seo-take',
    'mobile-website-speed-local-businesses',
    'get-more-local-customers-through-google',
    'why-small-business-needs-professional-website'
]

titles = set()
descs = set()

for slug in slugs:
    p = os.path.join('build', 'blog', slug + '.html')
    with open(p, encoding='utf-8') as f:
        c = f.read()

    # 1. H1 check
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.IGNORECASE | re.DOTALL)
    assert len(h1s) == 1, f"H1 count != 1 in {slug}: {len(h1s)}"

    # 2. Title check
    t_match = re.search(r'<title>(.*?)</title>', c, re.IGNORECASE)
    assert t_match, f"Missing title in {slug}"
    t = t_match.group(1).strip()
    assert t not in titles, f"Duplicate title: {t}"
    titles.add(t)

    # 3. Meta description check
    d_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', c, re.IGNORECASE)
    assert d_match, f"Missing description in {slug}"
    d = d_match.group(1).strip()
    assert d not in descs, f"Duplicate desc: {d}"
    descs.add(d)

    # 4. Check currency / US / Brazilian terms
    assert 'R$' not in c, f"R$ found in {slug}"
    assert 'lorem' not in c.lower(), f"Lorem found in {slug}"
    assert 'placeholder' not in c.lower(), f"Placeholder found in {slug}"

    # 5. Image check
    img_match = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\'](.*?)["\']', c, re.IGNORECASE)
    assert img_match, f"Missing og:image in {slug}"
    img_url = img_match.group(1)
    img_filename = img_url.split('/')[-1]
    local_img_path = os.path.join('build', '06-imagens', img_filename)
    assert os.path.exists(local_img_path), f"Image file missing: {local_img_path}"

    print(f"[OK] {slug}")
    print(f"     Title: {t}")
    print(f"     Desc:  {d}")
    print(f"     Image: {img_filename} (Size: {os.path.getsize(local_img_path)} bytes)")

print("\n--- CHECKING BLOG.HTML GRID CARDS ---")
with open(os.path.join('build', 'blog.html'), encoding='utf-8') as f:
    blog_html = f.read()

blog_card_slugs = re.findall(r'<a[^>]+href=["\']/blog/([^"\']+)["\']', blog_html)
print(f"Total blog cards found in build/blog.html: {len(blog_card_slugs)}")
for i, s in enumerate(blog_card_slugs, 1):
    print(f"  {i}. /blog/{s}")
assert len(blog_card_slugs) == 13, f"Expected 13 blog cards, got {len(blog_card_slugs)}"

print("\n--- ALL 6 ARTICLES AND BLOG INDEX VALIDATED SUCCESSFULLY ---")
