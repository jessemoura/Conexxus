import glob

files = glob.glob('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/**/*.html', recursive=True)
count = 0

old_header_class = "'bg-transparent py-4': !mobileMenuOpen && !isScrolled"
new_header_class = "'bg-transparent py-2 lg:py-4': !mobileMenuOpen && !isScrolled"

old_menu_class = 'class="lg:hidden bg-navy w-full border-t border-blue-900/50 absolute top-full left-0 py-4 shadow-xl"'
new_menu_class = 'class="lg:hidden bg-navy w-full min-h-screen border-t border-blue-900/50 absolute top-full left-0 py-4 shadow-xl"'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(old_header_class, new_header_class)
    new_content = new_content.replace(old_menu_class, new_menu_class)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f'Updated {count} files for header and mobile menu')
