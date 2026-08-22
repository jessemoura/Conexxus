import re

with open('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/servicos/criacao-de-websites.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

new_content = re.sub(
    r"Your website is your digital home.*?a space where you control your story, your brand and your customer's experience\.",
    "Your website is your digital home, a space where you control your story, your brand and your customer's experience.",
    content,
    flags=re.DOTALL
)

with open('c:/Users/Jesse/OneDrive/Documentos/Projetos Web/Conexxus/build/servicos/criacao-de-websites.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done')
