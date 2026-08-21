import os
import glob

def fix_dropdown():
    target_dir = r"c:\Users\Jesse\OneDrive\Documentos\Projetos Web\Conexxus\build"
    
    # We will search for all .html files
    html_files = glob.glob(os.path.join(target_dir, "**", "*.html"), recursive=True)
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Add click outside
        content = content.replace(
            '@mouseenter="open = true" @mouseleave="open = false"',
            '@mouseenter="open = true" @mouseleave="open = false" @click.outside="open = false"'
        )
        
        # 2. Add style="display: none;" to prevent flashing or staying open without Alpine
        content = content.replace(
            'x-show="open" x-transition.opacity',
            'x-show="open" style="display: none;" x-transition.opacity'
        )
        
        # Just in case they click the link itself on mobile and it toggles
        # Add a click handler to toggle on touch devices
        # Actually hover handles touch on iOS, but maybe a click is better.
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed dropdown in {os.path.basename(filepath)}")

if __name__ == "__main__":
    fix_dropdown()
