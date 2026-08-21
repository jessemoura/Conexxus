# Blueprint — Conexxus Digital Marketing Website

Este documento descreve fielmente a estrutura de cada página, com base nos arquivos de referência visual disponíveis na pasta `/04-referencia-visual/` (template Elementor `homepage.json`, imagens WebP e `GUIA-DE-USO.txt`), combinados com a copy aprovada (`/03-copy/copy-site.md`) e a arquitetura SEO (`/02-arquitetura-seo/arquitetura.md`).

---

## Estilos Globais

### Paleta de Cores
| Token | Hex | Uso |
|-------|-----|-----|
| Navy | #003A70 | Fundos escuros, header, footer |
| Brand Blue (Primária) | #0066B3 | Botões primários, links, destaques |
| Digital Cyan | #00A8E8 | Acentos, ícones, hover |
| Signal Blue | #70D7FF | Gradientes, detalhes secundários |
| Graphite (Secundária) | #181A1B | Texto principal, fundos escuros |
| Cloud (Fundo) | #F4F7FA | Fundo de seções alternadas |
| Branco | #FFFFFF | Fundo principal, texto sobre escuro |

### Proporção de Cores
- 60% Branco / Cloud
- 25% Navy / Graphite
- 10% Brand Blue
- 5% Cyan / Signal Blue

### Tipografia
- Fonte principal: Sem referência explícita no template (utilizar fonte moderna como Inter ou similar)
- H1: Grande, bold, cor branca sobre fundos escuros ou Graphite sobre fundos claros
- H2: Médio-grande, bold
- H3: Médio, semibold
- Corpo: Tamanho regular, cor Graphite
- Subtítulo/Lead: Tamanho ligeiramente maior que corpo, peso regular

### Elementos de Design (extraídos do template JSON)
- Border-radius: 15px em cards e imagens
- Box-shadow: `0 0 60px rgba(0, 0, 0, 0.1)` em cards e containers elevados
- Imagens: object-fit cover, saturação levemente reduzida (75%) em cards de serviço
- Overlays: Gradientes escuros sobre imagens de fundo (hero e seções de destaque)
- Botões: Border-radius arredondado (~30px), estilo sólido com variante outline
- Ícones: Circulares (border-radius 50%), posicionados como badges flutuantes (position absolute) sobre cards

### Imagens
- Formato: WebP
- Dimensões: 1536 × 1024 px
- Orientação: Horizontal
- Perfil de cor: sRGB
- Lazy loading: Sim para todas, exceto hero

---

## HEADER (Componente Global)

Ordem dos elementos (da esquerda para a direita):
1. **Logo** — `CONEXXUS_Logo_Web_Transparente.png` (alinhado à esquerda)
2. **Menu de navegação** — Links horizontais:
   - Home
   - Serviços (com submenu dropdown para as 5 páginas individuais)
   - Sobre
   - Portfólio
   - Blog
   - Contato
3. **Botão CTA** — "Talk to Us on WhatsApp" (alinhado à direita, estilo botão primário Brand Blue)

Comportamento:
- Fixo no topo (sticky)
- Fundo transparente sobre hero, transição para fundo Navy/Graphite ao rolar
- Menu responsivo: hamburger em mobile e tablet

---

## FOOTER (Componente Global)

Ordem dos elementos (de cima para baixo):

