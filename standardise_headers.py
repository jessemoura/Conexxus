import os
import glob
import re

def standardize_headers():
    target_dir = r"c:\Users\Jesse\OneDrive\Documentos\Projetos Web\Conexxus\build"
    index_path = os.path.join(target_dir, "index.html")
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
    if not header_match:
        print("Could not find header in index.html")
        return
        
    master_header = header_match.group(1)
    
    html_files = glob.glob(os.path.join(target_dir, "**", "*.html"), recursive=True)
    
    for filepath in html_files:
        if os.path.basename(filepath) == "index.html":
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_header_match = re.search(r'(<header.*?</header>)', content, re.DOTALL)
        if not old_header_match:
            print(f"Could not find header in {filepath}")
            continue
            
        basename = os.path.basename(filepath)
        is_subdir = "\\servicos\\" in filepath
        
        # Prepare header string for this specific file
        file_header = master_header
        
        # Adjust paths if we are in a subdirectory (build/servicos/*)
        if is_subdir:
            # Add '../' to all root links
            file_header = file_header.replace('href="index.html"', 'href="../index.html"')
            file_header = file_header.replace('href="servicos.html"', 'href="../servicos.html"')
            file_header = file_header.replace('href="sobre.html"', 'href="../sobre.html"')
            file_header = file_header.replace('href="portfolio.html"', 'href="../portfolio.html"')
            file_header = file_header.replace('href="blog.html"', 'href="../blog.html"')
            file_header = file_header.replace('href="contato.html"', 'href="../contato.html"')
            file_header = file_header.replace('href="servicos/', 'href="../servicos/')
            # Image path: index.html has src="../06-imagens/...", in subdir it should be src="../../06-imagens/..."
            file_header = file_header.replace('src="../06-imagens/', 'src="../../06-imagens/')
            # the logo link <a href="/"> is fine, or <a href="../index.html">
            file_header = file_header.replace('href="/"', 'href="../index.html"')
        
        # Replace the old header with the new one
        new_content = content[:old_header_match.start()] + file_header + content[old_header_match.end():]
        
        # Reset all links to hover:text-cyan (naive string replace)
        new_content = new_content.replace('class="text-cyan transition-colors"', 'class="hover:text-cyan transition-colors"')
        
        # Set active class for the current page
        if basename == "sobre.html":
            new_content = new_content.replace('href="sobre.html" class="hover:text-cyan', 'href="sobre.html" class="text-cyan')
        elif basename == "portfolio.html":
            new_content = new_content.replace('href="portfolio.html" class="hover:text-cyan', 'href="portfolio.html" class="text-cyan')
        elif basename == "blog.html":
            new_content = new_content.replace('href="blog.html" class="hover:text-cyan', 'href="blog.html" class="text-cyan')
        elif basename == "contato.html":
            new_content = new_content.replace('href="contato.html" class="hover:text-cyan', 'href="contato.html" class="text-cyan')
        elif basename == "servicos.html" or is_subdir:
            new_content = new_content.replace('href="servicos.html" class="flex items-center gap-1 hover:text-cyan', 'href="servicos.html" class="flex items-center gap-1 text-cyan')
            if is_subdir:
                new_content = new_content.replace('href="../servicos.html" class="flex items-center gap-1 hover:text-cyan', 'href="../servicos.html" class="flex items-center gap-1 text-cyan')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated header in {filepath}")
        
    print("Done")

if __name__ == "__main__":
    standardize_headers()
