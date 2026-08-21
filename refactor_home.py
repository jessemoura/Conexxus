import os

new_body = """    <!-- HERO SECTION -->
    <section class="relative min-h-[90vh] flex items-center pt-24 pb-32">
        <div class="absolute inset-0 z-0">
            <img src="../06-imagens/conexxus-digital-marketing-small-business-hero.webp" alt="Small business digital marketing" class="w-full h-full object-cover">
            <div class="absolute inset-0 hero-overlay"></div>
        </div>

        <div class="container mx-auto px-6 relative z-10 animate-fade-in-up">
            <div class="max-w-3xl">
                <p class="text-xl md:text-2xl text-cyan font-bold tracking-widest uppercase mb-4 drop-shadow-md">Connecting businesses with people.</p>
                <h1 class="text-4xl md:text-5xl lg:text-7xl font-bold text-white leading-tight mb-6">
                    Digital Marketing Agency in Swindon
                </h1>
                <p class="text-xl md:text-2xl text-blue-50 mb-10 leading-relaxed font-light">
                    Conexxus helps small businesses build a stronger digital presence through websites, local visibility and branding &mdash; creating meaningful connections between businesses and the people looking for them.
                </p>
                
                <div class="flex flex-col sm:flex-row gap-4">
                    <a href="https://wa.me/447341462757" class="btn-primary shadow-xl shadow-blue-500/20 text-center justify-center py-4 text-lg">Let's Connect</a>
                    <a href="/servicos" class="btn-secondary text-center justify-center py-4 text-lg">Explore Our Services</a>
                </div>
            </div>
        </div>
    </section>

    <!-- MANIFESTO SECTION -->
    <section class="section-padding bg-white relative">
        <div class="container mx-auto px-6 max-w-4xl text-center">
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-8 text-navy">More Than Digital Marketing. We Build Connections.</h2>
            <div class="text-lg md:text-xl text-gray-600 space-y-6 leading-relaxed mb-12">
                <p>Every business has a story.</p>
                <p>A reason it started, people behind it, and customers it hopes to reach. But in an increasingly digital world, even great businesses can struggle to be seen by the right people.</p>
                <p>That's where Conexxus comes in.</p>
                <p>We combine strategy, design and technology to help businesses build a stronger digital presence and connect with the people searching for what they offer.</p>
            </div>
            <div class="p-8 bg-cloud rounded-2xl border border-gray-100 shadow-sm inline-block">
                <p class="text-xl md:text-2xl font-bold text-navy italic">Behind every search is a person.<br>Behind every business is a story worth discovering.</p>
            </div>
        </div>
    </section>

    <!-- SERVICES CARDS SECTION -->
    <section class="section-padding bg-cloud relative overflow-hidden">
        <div class="container mx-auto px-6 relative z-10">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-6 text-navy">
                    Digital Marketing Services in Swindon
                </h2>
                <p class="text-lg text-gray-600">
                    Everything your business needs to build a professional, visible and connected digital presence.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Service 1: Website Design -->
                <div class="service-card group relative flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 p-8 hover:-translate-y-2 transition-transform duration-300">
                    <div class="flex flex-col flex-grow relative z-10">
                        <h3 class="text-2xl font-bold mb-4 text-navy group-hover:text-brand transition-colors">Website Design</h3>
                        <p class="text-gray-600 mb-8 flex-grow">Professional, responsive websites designed to turn your digital presence into a place where customers can discover, understand and connect with your business.</p>
                        <a href="/servicos/criacao-de-websites" class="inline-flex items-center text-brand font-semibold hover:text-cyan transition-colors">
                            Explore Website Design 
                            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>

                <!-- Service 2: Local SEO -->
                <div class="service-card group relative flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 p-8 hover:-translate-y-2 transition-transform duration-300">
                    <div class="flex flex-col flex-grow relative z-10">
                        <h3 class="text-2xl font-bold mb-4 text-navy group-hover:text-brand transition-colors">Local SEO</h3>
                        <p class="text-gray-600 mb-8 flex-grow">Help the right people find your business when they search for services like yours in their local area.</p>
                        <a href="/servicos/seo-local" class="inline-flex items-center text-brand font-semibold hover:text-cyan transition-colors">
                            Explore Local SEO 
                            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>

                <!-- Service 3: Google Business Profile -->
                <div class="service-card group relative flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 p-8 hover:-translate-y-2 transition-transform duration-300">
                    <div class="flex flex-col flex-grow relative z-10">
                        <h3 class="text-2xl font-bold mb-4 text-navy group-hover:text-brand transition-colors">Google Business Profile</h3>
                        <p class="text-gray-600 mb-8 flex-grow">Build a stronger presence on Google with clear, accurate and professionally managed business information.</p>
                        <a href="/servicos/google-business-profile" class="inline-flex items-center text-brand font-semibold hover:text-cyan transition-colors">
                            Explore Google Business Profile 
                            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>

                <!-- Service 4: Branding -->
                <div class="service-card group relative flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 p-8 hover:-translate-y-2 transition-transform duration-300">
                    <div class="flex flex-col flex-grow relative z-10">
                        <h3 class="text-2xl font-bold mb-4 text-navy group-hover:text-brand transition-colors">Branding</h3>
                        <p class="text-gray-600 mb-8 flex-grow">Create a clear and consistent identity that helps people recognise, remember and trust your business.</p>
                        <a href="/servicos/branding" class="inline-flex items-center text-brand font-semibold hover:text-cyan transition-colors">
                            Explore Branding 
                            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>

                <!-- Service 5: Social Media -->
                <div class="service-card group relative flex flex-col bg-white rounded-2xl overflow-hidden shadow-lg border border-gray-100 p-8 hover:-translate-y-2 transition-transform duration-300">
                    <div class="flex flex-col flex-grow relative z-10">
                        <h3 class="text-2xl font-bold mb-4 text-navy group-hover:text-brand transition-colors">Social Media Management</h3>
                        <p class="text-gray-600 mb-8 flex-grow">Build a consistent social presence that keeps your business connected with its audience.</p>
                        <a href="/servicos/gestao-de-redes-sociais" class="inline-flex items-center text-brand font-semibold hover:text-cyan transition-colors">
                            Explore Social Media 
                            <svg class="w-4 h-4 ml-2 transform group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                        </a>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- PROBLEM + PURPOSE -->
    <section class="section-padding bg-navy text-white relative overflow-hidden">
        <div class="container mx-auto px-6 relative z-10 flex flex-col lg:flex-row items-center gap-16">
            <div class="lg:w-1/2">
                <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-8">Being Online Isn't Enough.</h2>
                <div class="text-lg text-blue-100 space-y-6 leading-relaxed font-light mb-10">
                    <p>Your customers move between Google, websites and social media before deciding who to contact.</p>
                    <p>If your business is difficult to find, unclear online or inconsistent across different platforms, that connection can be lost before the first conversation even begins.</p>
                    <p>Conexxus brings these digital touchpoints together to create a clearer journey from search to connection.</p>
                </div>
                <div class="inline-block border-l-4 border-cyan pl-6 py-2">
                    <p class="text-2xl font-bold text-white tracking-wide">Be found. Be understood. Be remembered.</p>
                </div>
            </div>
            <div class="lg:w-1/2 w-full">
                <img src="../06-imagens/conexxus-digital-marketing-agency-swindon.webp" alt="Digital Marketing Connections" class="w-full h-[400px] object-cover rounded-2xl shadow-2xl opacity-90">
            </div>
        </div>
    </section>

    <!-- WHY CHOOSE US -->
    <section class="section-padding bg-white relative">
        <div class="container mx-auto px-6 max-w-5xl">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-navy">Why Businesses Choose Conexxus</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
                <div class="flex gap-6 items-start">
                    <div class="w-12 h-12 rounded-full bg-cloud flex items-center justify-center flex-shrink-0 text-brand font-bold text-xl">1</div>
                    <div>
                        <h4 class="text-xl font-bold mb-3 text-navy">Built for Small Businesses</h4>
                        <p class="text-gray-600 leading-relaxed">Practical digital solutions created around the real needs of small and medium-sized businesses.</p>
                    </div>
                </div>

                <div class="flex gap-6 items-start">
                    <div class="w-12 h-12 rounded-full bg-cloud flex items-center justify-center flex-shrink-0 text-brand font-bold text-xl">2</div>
                    <div>
                        <h4 class="text-xl font-bold mb-3 text-navy">One Connected Digital Presence</h4>
                        <p class="text-gray-600 leading-relaxed">Website, local visibility, branding and social media working together instead of as disconnected pieces.</p>
                    </div>
                </div>

                <div class="flex gap-6 items-start">
                    <div class="w-12 h-12 rounded-full bg-cloud flex items-center justify-center flex-shrink-0 text-brand font-bold text-xl">3</div>
                    <div>
                        <h4 class="text-xl font-bold mb-3 text-navy">English & Portuguese</h4>
                        <p class="text-gray-600 leading-relaxed">Bilingual support that makes communication simpler for businesses operating across different markets.</p>
                    </div>
                </div>

                <div class="flex gap-6 items-start">
                    <div class="w-12 h-12 rounded-full bg-cloud flex items-center justify-center flex-shrink-0 text-brand font-bold text-xl">4</div>
                    <div>
                        <h4 class="text-xl font-bold mb-3 text-navy">Local Roots. International Reach.</h4>
                        <p class="text-gray-600 leading-relaxed">Based in Swindon, supporting businesses across the UK and international markets.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="section-padding bg-cloud relative">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-4xl font-bold text-navy">From Business to Connection</h2>
            </div>
            
            <div class="space-y-6 relative before:absolute before:inset-0 before:ml-6 before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-brand before:to-cyan">
                
                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-12 h-12 rounded-full border-4 border-cloud bg-brand text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 font-bold text-xl">1</div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                        <h4 class="text-xl font-bold text-navy mb-2">Understand</h4>
                        <p class="text-gray-600">We learn about your business, your customers and where your digital presence needs to improve.</p>
                    </div>
                </div>

                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-12 h-12 rounded-full border-4 border-cloud bg-brand text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 font-bold text-xl">2</div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                        <h4 class="text-xl font-bold text-navy mb-2">Build</h4>
                        <p class="text-gray-600">We create the digital foundations your business needs — from websites and branding to local visibility.</p>
                    </div>
                </div>

                <div class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active">
                    <div class="flex items-center justify-center w-12 h-12 rounded-full border-4 border-cloud bg-brand text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 font-bold text-xl">3</div>
                    <div class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] bg-white p-8 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow">
                        <h4 class="text-xl font-bold text-navy mb-2">Connect</h4>
                        <p class="text-gray-600">We bring the pieces together so customers can find, understand and contact your business more easily.</p>
                    </div>
                </div>

            </div>

            <div class="mt-16 text-center">
                <a href="https://wa.me/447341462757" class="btn-primary inline-flex text-lg px-8 py-4">Let's Talk About Your Business</a>
            </div>
        </div>
    </section>

    <!-- HUMAN STORY SECTION -->
    <section class="section-padding bg-white relative overflow-hidden">
        <div class="container mx-auto px-6 relative z-10 flex flex-col lg:flex-row items-center gap-16">
            <div class="lg:w-5/12 w-full">
                <img src="../06-imagens/conexxus-founder-jesse.webp" alt="Conexxus Founder" class="w-full h-auto object-cover rounded-2xl shadow-2xl">
            </div>
            <div class="lg:w-7/12">
                <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-8 text-navy">It Started With a Connection.</h2>
                <div class="text-lg text-gray-600 space-y-6 leading-relaxed mb-10">
                    <p>Conexxus was born from a simple observation: many great small businesses struggle to stand out in an increasingly digital world.</p>
                    <p>They have experience. They have something valuable to offer. They have a story.</p>
                    <p>What they often need is a better way for people to discover it.</p>
                    <p>That's why we created Conexxus — to bridge the space between businesses and people through strategy, design and technology.</p>
                    <p>For us, digital presence isn't simply about being online.</p>
                    <p>It's about creating the connection that can turn a search into a visit, a visit into a conversation, and a conversation into a customer relationship.</p>
                </div>
                <div class="inline-block border-l-4 border-cyan pl-6 py-2">
                    <p class="text-2xl font-bold text-navy italic">Your business has a story.<br>We help people find it.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- LOCAL SEO SECTION -->
    <section class="section-padding bg-cloud border-y border-gray-100">
        <div class="container mx-auto px-6 max-w-4xl text-center">
            <h2 class="text-3xl md:text-4xl font-bold mb-8 text-navy">Digital Marketing Support in Swindon and Beyond</h2>
            <div class="text-lg text-gray-600 leading-relaxed space-y-6">
                <p>Conexxus is a digital marketing agency based in Swindon, Wiltshire, supporting small and medium-sized businesses with <a href="/servicos/criacao-de-websites" class="text-brand font-semibold hover:underline">website design</a>, <a href="/servicos/seo-local" class="text-brand font-semibold hover:underline">Local SEO</a>, <a href="/servicos/google-business-profile" class="text-brand font-semibold hover:underline">Google Business Profile</a>, <a href="/servicos/branding" class="text-brand font-semibold hover:underline">branding</a> and <a href="/servicos/gestao-de-redes-sociais" class="text-brand font-semibold hover:underline">social media management</a>.</p>
                <p>Our local focus is Swindon and the surrounding market, while our digital services also allow us to support businesses across the UK and internationally.</p>
            </div>
        </div>
    </section>

    <!-- PROJECTS SECTION -->
    <section class="section-padding bg-white relative text-center">
        <div class="container mx-auto px-6 max-w-4xl">
            <h2 class="text-3xl md:text-4xl font-bold mb-6 text-navy">Our Work. Their Stories.</h2>
            <p class="text-lg text-gray-600 mb-10">Every project starts with a different business, a different challenge and a different story. Explore how we turn those needs into clear, professional digital experiences.</p>
            <a href="/portfolio" class="btn-primary inline-flex shadow-lg shadow-blue-500/20 text-lg px-8 py-4">Explore Our Work</a>
        </div>
    </section>

    <!-- FAQ SECTION -->
    <section class="section-padding bg-cloud">
        <div class="container mx-auto px-6 max-w-4xl">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-4xl font-bold text-navy">Frequently Asked Questions</h2>
            </div>

            <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-100" x-data="{ selected: 1 }">
                
                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 1 ? selected = 1 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">What digital marketing services does Conexxus offer in Swindon?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 1}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 1" x-collapse>
                        <p>We provide website design, Local SEO, Google Business Profile management, branding, and social media management for small businesses.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 2 ? selected = 2 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Does Conexxus work only with businesses in Swindon?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 2}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 2" x-collapse>
                        <p>No. While our roots and local focus are in Swindon, we support businesses across the UK and international markets.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 3 ? selected = 3 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Can Conexxus create a website for my small business?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 3}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 3" x-collapse>
                        <p>Yes. Designing professional, responsive websites for small businesses is one of our core services.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 4 ? selected = 4 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Can Local SEO help customers find my business?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 4}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 4" x-collapse>
                        <p>Absolutely. Local SEO is designed to improve your visibility in search results when people look for services in your specific area.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 5 ? selected = 5 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Does Conexxus manage Google Business Profiles?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 5}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 5" x-collapse>
                        <p>Yes. We help set up, optimise, and maintain your Google Business Profile to ensure your information is clear and professional.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 6 ? selected = 6 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Does Conexxus provide branding services?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 6}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 6" x-collapse>
                        <p>Yes, we create clear and consistent brand identities that help your business stand out and build trust.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 7 ? selected = 7 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Does Conexxus offer social media management?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 7}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 7" x-collapse>
                        <p>Yes, we manage social media profiles to keep your business connected with your audience consistently.</p>
                    </div>
                </div>

                <div class="border-b border-gray-100 last:border-b-0">
                    <button class="w-full text-left px-6 py-5 flex items-center justify-between focus:outline-none hover:bg-gray-50 transition-colors" @click="selected !== 8 ? selected = 8 : selected = null">
                        <span class="font-bold text-navy text-lg pr-4">Does Conexxus provide support in English and Portuguese?</span>
                        <svg class="w-5 h-5 text-brand transform transition-transform" :class="{'rotate-180': selected === 8}" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                    <div class="px-6 pb-5 text-gray-600 text-lg" x-show="selected === 8" x-collapse>
                        <p>Yes, we offer bilingual support, making it easier to communicate and develop your project in either language.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FINAL CTA -->
    <section class="py-24 bg-navy text-white text-center border-t-4 border-brand">
        <div class="container mx-auto px-6 max-w-3xl">
            <h2 class="text-3xl md:text-4xl lg:text-5xl font-bold mb-6">Let's Build Your Next Connection.</h2>
            <p class="text-xl text-blue-100 mb-10 leading-relaxed font-light">
                Whether you're starting your digital presence or strengthening what you already have, we're here to help your business become easier to find, understand and connect with.
            </p>
            <a href="https://wa.me/447341462757" class="btn-primary text-lg px-10 py-4 shadow-xl shadow-blue-500/20 inline-flex items-center justify-center">Let's Connect</a>
            <p class="mt-8 text-sm text-cyan tracking-wider uppercase font-semibold">Based in Swindon. Supporting businesses beyond borders.</p>
        </div>
    </section>"""