1. **Container principal** (fundo Navy #003A70)
   - **Coluna 1 — Marca**
     - Logo branco/transparente
     - Texto breve descritivo da empresa
     - Ícones de redes sociais: Instagram, WhatsApp
   - **Coluna 2 — Links Rápidos**
     - Home
     - Serviços
     - Sobre
     - Portfólio
     - Blog
     - Contato
   - **Coluna 3 — Serviços**
     - Website Design
     - Local SEO
     - Google Business Profile
     - Branding
     - Social Media Management
   - **Coluna 4 — Contato**
     - Ícone telefone + 07341 462757
     - Ícone WhatsApp + +44 7341 462757
     - Ícone localização + Swindon, Wiltshire, UK
     - Ícone Instagram + @conexxus.co.uk

2. **Barra inferior** (fundo mais escuro ou borda superior)
   - "© 2025 Conexxus Digital Marketing. All rights reserved."
   - Link: Privacy Policy

---

## PÁGINA: HOME (/)

### Seção 1 — Hero
- **Tipo:** Hero fullscreen com imagem de fundo
- **Fundo:** Imagem `conexxus-digital-marketing-small-business-hero.webp` com overlay gradiente escuro (Navy → transparente, diagonal 135°)
- **Lazy loading:** NÃO (carregamento prioritário)
- **Layout:** Coluna única, conteúdo alinhado à esquerda, largura ~50% do container
- **Padding:** Grande (7em topo, 10em base desktop; responsivo para tablet e mobile)
- **Conteúdo:**
  1. H1: "Digital Marketing Agency in Swindon for Small Businesses"
  2. Subtítulo (div): Texto descritivo sobre os serviços
  3. Botão primário: "Talk to Us on WhatsApp" (fundo branco, texto escuro)
  4. Botão secundário: "Explore Our Services" (outline)
  5. Texto de apoio: "Based in Swindon, Wiltshire..."

### Seção 2 — Barra de Contato / Credibilidade
- **Tipo:** Barra flutuante sobreposta (margem negativa sobre hero, -6em)
- **Layout:** Container com border-radius 15px, box-shadow, fundo branco
- **Estrutura:** Duas áreas lado a lado (row wrap)
  - **Esquerda (35%):** Fundo com imagem + overlay gradiente. Dois icon-boxes empilhados:
    1. Ícone telefone + "Customer Services" + número
    2. Ícone WhatsApp + "WhatsApp" + número
  - **Direita (65%):** Barra com 4 credenciais em texto:
    - Based in Swindon, Wiltshire
    - Support in English & Portuguese
    - Services for small and medium-sized businesses
    - UK, Brazil & European market support

### Seção 3 — Quem Somos (About Preview)
- **Tipo:** Texto + Imagem lado a lado
- **Layout:** Row, sem gap
- **Esquerda (45%):** Conteúdo textual
  1. H6/Tag: "Who we are"
  2. H2: "Digital Marketing Support for Small Businesses in Swindon"
  3. Subtítulo (div): Texto descritivo
  4. Divisor decorativo (linha colorida)
  5. Icon-box 1: Ícone + título + descrição (serviço/diferencial)
  6. Icon-box 2: Ícone + título + descrição (serviço/diferencial)
- **Direita (55%):** Imagem
  1. Imagem principal: `conexxus-digital-marketing-agency-swindon.webp` (550px altura, border-radius 15px, object-fit cover)
  2. Badge circular flutuante (position absolute, canto inferior direito): Número destaque + texto (ex: indicador de experiência)
- **Botão:** "About Conexxus"

### Seção 4 — Logos/Parceiros (Barra de Confiança)
- **Tipo:** Carrossel/Grid de logos
- **Fundo:** Cloud (#F4F7FA)
- **Layout:** Título centralizado + linha de logos
  1. H2 centralizado: Texto de credibilidade
  2. Grid horizontal: 6–7 logos em linha (19% cada, wrap em tablet/mobile)
     - Cada logo: Altura 70px, object-fit contain, fundo com border-radius 7px, padding 14px, filtro brightness

### Seção 5 — Bloco de Valor / Proposta
- **Tipo:** Texto centralizado sobre imagem de fundo
- **Fundo:** Imagem com overlay escuro
- **Layout:** Container centralizado (max-width ~600px)
  1. H6/Tag: "Our Value"
  2. H2: Título de proposta de valor
  3. Texto (text-editor): Descrição

### Seção 6 — Testemunho / Prova Social
- **Tipo:** Galeria de imagens + Card de depoimento
- **Layout:** Row, 50/50, com border inferior
- **Esquerda (50%):** Grid de imagens (2 colunas)
  - Imagem grande (48%, 500px altura, border-radius 15px)
  - Coluna com imagem menor (240px) + card de depoimento sobreposto (margem negativa à esquerda)
    - Card: Fundo branco, border-radius 15px, box-shadow, contém:
      1. Estrelas de avaliação (star-rating, 4/5)
      2. Texto de depoimento (com borda esquerda colorida)
      3. Nome do cliente + cargo (icon-box)
- **Direita (50%):** Conteúdo textual
  1. H2: Título
  2. Texto descritivo
  3. Icon-box: Contato/telefone
  4. Icon-box: Booking/contato
  5. Botão: "Discover more"

### Seção 7 — Serviços (Cards)
- **Tipo:** Grid de service cards
- **Fundo:** Cloud (#F4F7FA)
- **Layout:** Cabeçalho centralizado + Grid 3 colunas (wrap)
- **Cabeçalho:**
  1. H6/Tag: "Our Services"
  2. H2: "Digital Marketing Services for Small Businesses"
  3. Subtítulo (div): Texto descritivo
- **Cards (6 ao todo, 32% largura cada, 49% em tablet):**
  Cada card contém:
  1. Imagem de capa (250px altura, object-fit cover, saturação reduzida, border-radius 15px topo)
  2. Ícone circular flutuante (position absolute, badge sobre a transição imagem/texto)
  3. H3: Nome do serviço
  4. Subtítulo (div): Descrição
  5. Botão "Learn more →" (tamanho xs, com ícone seta)
  - Card: Fundo branco, border-radius 15px, box-shadow, overflow hidden, gap 0

  **Serviços nos cards:**
  - Website Design → `conexxus-website-design-services.webp`
  - Local SEO → `conexxus-local-seo-small-business.webp`
  - Google Business Profile → `conexxus-google-business-profile-services.webp`
  - Branding → `conexxus-branding-brand-identity.webp`
  - Social Media Management → `conexxus-social-media-management.webp`
  - (6º card: reservado ou duplicável conforme necessidade)

### Seção 8 — Como Funciona (How It Works)
- **Tipo:** Processo / Steps
- **Layout:** Cabeçalho + steps sequenciais
  1. H6/Tag: "How it works"
  2. H2: "How We Work"
  3. Steps numerados (1–5):
     - 1. Understand Your Business
     - 2. Identify the Priority
     - 3. Build the Digital Foundation
     - 4. Review and Refine
     - 5. Maintain Your Presence
  4. Botão CTA: "Discuss Your Business on WhatsApp"

### Seção 9 — Bloco CTA Intermediário
- **Tipo:** Banner com imagem de fundo
- **Fundo:** Imagem com overlay escuro
- **Conteúdo centralizado:**
  1. H2: Título motivacional
  2. Texto descritivo

### Seção 10 — Por que nos Escolher (Why Choose Us)
- **Tipo:** Grid de benefícios
- **Layout:** Cabeçalho + grid de items
  1. H6/Tag: "WHY CHOOSE US"
  2. H2: "Why Choose Conexxus"
  3. Grid de benefícios (ícone + título + descrição):
     - Digital Solutions for Small Businesses
     - Bilingual Support
     - Local Knowledge
     - International Support
     - Connected Digital Presence
     - Direct Communication

### Seção 11 — Depoimentos (Testimonials Carousel)
- **Tipo:** Carrossel de depoimentos
- **Layout:**
  1. H6/Tag: "Testimonial"
  2. H2: "Client Feedback & Reviews"
  3. Slides com depoimentos (quando disponíveis)
  - Nota: Seção placeholder até que depoimentos reais sejam adicionados

### Seção 12 — FAQ Estratégico
- **Tipo:** Accordion / Lista de perguntas expandíveis
- **Layout:**
  1. H2: "Frequently Asked Questions"
  2. 10 perguntas em formato accordion (pergunta clicável → resposta expande)

### Seção 13 — CTA Final
- **Tipo:** Banner CTA
- **Fundo:** Imagem ou gradiente escuro
- **Conteúdo centralizado:**
  1. H2: "Ready to Strengthen Your Digital Presence?"
  2. Texto de apoio
  3. Botão CTA: "Talk to Conexxus on WhatsApp"
  4. Subtexto: "Supporting small businesses from Swindon to international markets."

### Seção 14 — Cookie Consent Banner
- **Tipo:** Barra fixa no fundo da tela
- **Conteúdo:**
  1. Texto sobre cookies
  2. Botão "Accept"
  3. Botão "Decline"
  4. Link "Learn more" → /privacidade

---

## PÁGINA: SOBRE (/sobre)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto com fundo escuro ou imagem
- **Conteúdo:**
  1. H1: "About Conexxus Digital Marketing in Swindon"

### Seção 2 — Nossa História
- **Tipo:** Texto + Imagem
- **Layout:** Dois blocos lado a lado
- **Esquerda:** Texto narrativo (4 parágrafos sobre a fundação e missão)
- **Direita:** Imagem `conexxus-digital-marketing-agency-swindon.webp`

### Seção 3 — Missão
- **Tipo:** Bloco de texto destacado
- **Conteúdo:**
  1. H2: "Our Mission"
  2. Texto da missão

### Seção 4 — Valores
- **Tipo:** Grid de icon-boxes
- **Conteúdo:**
  1. H2: "Our Values"
  2. 5 valores em grid (ícone + título + descrição):
     - Clarity
     - Professionalism
     - Connection
     - Consistency
     - Accessibility

### Seção 5 — Fundador
- **Tipo:** Bloco Perfil (imagem + texto)
- **Layout:** Imagem à esquerda + texto à direita
- **Conteúdo:**
  1. H2: "Meet the Founder"
  2. Imagem: `conexxus-founder-digital-marketing-swindon.webp`
  3. Nome (pendente) + Cargo
  4. Descrição do fundador

### Seção 6 — Equipe
- **Tipo:** Bloco de texto (placeholder)
- **Conteúdo:**
  1. H2: "Our Team"
  2. Texto indicando que dados verificados serão adicionados

### Seção 7 — Certificações
- **Tipo:** Bloco de texto (placeholder)
- **Conteúdo:**
  1. H2: "Qualifications and Certifications"
  2. Texto indicando que certificações verificadas serão adicionadas

### Seção 8 — Atendimento Bilíngue
- **Tipo:** Texto + Imagem
- **Conteúdo:**
  1. H2: "Bilingual Digital Marketing Support"
  2. Texto sobre suporte em inglês e português
  3. Imagem: `conexxus-bilingual-digital-marketing-support.webp`

### Seção 9 — Atuação Internacional
- **Tipo:** Texto + Imagem
- **Conteúdo:**
  1. H2: "Local Base, International Perspective"
  2. Texto sobre área de atuação
  3. Imagem: `conexxus-international-client-support.webp`

### Seção 10 — CTA Final
- **Tipo:** Banner CTA
- **Conteúdo:**
  1. Botão CTA: "Talk to Conexxus on WhatsApp"

---

## PÁGINA: SERVIÇOS (/servicos)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Digital Marketing Services in Swindon"
  2. Texto introdutório

### Seção 2 — Grid de Serviços
- **Tipo:** Cards de serviço (mesmo padrão da Home)
- **Layout:** Grid responsivo
- **Cards (5):**
  1. Website Design → CTA: "Explore Website Design"
  2. Local SEO → CTA: "Explore Local SEO"
  3. Google Business Profile → CTA: "Explore Google Business Profile"
  4. Branding → CTA: "Explore Branding"
  5. Social Media Management → CTA: "Explore Social Media Management"

---

## PÁGINA: SERVIÇO INDIVIDUAL (template para cada um dos 5 serviços)

Slugs:
- /servicos/criacao-de-websites
- /servicos/seo-local
- /servicos/google-business-profile
- /servicos/branding
- /servicos/gestao-de-redes-sociais

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto com imagem de fundo do serviço
- **Conteúdo:**
  1. H1: Título específico do serviço (ver arquitetura.md)

### Seção 2 — O que é
- **Tipo:** Texto descritivo
- **Conteúdo:**
  1. Título introdutório
  2. 1–2 parágrafos explicativos

### Seção 3 — Para quem é
- **Tipo:** Lista com ícones ou bullets
- **Conteúdo:**
  1. H2: "Who Is This Service For?"
  2. Lista de perfis de clientes

### Seção 4 — Como funciona
- **Tipo:** Steps / Processo numerado
- **Conteúdo:**
  1. H2: "How [Service] Works"
  2. Steps numerados (3–5 etapas)

### Seção 5 — Benefícios
- **Tipo:** Lista ou grid de ícones
- **Conteúdo:**
  1. H2: "Benefits of [Service]"
  2. Lista de benefícios

### Seção 6 — FAQ do Serviço
- **Tipo:** Accordion
- **Conteúdo:**
  1. 5 perguntas específicas do serviço

### Seção 7 — CTA
- **Tipo:** Banner CTA
- **Conteúdo:**
  1. Botão: "Discuss [Service] on WhatsApp"

### Imagens por serviço:
| Serviço | Imagem |
|---------|--------|
| Website Design | `conexxus-website-design-services.webp` |
| SEO Local | `conexxus-local-seo-small-business.webp` |
| Google Business Profile | `conexxus-google-business-profile-services.webp` |
| Branding | `conexxus-branding-brand-identity.webp` |
| Social Media Management | `conexxus-social-media-management.webp` |

---

## PÁGINA: PORTFÓLIO (/portfolio)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Digital Marketing & Website Projects"

### Seção 2 — Introdução
- **Tipo:** Texto + Imagem
- **Conteúdo:**
  1. H2: "Digital Work Built Around Real Businesses"
  2. Texto descritivo
  3. Imagem: `conexxus-digital-projects-portfolio.webp`

### Seção 3 — Grid de Projetos
- **Tipo:** Grid de cards de projeto (placeholder)
- **Estrutura sugerida por card:**
  1. Screenshot do projeto
  2. Nome do cliente/empresa
  3. Setor
  4. Serviço prestado
  5. Objetivo
  6. Link do site (quando autorizado)
  7. Resultado/feedback (quando verificado)

### Seção 4 — CTA
- **Tipo:** Banner CTA
- **Conteúdo:**
  1. Botão: "Discuss Your Project on WhatsApp"

---

## PÁGINA: CONTATO (/contato)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Contact Conexxus Digital Marketing in Swindon"
  2. Texto introdutório

### Seção 2 — Informações de Contato
- **Tipo:** Grid de icon-boxes
- **Layout:** Blocos com ícones
  1. WhatsApp: +44 7341 462757 + Botão CTA "Start a WhatsApp Conversation"
  2. Telephone: 07341 462757
  3. Instagram: @conexxus.co.uk
  4. Location: Swindon, Wiltshire, United Kingdom

### Seção 3 — Detalhes Adicionais
- **Tipo:** Texto informativo
- **Conteúdo:**
  1. Full Address: Pendente
  2. Opening Hours: Pendente
  3. How to Reach Us: WhatsApp como canal principal, sem formulário
  4. Areas Served: Swindon, Wiltshire + remoto UK, Brasil, Europa

### Seção 4 — Mapa
- **Tipo:** Embed de mapa
- **Conteúdo:** Google Maps (pendente confirmação do endereço)

### Seção 5 — Imagem de apoio
- **Tipo:** Imagem
- **Conteúdo:** `conexxus-small-business-whatsapp-support.webp`

---

## PÁGINA: BLOG (/blog)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Digital Marketing Insights for Small Businesses"
  2. Texto introdutório

### Seção 2 — Grid de Posts
- **Tipo:** Grid de cards de blog
- **Layout:** 3 colunas (wrap)
- **Cada card:**
  1. Imagem de capa
  2. Categoria/Cluster
  3. Título do post (link)
  4. Resumo/excerpt
  5. Data
  6. Botão "Read more"

### Seção 3 — Author Box (presente nos posts individuais)
- **Tipo:** Bloco de autor
- **Conteúdo:**
  1. Nome do fundador (pendente)
  2. Cargo: Founder, Conexxus
  3. Bio curta
  4. Foto (quando disponível)

---

## PÁGINA: FAQ (/faq)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Digital Marketing FAQs for Small Businesses in Swindon"

### Seção 2 — FAQs por Categoria
- **Tipo:** Accordions agrupados por categoria
- **Categorias:**
  1. **Atendimento** (perguntas 1–5)
  2. **Website Design** (perguntas 6–9)
  3. **SEO & Google** (perguntas 10–13)
  4. **Branding & Social Media** (perguntas 14–16)
  5. **Preços e Pagamentos** (perguntas 17–20)

---

## PÁGINA: POLÍTICA DE PRIVACIDADE (/privacidade)

### Seção 1 — Hero Interno
- **Tipo:** Hero compacto
- **Conteúdo:**
  1. H1: "Privacy Policy — Conexxus Digital Marketing"
  2. "Last updated: [data]"

### Seção 2 — Conteúdo da Política
- **Tipo:** Texto longo formatado
- **Estrutura:** 15 seções numeradas com H2:
  1. Data Controller
  2. Information We May Process
  3. WhatsApp Communications
  4. Cookies
  5. Purposes of Processing
  6. Legal Basis
  7. Sharing of Information
  8. International Processing
  9. Data Retention
  10. Your Rights
  11. How to Exercise Your Rights
  12. External Links
  13. Security
  14. Changes to This Policy
  15. Contact
