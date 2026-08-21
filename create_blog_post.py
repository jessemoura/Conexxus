import os
import re

def create_blog_post():
    base_dir = r"c:\Users\Jesse\OneDrive\Documentos\Projetos Web\Conexxus\build"
    blog_dir = os.path.join(base_dir, "blog")
    os.makedirs(blog_dir, exist_ok=True)
    
    blog_index_path = os.path.join(base_dir, "blog.html")
    
    with open(blog_index_path, 'r', encoding='utf-8') as f:
        blog_html = f.read()
        
    # Extract header
    header_match = re.search(r'(<header.*?</header>)', blog_html, re.DOTALL)
    header = header_match.group(1) if header_match else ""
    
    # Extract footer
    footer_match = re.search(r'(<footer.*?</form>.*?</div>\s*</div>\s*</footer>)', blog_html, re.DOTALL)
    # The footer might not have a form, let's just grab from <footer to </footer>
    footer_match = re.search(r'(<footer.*?</footer>)', blog_html, re.DOTALL)
    footer = footer_match.group(1) if footer_match else ""
    
    # Also grab everything from <html> to </header>
    top_match = re.search(r'(<!DOCTYPE html>.*?</header>)', blog_html, re.DOTALL)
    top_html = top_match.group(1) if top_match else ""
    
    # And everything from </footer> to </html>
    bottom_match = re.search(r'(</footer>.*</html>)', blog_html, re.DOTALL)
    bottom_html = bottom_match.group(1) if bottom_match else ""
    
    # Fix paths in top_html and bottom_html for the new depth (from /blog/ to /)
    # They currently point to root from root. So './assets' becomes '../assets', etc.
    top_html = top_html.replace('href="./assets', 'href="../assets')
    top_html = top_html.replace('src="./assets', 'src="../assets')
    top_html = top_html.replace('href="index.html"', 'href="../index.html"')
    top_html = top_html.replace('href="servicos.html"', 'href="../servicos.html"')
    top_html = top_html.replace('href="sobre.html"', 'href="../sobre.html"')
    top_html = top_html.replace('href="portfolio.html"', 'href="../portfolio.html"')
    top_html = top_html.replace('href="blog.html"', 'href="../blog.html"')
    top_html = top_html.replace('href="contato.html"', 'href="../contato.html"')
    top_html = top_html.replace('href="servicos/', 'href="../servicos/')
    top_html = top_html.replace('src="../06-imagens', 'src="../../06-imagens')
    top_html = top_html.replace('href="/"', 'href="../index.html"')
    
    # Update title and meta description
    top_html = re.sub(r'<title>.*?</title>', '<title>Digital Marketing for Small Businesses | Conexxus Swindon</title>', top_html)
    top_html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Discover how digital marketing can help small businesses build a stronger online presence, connect with customers and grow their visibility online.">', top_html)
    
    # Add canonical
    canonical = '<link rel="canonical" href="https://www.conexxus.co.uk/blog/digital-marketing-for-small-businesses" />\n    <script src="https://cdn.tailwindcss.com"></script>'
    top_html = top_html.replace('<script src="https://cdn.tailwindcss.com"></script>', canonical)
    
    # Article content
    article_content = """
    <!-- BREADCRUMBS -->
    <div class="bg-navy pt-32 pb-8">
        <div class="container mx-auto px-6">
            <nav class="text-sm text-blue-200 breadcrumbs">
                <a href="../index.html">Home</a> &gt; <a href="../blog.html">Blog</a> &gt; <span class="text-white">Digital Marketing for Small Businesses</span>
            </nav>
        </div>
    </div>

    <!-- ARTICLE HEADER -->
    <section class="bg-navy text-white pb-16">
        <div class="container mx-auto px-6 max-w-4xl">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">Digital Marketing for Small Businesses: How to Build a Stronger Online Presence</h1>
        </div>
    </section>

    <!-- ARTICLE BODY -->
    <article class="section-padding bg-white">
        <div class="container mx-auto px-6 max-w-3xl text-lg text-gray-700 space-y-6 leading-relaxed">
            <p>For a small business, being online is no longer simply about having a website or a social media account. It is about being present when potential customers are searching, building trust before the first conversation and making it easy for people to understand what your business offers.</p>
            <p>That is where digital marketing becomes valuable.</p>
            <p>At Conexxus, we believe digital presence should create connections. A website, a Google Business Profile, local search visibility, branding and social media should not exist as isolated pieces. Together, they should help connect your business with the people who are already looking for what you offer.</p>
            <p>Based in Swindon, Wiltshire, Conexxus supports small and medium-sized businesses in building professional, clear and connected digital experiences.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">What Does Digital Marketing Mean for a Small Business?</h2>
            <p>Digital marketing covers the different ways a business presents itself, communicates and becomes discoverable online.</p>
            <p>For a small business, this does not necessarily mean being everywhere.</p>
            <p>It means building the right digital foundations so customers can find your business, understand what you do, trust your brand and contact you easily.</p>
            <p>A strong digital presence can include:</p>
            <ul class="list-disc pl-6 space-y-2 mb-6">
                <li>A professional website</li>
                <li>Local SEO</li>
                <li>Google Business Profile</li>
                <li>Consistent branding</li>
                <li>Social media presence</li>
                <li>Clear ways for customers to get in touch</li>
            </ul>
            <p>When these elements work together, your digital presence becomes more than a collection of online profiles. It becomes part of the customer journey.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Why Digital Presence Matters for Small Businesses</h2>
            <p>Before contacting a company, customers often search online.</p>
            <p>They may visit the company website, check its Google presence, look through social media or compare several businesses before deciding who to contact.</p>
            <p>That means your digital presence often creates an impression of your business before you ever speak to the customer.</p>
            <p>A clear and professional presence can help potential customers answer important questions:</p>
            <ul class="list-none space-y-2 font-semibold text-navy my-6 bg-cloud p-6 rounded-xl border border-gray-100">
                <li>&bull; Who are you?</li>
                <li>&bull; What do you offer?</li>
                <li>&bull; Where do you operate?</li>
                <li>&bull; Can I trust this business?</li>
                <li>&bull; How can I contact you?</li>
            </ul>
            <p>The easier these answers are to find, the easier it becomes for a potential customer to take the next step.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Your Website Is the Digital Home of Your Business</h2>
            <p>Social media platforms can help people discover your business, but your website is the space that your business controls.</p>
            <p>A professional small business website should clearly communicate who you are, what you offer and how customers can contact you.</p>
            <p>It should also work properly across desktop, tablet and mobile devices.</p>
            <p>Good website design is not only about appearance. Structure, usability, speed, content and search visibility all contribute to the experience.</p>
            <p>For businesses looking for professional <a href="../servicos/criacao-de-websites.html" class="text-brand font-semibold hover:underline">website design in Swindon</a>, having a website built around both the customer journey and search visibility can create a stronger foundation for the rest of the digital strategy.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Local SEO Helps Customers Find Your Business</h2>
            <p>For businesses serving a particular town, city or region, local visibility can be particularly important.</p>
            <p>Local SEO focuses on helping search engines understand what your business offers and where it operates.</p>
            <p>For example, someone searching for a service in Swindon may use Google to find businesses located in or serving the area.</p>
            <p>A well-structured website, relevant local content and an optimised business presence can help search engines better understand the relationship between your services and your location.</p>
            <p>Local SEO is not about guaranteeing a particular Google position. It is about building stronger signals that make your business more relevant and easier to understand in local searches.</p>
            <p>Learn more about <a href="../servicos/seo-local.html" class="text-brand font-semibold hover:underline">Local SEO in Swindon</a>.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Google Business Profile Connects Search With Your Business</h2>
            <p>Google Business Profile can play an important role in local digital visibility.</p>
            <p>It gives businesses an opportunity to present important information directly within Google Search and Maps, depending on eligibility and Google's platform requirements.</p>
            <p>Business information should be accurate and consistent. This can include details such as services, contact information, business category, opening hours and other relevant information.</p>
            <p>A well-maintained Google Business Profile can complement your website and Local SEO strategy, helping create a more consistent presence across Google. Discover our <a href="../servicos/google-business-profile.html" class="text-brand font-semibold hover:underline">Google Business Profile services</a>.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Branding Creates Recognition and Trust</h2>
            <p>Your brand is more than a logo.</p>
            <p>It includes the colours, typography, visual identity, tone of voice and overall experience people associate with your business.</p>
            <p>For small businesses, consistency matters. When your website, social media and other digital channels share the same visual language and message, the business can appear more organised and professional.</p>
            <p>Strong branding helps people recognise your business and understand how you want to be perceived. Explore <a href="../servicos/branding.html" class="text-brand font-semibold hover:underline">branding for small businesses</a>.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Social Media Keeps the Connection Going</h2>
            <p>While a website provides a permanent digital home for your business, social media provides opportunities for ongoing communication.</p>
            <p>It can help businesses share updates, demonstrate their work, communicate their personality and stay visible to their audience.</p>
            <p>However, social media works best when it forms part of a wider digital presence. The visual identity, tone and message should feel connected to the website and the rest of the brand.</p>
            <p>This creates a more consistent experience wherever a potential customer discovers your business. Learn about <a href="../servicos/gestao-de-redes-sociais.html" class="text-brand font-semibold hover:underline">social media management for small businesses</a>.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">The Most Important Part Is the Connection</h2>
            <p>Digital marketing can involve websites, search engines, social platforms and technology.</p>
            <p>But behind every search, click and message is a person. Someone looking for a service. Someone comparing businesses. Someone trying to solve a problem. Someone deciding who they can trust.</p>
            <p>This is the idea behind Conexxus. We see digital presence as the bridge between a business and the people it wants to reach.</p>
            <p>Technology provides the tools. Strategy creates the direction. But connection is the purpose.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">How the Different Parts of Your Digital Presence Work Together</h2>
            <p>Imagine a potential customer searching online for a service. They discover your business through Google. They visit your website. The website clearly explains what you offer. The branding feels professional and consistent. They may then visit your social media to learn more about the business. Finally, they decide to contact you.</p>
            <p>Each digital touchpoint supports the next. This is why website design, Local SEO, Google Business Profile, branding and social media should not be treated as completely separate elements.</p>
            <p>Together, they create a connected customer journey.</p>

            <h2 class="text-3xl font-bold text-navy mt-12 mb-6">Digital Marketing Support in Swindon and Beyond</h2>
            <p>Conexxus is based in Swindon, Wiltshire, and provides digital marketing support for small and medium-sized businesses.</p>
            <p>Our services include website design, Local SEO, Google Business Profile support, branding and social media management.</p>
            <p>We also provide bilingual support in English and Portuguese and work with businesses across the UK and internationally, including clients in Europe and Brazil.</p>
            <p>Our goal is simple: To help businesses build a digital presence that makes them easier to find, easier to understand and easier to contact.</p>
            
            <div class="mt-16 bg-cloud p-10 rounded-3xl border border-gray-100 text-center">
                <h2 class="text-3xl font-bold text-navy mb-4">Ready to Build a Stronger Digital Presence?</h2>
                <p class="text-gray-600 mb-8 max-w-xl mx-auto">Your business already has a story. The right digital presence helps the right people discover it. Conexxus brings together website design, Local SEO, Google Business Profile, branding and social media to create a clearer connection between businesses and their customers.</p>
                <a href="https://wa.me/447341462757" target="_blank" class="btn-primary inline-flex items-center gap-2 text-lg">
                    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/></svg>
                    Talk to Conexxus on WhatsApp
                </a>
            </div>

            <hr class="my-16 border-gray-200">

            <h2 class="text-3xl font-bold text-navy mb-8">Frequently Asked Questions</h2>
            <div class="space-y-6">
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">What is digital marketing for small businesses?</h3>
                    <p class="text-gray-600">Digital marketing for small businesses includes the online strategies and platforms used to help a business build visibility, communicate its services and connect with potential customers. This can include websites, Local SEO, Google Business Profile, branding and social media.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">Does a small business really need a website?</h3>
                    <p class="text-gray-600">A professional website gives a business its own digital space where customers can learn about its services, understand the brand and find clear contact information. It can also support search visibility and other digital marketing activities.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">What is Local SEO?</h3>
                    <p class="text-gray-600">Local SEO focuses on improving how clearly search engines understand a business, its services and the geographic areas it serves. It is particularly relevant for businesses that depend on customers within a specific town, city or region.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">Can digital marketing help customers find my business on Google?</h3>
                    <p class="text-gray-600">A combination of website optimisation, relevant content, Local SEO and Google Business Profile management can help strengthen a business's presence in Google Search. Results depend on many factors, so no legitimate strategy should guarantee a specific ranking.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">What is Google Business Profile?</h3>
                    <p class="text-gray-600">Google Business Profile is a Google platform that allows eligible businesses to manage information that may appear across Google Search and Maps. Maintaining accurate information can support a business's local digital presence.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">Why is branding important for a small business?</h3>
                    <p class="text-gray-600">Consistent branding helps customers recognise a business and creates a more professional experience across websites, social media and other communication channels.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">Should my website and social media have the same branding?</h3>
                    <p class="text-gray-600">They should feel visually and strategically connected. Consistent colours, typography, imagery, tone and messaging can create a stronger and more recognisable brand experience.</p>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-navy mb-2">Does Conexxus only work with businesses in Swindon?</h3>
                    <p class="text-gray-600">No. Conexxus is based in Swindon, Wiltshire, but supports small and medium-sized businesses across the UK and internationally, including businesses in Europe and Brazil.</p>
                </div>
            </div>
            
        </div>
    </article>
    """
    
    # Let's add structured data (Article and FAQPage)
    structured_data = """
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "Digital Marketing for Small Businesses: How to Build a Stronger Online Presence",
      "author": {
        "@type": "Organization",
        "name": "Conexxus"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Conexxus",
        "logo": {
          "@type": "ImageObject",
          "url": "https://www.conexxus.co.uk/06-imagens/CONEXXUS_Logo_Web_Transparente.png"
        }
      },
      "datePublished": "2026-08-21",
      "description": "Discover how digital marketing can help small businesses build a stronger online presence, connect with customers and grow their visibility online."
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "What is digital marketing for small businesses?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Digital marketing for small businesses includes the online strategies and platforms used to help a business build visibility, communicate its services and connect with potential customers. This can include websites, Local SEO, Google Business Profile, branding and social media."
        }
      },{
        "@type": "Question",
        "name": "Does a small business really need a website?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A professional website gives a business its own digital space where customers can learn about its services, understand the brand and find clear contact information. It can also support search visibility and other digital marketing activities."
        }
      },{
        "@type": "Question",
        "name": "What is Local SEO?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Local SEO focuses on improving how clearly search engines understand a business, its services and the geographic areas it serves. It is particularly relevant for businesses that depend on customers within a specific town, city or region."
        }
      },{
        "@type": "Question",
        "name": "Can digital marketing help customers find my business on Google?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A combination of website optimisation, relevant content, Local SEO and Google Business Profile management can help strengthen a business's presence in Google Search. Results depend on many factors, so no legitimate strategy should guarantee a specific ranking."
        }
      },{
        "@type": "Question",
        "name": "What is Google Business Profile?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Google Business Profile is a Google platform that allows eligible businesses to manage information that may appear across Google Search and Maps. Maintaining accurate information can support a business's local digital presence."
        }
      },{
        "@type": "Question",
        "name": "Why is branding important for a small business?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Consistent branding helps customers recognise a business and creates a more professional experience across websites, social media and other communication channels."
        }
      },{
        "@type": "Question",
        "name": "Should my website and social media have the same branding?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "They should feel visually and strategically connected. Consistent colours, typography, imagery, tone and messaging can create a stronger and more recognisable brand experience."
        }
      },{
        "@type": "Question",
        "name": "Does Conexxus only work with businesses in Swindon?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Conexxus is based in Swindon, Wiltshire, but supports small and medium-sized businesses across the UK and internationally, including businesses in Europe and Brazil."
        }
      }]
    }
    </script>
    """
    
    full_html = top_html + article_content + footer + structured_data + bottom_html
    
    with open(os.path.join(blog_dir, "digital-marketing-for-small-businesses.html"), 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print("Created blog post HTML.")

if __name__ == "__main__":
    create_blog_post()