new_footer = """    <!-- FOOTER -->
    <footer class="site-footer bg-graphite text-gray-400 pt-16 pb-8 border-t border-gray-800">
        <div class="container mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-10 mb-12">
                
                <!-- Brand -->
                <div class="space-y-4">
                    <h3 class="text-2xl font-bold text-white tracking-wider">CONEXXUS</h3>
                    <p class="text-cyan font-semibold italic">Connecting businesses with people.</p>
                    <p class="text-sm leading-relaxed mt-4">
                        Digital Marketing Agency<br>
                        Swindon, Wiltshire, United Kingdom
                    </p>
                </div>
                
                <!-- Links -->
                <div>
                    <h4 class="text-white font-bold mb-4 uppercase tracking-wider text-sm">Links</h4>
                    <div class="grid grid-cols-2 gap-3 text-sm">
                        <a href="/index.html" class="hover:text-white transition-colors">Home</a>
                        <a href="/servicos.html" class="hover:text-white transition-colors">Services</a>
                        <a href="/sobre.html" class="hover:text-white transition-colors">About</a>
                        <a href="/portfolio.html" class="hover:text-white transition-colors">Portfolio</a>
                        <a href="/blog.html" class="hover:text-white transition-colors">Blog</a>
                        <a href="/index.html#faq" class="hover:text-white transition-colors">FAQ</a>
                        <a href="/contato.html" class="hover:text-white transition-colors">Contact</a>
                        <a href="/privacidade.html" class="hover:text-white transition-colors">Privacy Policy</a>
                    </div>
                </div>

                <!-- Contact -->
                <div>
                    <h4 class="text-white font-bold mb-4 uppercase tracking-wider text-sm">Contact</h4>
                    <ul class="space-y-3 text-sm">
                        <li>07341 462757</li>
                        <li><a href="https://wa.me/447341462757" target="_blank" class="hover:text-[#25D366] transition-colors flex items-center gap-2">WhatsApp</a></li>
                        <li><a href="https://instagram.com/conexxus.co.uk" target="_blank" class="hover:text-[#E1306C] transition-colors flex items-center gap-2">Instagram @conexxus.co.uk</a></li>
                    </ul>
                </div>

            </div>

            <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-gray-500">
                <p>&copy; 2026 Conexxus Digital Marketing. All rights reserved.</p>
                <div class="flex gap-4">
                    <a href="/privacidade.html" class="hover:text-white transition-colors">Privacy Policy</a>
                    <a href="/termos.html" class="hover:text-white transition-colors">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>"""


