import os
import re

css_path = 'c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/assets/css/style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove newlines and extra spaces
css = re.sub(r'\s+', ' ', css)
# Remove spaces around brackets, colons, etc.
css = re.sub(r'\s*([\{\}\:\;\,\>])\s*', r'\1', css)
css = css.strip()

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print('Minified style.css')
