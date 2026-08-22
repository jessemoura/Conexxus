import glob

files = glob.glob('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/**/*.html', recursive=True)
count = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('class="btn-whatsapp"', 'class="btn-primary"')
    new_content = new_content.replace('class="btn-whatsapp ', 'class="btn-primary ')
    
    # Also find "Don't build your business on rented land"
    if "rented land" in content:
        new_content = new_content.replace('digital home a space where', 'digital home — a space where')
        new_content = new_content.replace('customers experience', "customer's experience")
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f'Updated {file}')