# 1. Update index.html
with open('./build/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Separate header, body, footer, translate script
header_part = content.split("<!-- HERO SECTION -->")[0]
footer_part_idx = content.find("<!-- FOOTER -->")
footer_part_old = content[footer_part_idx:]

# Find the translate script to preserve it
translate_script_idx = footer_part_old.find("<!-- Google Translate Script -->")
translate_script = ""
if translate_script_idx != -1:
    translate_script = footer_part_old[translate_script_idx:]
    # Remove the </body> from translate_script just in case, we will add it back
    translate_script = translate_script.replace("</body>", "")
    translate_script = translate_script.replace("</html>", "")

new_index_html = header_part + new_body + "\n\n" + new_footer + "\n\n" + translate_script + "\n</body>\n</html>"

with open('./build/index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)


# 2. Update Footer in all other files
for root, dirs, files in os.walk('./build'):
    for file in files:
        if file == 'index.html' or not file.endswith('.html'):
            continue
        filepath = os.path.join(root, file)
        with open(filepath, 'r', encoding='utf-8') as f:
            file_content = f.read()
        
        f_idx = file_content.find("<!-- FOOTER -->")
        if f_idx != -1:
            head_body = file_content[:f_idx]
            
            t_idx = file_content.find("<!-- Google Translate Script -->")
            t_script = ""
            if t_idx != -1:
                t_script = file_content[t_idx:]
                t_script = t_script.replace("</body>", "").replace("</html>", "")
            
            new_file_html = head_body + new_footer + "\n\n" + t_script + "\n</body>\n</html>"
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_file_html)

print("Home page and Global Footers successfully updated.")
