import os
import glob

def fix_mojibake():
    target_dir = r"c:\Users\Jesse\OneDrive\Documentos\Projetos Web\Conexxus\build"
    html_files = glob.glob(os.path.join(target_dir, "**", "*.html"), recursive=True)
    
    # 'Ã¢â‚¬â€' represents '—' in botched utf-8 -> cp1252 conversion
    broken_str = "Ã¢â‚¬â€"
    fixed_str = "—"

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if broken_str in content:
            new_content = content.replace(broken_str, fixed_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed mojibake in {os.path.basename(filepath)}")

if __name__ == "__main__":
    fix_mojibake()
