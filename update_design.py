import os
import glob
import re

build_dir = 'c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build'

old_colors_re = re.compile(r'colors:\s*\{[^}]+\}', re.MULTILINE)
new_colors = """colors: {
                        navy: '#003A70',
                        brand: '#0066B3',
                        champagne_gold: '#D6B66A',
                        champagne_light: '#E8D39B',
                        cloud: '#F4F7FA',
                        graphite: '#181A1B',
                    }"""

files = glob.glob(f'{build_dir}/**/*.html', recursive=True)
count = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update tailwind config
    content = old_colors_re.sub(new_colors, content)

    # 2. Update CSS classes
    content = content.replace('text-cyan', 'text-champagne_gold')
    content = content.replace('border-cyan', 'border-champagne_gold')
    content = content.replace('bg-cyan', 'bg-champagne_gold')
    content = content.replace('hover:text-cyan', 'hover:text-champagne_gold')
    content = content.replace('shadow-cyan', 'shadow-champagne_gold')
    
    # 3. Update logo images
    content = content.replace('CONEXXUS_Logo_Web_Transparente.png', 'logo-conexxus-light.png')
    
    # Invert class is no longer needed since the logo has white/gold colors, not just plain white that needs invert.
    # We remove 'brightness-0 invert' specifically from the logo img tag.
    content = content.replace('class="h-10 w-auto brightness-0 invert"', 'class="h-10 w-auto"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        count += 1

print(f"Updated {count} files with new colors and logo.")
