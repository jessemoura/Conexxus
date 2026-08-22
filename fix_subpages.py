import glob

files = glob.glob('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/**/*.html', recursive=True)
count = 0

old_tag1 = '<img src="..//06-imagens/Conexxus-digital-marketing-logo-transparent.png" alt="Conexxus Logo" class="h-10 w-auto">'
new_tag = '<img src="/06-imagens/Conexxus-digital-marketing-logo-transparent.png" alt="Conexxus Logo" class="h-14 w-auto">'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content.replace(old_tag1, new_tag)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Fixed remaining {count} files.")
