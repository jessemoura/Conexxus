import os
import glob
import re

build_dir = 'build'

whatsapp_block_re = re.compile(
    r'<a href="https://wa\.me/447341462757" target="_blank" class="flex items-center justify-center w-9 h-9 rounded-full bg-\[#25D366\] text-white shadow-\[0_0_12px_rgba\(37,211,102,0\.5\)\] hover:scale-110 transition-transform" title="WhatsApp">\s*<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="[^"]+"/></svg>\s*</a>'
)

email_block = """<a href="mailto:hello@conexxus.co.uk" class="flex items-center justify-center w-9 h-9 rounded-full bg-[#00A8E8] text-white shadow-[0_0_12px_rgba(0,168,232,0.5)] hover:scale-110 transition-transform" title="Email">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                    </a>"""

files = glob.glob(f'{build_dir}/**/*.html', recursive=True)
count = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, num_subs = whatsapp_block_re.subn(email_block, content)
    
    if num_subs > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Replaced in {file}")

print(f"Done. Replaced in {count} files.")
