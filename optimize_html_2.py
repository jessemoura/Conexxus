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

    # 1. Add preconnects if not already present
    if '<link rel="preconnect" href="https://cdn.tailwindcss.com"' not in content:
        content = content.replace('</title>', '</title>\n' + preconnect_tags)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added preconnects")
