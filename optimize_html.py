import os
import glob
import re

html_files = glob.glob('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/**/*.html', recursive=True)

preconnect_tags = """
<link rel="preconnect" href="https://cdn.tailwindcss.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add preconnects
    if 'https://cdn.tailwindcss.com' not in content[:content.find('</head>')]:
        content = content.replace('</title>', '</title>\n' + preconnect_tags.strip())

    # 2. Add loading="lazy" and decoding="async" to images (except logos/heroes)
    # We will find all <img ...> tags
    def optimize_img(match):
        img_tag = match.group(0)
        # Skip if already has loading=
        if 'loading=' in img_tag:
            return img_tag
        # Skip hero images or logos that are likely above the fold
        if 'hero' in img_tag.lower() or ('logo' in img_tag.lower() and 'footer' not in img_tag.lower() and 'w-auto' in img_tag):
            return img_tag
        
        # Add attributes
        return img_tag.replace('<img ', '<img loading="lazy" decoding="async" ')

    content = re.sub(r'<img [^>]+>', optimize_img, content)
    
    # 3. Ensure display=swap for Google Fonts
    if 'fonts.googleapis.com/css2' in content and 'display=swap' not in content:
        content = re.sub(r'(fonts\.googleapis\.com/css2[^"\'>]+)', r'\1&display=swap', content)

    # 4. Optional inline JS minification (Alpine / Google Translate)
    # Just basic minification
    content = content.replace('function googleTranslateElementInit() {\n            new google.translate.TranslateElement({\n                pageLanguage: \'en\',\n                includedLanguages: \'en,pt,es\',\n                autoDisplay: false\n            }, \'google_translate_element\');\n        }', 'function googleTranslateElementInit(){new google.translate.TranslateElement({pageLanguage:"en",includedLanguages:"en,pt,es",autoDisplay:!1},"google_translate_element")}')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Optimized HTML files")
