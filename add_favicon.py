import glob
import re

files = glob.glob('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/**/*.html', recursive=True)
count = 0

favicon_tag = '\n    <link rel="icon" type="image/png" href="/06-imagens/favicon.png">\n'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'favicon.png' not in content:
        # Try to insert after <title>...</title>
        if '<title>' in content:
            new_content = re.sub(r'(</title>)', r'\1' + favicon_tag, content, count=1)
        else:
            new_content = re.sub(r'(<head.*?>)', r'\1' + favicon_tag, content, count=1)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f'Added favicon to {count} files')
