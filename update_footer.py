import glob
import os

build_dir = 'c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build'
files = glob.glob(f'{build_dir}/**/*.html', recursive=True)
count = 0

old_str = '<h3 class="text-2xl font-bold text-white tracking-wider">CONEXXUS</h3>'
new_str = '<img src="../06-imagens/Conexxus-digital-marketing-logo-transparent.png" alt="Conexxus Logo" class="h-12 w-auto">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(old_str, new_str)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Updated footer logo in {count} files.')
