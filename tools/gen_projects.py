# -*- coding: utf-8 -*-
"""Rebuild the whole portfolio section of dyrn-site: featured stack, an
'other work' grid, and one detailed case-study popup per project.

Every factual claim traces to D:\\CV\\Docs\\Dyrn_Verified_Facts_Memory.md.
AquaFoam and the Agromas builds are deliberately absent - see README.
"""
import io

# ---------------------------------------------------------------- projects

PROJECTS = [
    dict(
        key="busabunga", featured=True, img="busabunga",
        title="busabunga.com",
        tagline="Greenfield build that reached #1 in a month",
        type="Website build + technical SEO", date="Launched June 2026",
        role="Research, design, build, SEO", client="PT Tjikko Sentral Industrial",
        url=("Visit busabunga.com", "https://busabunga.com"),
        intro="A commercial site for Tjikko's decorative foam line, built end to end in React with Claude "
              "Code as the development partner. Keyword research, information architecture, build, content "
              "and search strategy were all mine. There was no existing site, no legacy traffic, no backlink "
              "profile and no advertising budget, so the only lever available was getting the structure and "
              "the search intent right before anything shipped.",
        scope=["Commercial keyword and intent research completed before any code was written",
               "Information architecture organised around buyer intent rather than the internal product catalogue",
               "Full React build, AI-assisted through Claude Code and Git",
               "Technical SEO foundation: crawl paths, indexation rules, schema, Core Web Vitals",
               "Dedicated pages for florists, wholesale buyers and private-label enquiries",
               "WhatsApp-first enquiry flow, matching how Indonesian B2B buyers actually make contact",
               "Search Console and analytics instrumented from day one, not retrofitted"],
        challenge="A brand-new domain competing for commercial terms that established suppliers and the big "
                  "marketplaces already owned. No authority to borrow from, no history for Google to trust, and "
                  "no paid support to buy time while rankings matured. On a domain like that, most of the usual "
                  "SEO levers are unavailable: what is left is structure, intent matching, and not making the "
                  "mistakes that keep new sites invisible.",
        approach="I mapped the commercial keyword set first and let it decide the site architecture, which is "
                 "the opposite of the usual order. Primary terms were floral foam, wet and dry floral foam, busa "
                 "bunga and floral foam indonesia; secondary terms covered supplier, distributor, grosir and "
                 "private-label variations. Each target term got exactly one page that clearly owned it, so the "
                 "site never competed with itself. Buyer-intent language went into headings and body copy rather "
                 "than internal product naming, and the enquiry path was kept short enough that arriving traffic "
                 "had somewhere obvious to go.",
        result="Within roughly one month of launch the site held #1 and page-one Google positions for its target "
               "commercial keywords. That came from structure and intent matching, not from authority the domain "
               "had not had time to build. It is the cleanest evidence I have that the method is repeatable: same "
               "approach, no inherited advantages, measurable outcome.",
        stack=["React", "Claude Code", "Technical SEO", "Schema.org", "Search Console", "GA4", "Cloudflare"],
    ),
    dict(
        key="trinitas", featured=True, img="trinitas",
        title="Sekolah Trinitas",
        tagline="#1 for five competitive local keywords",
        type="Local SEO", date="2026", role="SEO &amp; website developer",
        client="Sekolah Trinitas \u2014 via RIAS Strategic",
        url=("Visit sekolahtrinitasbdl.sch.id", "https://sekolahtrinitasbdl.sch.id"),
        intro="Local search work for a Christian trilingual school in Bandar Lampung, delivered through the RIAS "
              "Strategic freelance talent pool. The brief was easy to state and hard to win: own the terms parents "
              "type when they are shortlisting schools for their children.",
        scope=["Keyword mapping across the five priority local terms",
               "On-page rewrite so each term had one page unambiguously earning it",
               "Cannibalisation audit and fixes across overlapping pages",
               "Technical clean-up: crawl paths, indexation, on-page structure",
               "Local relevance signals tightened around Bandar Lampung",
               "Rank tracking against the target set through to position"],
        challenge="Education keywords in a regional Indonesian market are crowded with directories, aggregators "
                  "and institutions that have been online for a decade. Ranking meant beating pages with far more "
                  "authority, on terms where realistically only the top result converts. Parents do not scroll for "
                  "a school, and the decision cycle is short and emotional, so second place is close to worthless.",
        approach="I rebuilt the on-page and technical foundation around the five keywords that mattered and made "
                 "sure each had a single page earning it, which removed the cannibalisation quietly splitting the "
                 "site's own relevance across near-duplicate pages. Local signals were tightened so the school read "
                 "unambiguously as a Bandar Lampung institution rather than a generic national one. No link "
                 "building was involved: the gains came from fixing what the site was already saying badly.",
        result="#1 Google rankings for all five target keywords: sekolah kristen lampung, sekolah kristen terbaik "
               "lampung, sekolah trilingual terbaik lampung, sekolah trilingual lampung, and sekolah kristen "
               "lampung paling bagus. Verifiable in an incognito search from the region.",
        stack=["WordPress", "Technical SEO", "Local SEO", "Search Console", "Rank tracking"],
    ),
    dict(
        key="tjikko", featured=True, img="tjikko",
        title="Tjikko Foam",
        tagline="Four years owning an entire digital and IT function",
        type="Digital &amp; IT ownership", date="Jul 2021 \u2014 present",
        role="IT &amp; Digital Specialist", client="PT Tjikko Sentral Industrial",
        url=("Visit tjikkofoam.com", "https://tjikkofoam.com"),
        intro="For four years I have been the entire digital and IT function at a B2B polyurethane foam "
              "manufacturer. Not the marketing person with IT help, and not the IT person who also runs the "
              "website: both jobs, alone. Websites, SEO, analytics, brand and packaging design, video, "
              "marketplace channels, servers, security and procurement, with reporting that goes to the Board.",
        scope=["Corporate site rebuilt on WordPress and Elementor with an SEO-first structure",
               "Technical SEO: Core Web Vitals, schema markup, crawl and index hygiene",
               "Analytics stack: GA4, Google Tag Manager, Looker Studio, Search Console",
               "Indotrading B2B listing built from scratch, including direct coordination with their account team",
               "Shopee and Tokopedia listings built and managed, and currently leading their redesign",
               "Full design ownership: print and online catalogues, company profile, logos, packaging, product "
               "photography direction and video",
               "Wazuh SIEM deployed and monitored across 50+ devices",
               "Server, Cloudflare and Docker administration, plus IT procurement and hardware rollout",
               "Client-facing sales material and Board-level reporting"],
        challenge="A B2B industrial manufacturer with a technical product, a long sales cycle and no paid "
                  "advertising budget. Every enquiry had to be earned through organic search. There was also no "
                  "team, so nothing could be delegated and nothing could be high-maintenance: anything I built had "
                  "to keep working while I was busy with the other half of the job. The constraint shaped the "
                  "engineering as much as the strategy.",
        approach="I rebuilt the site around the language buyers actually search with instead of internal product "
                 "naming, then fixed the technical foundation underneath it so the content had a chance of being "
                 "found. Analytics went in early so performance became something the business could see and argue "
                 "about rather than a black box. On the infrastructure side I standardised monitoring so problems "
                 "surfaced before they became downtime. The marketplace work taught the most useful lesson: after "
                 "building and running the Shopee and Tokopedia listings, it became clear that molded industrial "
                 "foam had a product-market fit problem on consumer platforms, not an execution problem, which is "
                 "why the reactivation now centres on the consumer-fit decorative foam line instead.",
        result="Roughly 40% growth in organic traffic and a 25% increase in lead generation, entirely SEO-driven "
               "with no paid advertising. On the infrastructure side, around 30% less downtime across 50+ "
               "monitored devices, with no major security incident in four years.",
        stack=["WordPress", "Elementor", "Technical SEO", "GA4", "GTM", "Looker Studio", "Search Console",
               "Cloudflare", "Docker", "Wazuh SIEM", "Adobe CC"],
    ),
    dict(
        key="hermes", featured=True, img="hermes",
        title="Hermes AI Agent System",
        tagline="A self-hosted agent stack doing real daily work",
        type="AI automation platform", date="2026 \u2014 ongoing",
        role="Architect &amp; builder", client="Self-hosted / internal",
        url=None,
        intro="A self-hosted multi-agent system that does real daily work. Not a demo, not a prototype. Claude "
              "API handles the reasoning, n8n owns scheduling and orchestration, and MCP connects the whole thing "
              "to live WordPress sites and analytics properties. It runs on my own VPS, which means I also own the "
              "uptime, the credentials and the failure modes.",
        scope=["Multi-agent framework on a self-hosted VPS, with a reusable skill library",
               "Claude API as the reasoning engine; Claude Code and Git as the development workflow",
               "n8n for scheduling, orchestration, retries and error handling",
               "Claude Desktop with MCP connected to live WordPress sites",
               "RAG architecture for grounding agents in real documents rather than model memory",
               "Full multi-page client website builds executed through MCP",
               "SEO, GEO and AEO documentation systems",
               "GA4 audits and a daily reporting agent across three properties"],
        challenge="Most AI automation stops at the proof-of-concept stage: impressive in a screenshot, unreliable "
                  "the moment it has to run unattended against production systems. The hard part was never the "
                  "model call. It is everything around it: scheduling, credential handling, retry logic, and "
                  "knowing when the output is wrong before it reaches anyone who would act on it.",
        approach="I built Hermes as infrastructure rather than as a collection of scripts. Agents are composable "
                 "skills with a Git workflow behind them, so behaviour is versioned and reviewable. MCP handles "
                 "the integrations into live systems so agents act through real interfaces instead of scraped "
                 "ones. n8n owns scheduling and retries, which keeps the failure handling out of the prompts. "
                 "The design bias throughout is towards systems that degrade visibly rather than silently.",
        result="A GA4 Daily Reporter runs in production across three properties, pulling the data, formatting the "
               "report and distributing the insight without a human in the loop. The system is part of a 90-day "
               "practitioner sprint aimed at three to five production agents and a monetisable automation service.",
        stack=["Claude API", "Claude Code", "MCP", "n8n", "RAG", "Docker", "Self-hosted VPS", "Git"],
    ),
    dict(
        key="quotation-po", featured=True, img="quotation-po",
        title="Quotation vs PO Validation",
        tagline="AI checking paperwork nobody wanted to check",
        type="Business process automation", date="Live since July 2026",
        role="Architect &amp; builder", client="PT Tjikko Sentral Industrial",
        url=None,
        intro="A first-line AI validation layer that checks incoming customer purchase orders against the "
              "quotations they came from. It is a small, unglamorous problem that quietly costs a lot: a "
              "mismatch caught after acceptance becomes a margin loss or an argument, and catching them by hand "
              "is exactly the kind of work that gets skipped when the week is busy.",
        scope=["Line-item validation: does the PO match what was actually quoted",
               "Price validation: does the PO price match the quotation price",
               "Expiry validation: was the quotation still valid when the PO arrived",
               "Built on Claude scheduled tasks with MCP integrations into Google Drive and Gmail",
               "Reports hourly, so a mismatch surfaces the same working day",
               "Deliberately separate from Hermes, which is n8n-based: different failure modes, different "
               "operational risk"],
        challenge="Manual reconciliation is the sort of task that is important but never urgent, so it slips. It "
                  "also has to be right: a validation layer that raises false alarms gets ignored within a week, "
                  "and one that misses real mismatches is worse than nothing because it creates false confidence.",
        approach="I kept the scope narrow on purpose. Three checks, clearly defined, running on a schedule rather "
                 "than trying to be a general-purpose document agent. It reads from the systems the team already "
                 "uses via MCP rather than asking anyone to change how they work, and reports hourly so a problem "
                 "surfaces while the paperwork is still fresh. Building it separately from Hermes was a "
                 "reliability decision, not a technical one: I did not want a workflow failure in one system to "
                 "take out the other.",
        result="Live in production since July 2026, removing a recurring manual reconciliation task from the "
               "Marketing Manager and returning that time to field and market work. It is still early, so there "
               "is deliberately no catch-rate or time-saved figure here: those numbers are worth having only once "
               "the system has a real track record behind it.",
        stack=["Claude API", "Claude scheduled tasks", "MCP", "Google Drive", "Gmail"],
    ),
    dict(
        key="tjikko-global", featured=True, img="tjikko-global",
        title="Tjikko Foam Global",
        tagline="Export-facing platform for international buyers",
        type="International website + SEO", date="2026",
        role="Build &amp; international SEO", client="PT Tjikko Sentral Industrial",
        url=("Visit global.tjikkofoam.com", "https://global.tjikkofoam.com"),
        intro="A dedicated global-facing site positioning Tjikko Foam for international wholesale buyers, "
              "distributors and export partners. Built in Next.js and kept structurally separate from the "
              "domestic site so neither proposition had to compromise for the other.",
        scope=["Next.js build with an export-oriented information architecture",
               "English-first messaging written for overseas procurement teams",
               "Product specifications surfaced early rather than buried in a catalogue",
               "International on-page SEO",
               "Cloudflare performance and security layer",
               "Cross-border enquiry flow with the credibility signals export buyers look for"],
        challenge="Domestic B2B messaging does not transfer across borders. International procurement teams "
                  "evaluate on specification, capacity and verifiable credibility long before they consider "
                  "brand, and they arrive with no context about an Indonesian manufacturer they have not heard of.",
        approach="I restructured the content around what an overseas buyer needs to verify first, kept the "
                 "specifications explicit and scannable, and separated the export proposition from the domestic "
                 "site entirely. The technical build uses Next.js for speed and clean indexation, with Cloudflare "
                 "in front to keep latency reasonable for visitors far from the origin.",
        result="A distinct international presence engineered to capture export demand and convert overseas "
               "visitors into qualified enquiries, rather than an English translation of a domestic site.",
        stack=["Next.js", "International SEO", "GA4", "Search Console", "Cloudflare"],
    ),

    dict(
        key="soka", featured=False, img="soka",
        title="Soka Chemical",
        tagline="B2B chemical distribution",
        type="Corporate website", date="2025", role="Website developer",
        client="PT Soka Uni Pratama \u2014 via RIAS Strategic",
        url=("Visit soka-chem.com", "https://soka-chem.com"),
        intro="A corporate product website for a chemical distribution company selling to industrial buyers and "
              "distributors, delivered through the RIAS Strategic talent pool.",
        scope=["WordPress and Elementor design and build",
               "Product catalogue structure organised by application, not by internal SKU grouping",
               "Specification presentation aimed at procurement readers",
               "On-page SEO foundation and indexable catalogue pages"],
        challenge="Chemical distribution is a credibility-first category with an unglamorous catalogue. Buyers "
                  "compare on specification and supply reliability, so the site had to make dry technical "
                  "information legible and trustworthy rather than dress it up.",
        approach="A clean catalogue structure that puts specifications where buyers look for them, built on a "
                 "foundation that can actually be found in search rather than only handed out as a link in an "
                 "email.",
        result="A professional digital presence that represents the company credibly to industrial buyers and "
               "gives its catalogue a searchable home.",
        stack=["WordPress", "Elementor", "On-page SEO"],
    ),
    dict(
        key="rias", featured=False, img="rias",
        title="RIAS Strategic",
        tagline="Platform for a remote services business",
        type="Corporate website", date="2025", role="Website developer",
        client="RIAS Strategic \u2014 the agency whose talent pool I freelance through",
        url=("Visit riasstrategic.com", "https://riasstrategic.com"),
        intro="A digital platform for RIAS Strategic, the virtual assistant agency whose freelance talent pool I "
              "belong to as a UI/UX and website developer. Their own site was one of the projects I delivered for "
              "them, which is a reasonable signal in itself.",
        scope=["WordPress design and build",
               "Service page structure organised around client problems rather than internal divisions",
               "Brand-aligned visual layout",
               "Conversion path for enquiry and onboarding"],
        challenge="A services business has nothing physical to show. Credibility has to come from how clearly the "
                  "offer is structured and how quickly a prospect can work out whether it applies to them.",
        approach="Service pages framed by the problem the client arrives with, with the agency's internal "
                 "structure kept out of the navigation entirely, on a layout consistent with the existing brand.",
        result="A platform ready for client acquisition and service promotion, and the site the agency uses to "
               "represent itself.",
        stack=["WordPress", "Elementor", "UX layout"],
    ),
    dict(
        key="pawcharm", featured=False, img="pawcharm",
        title="The Paw Charm",
        tagline="Direct-to-consumer pet accessories",
        type="E-commerce", date="2025", role="Store build",
        client="The Paw Charm",
        url=("Visit thepawcharmstore.com", "https://thepawcharmstore.com"),
        intro="A Shopify store for a pet accessories brand selling directly to consumers. A different problem "
              "from the B2B work: impulse-led, mobile-first, and entirely dependent on the checkout not getting "
              "in the way.",
        scope=["Shopify store setup and theme configuration",
               "Product catalogue and collection structure built around browsing behaviour",
               "Checkout path optimisation",
               "Mobile-first presentation, where the majority of the traffic lands"],
        challenge="Consumer retail forgives nothing at checkout. Every additional step between wanting the "
                  "product and owning it costs conversions, and the margin on accessories does not leave room to "
                  "buy that traffic back.",
        approach="A catalogue organised the way shoppers browse rather than the way inventory is filed, with the "
                 "checkout path kept as short as the platform allows and the mobile view treated as the primary "
                 "design target rather than an adaptation.",
        result="An operational store ready to sell, with the catalogue and fulfilment structure in place behind "
               "it.",
        stack=["Shopify", "E-commerce setup", "Product catalogue", "CRO"],
    ),
    dict(
        key="lingga", featured=False, img="lingga",
        title="Lingga Florist",
        tagline="Florist site plus a paid search campaign",
        type="Website + Google Ads", date="Aug \u2014 Sep 2023", role="Build &amp; campaign",
        client="Lingga Florist",
        url=("Visit linggaflorist.com", "https://linggaflorist.com/"),
        intro="A florist store website, plus a Google Ads campaign I ran as a personal project between August and "
              "September 2023. It is the one place in my work where I have run paid search end to end rather than "
              "relying on organic, and I include it precisely because it marks the boundary of what I have "
              "actually executed.",
        scope=["Website build and product presentation",
               "Google Ads campaign structure, targeting and ad copy",
               "Conversion tracking configured before spend started",
               "Ongoing optimisation across the campaign period"],
        challenge="Florists compete on immediacy. People buy flowers against a deadline, so the campaign had to "
                  "catch high-intent searches at the moment of need, on a budget small enough that wasted "
                  "impressions mattered.",
        approach="Tight keyword targeting around purchase-intent terms rather than broad category terms, with "
                 "conversion tracking in place from the start so budget could follow what was actually converting "
                 "instead of what was merely getting clicks.",
        result="Across the campaign period: 261,000+ impressions, 795 clicks and 275 conversions at a 34.6% "
               "conversion rate, on roughly Rp 1.04M of total spend.",
        stack=["WordPress", "Google Ads", "Conversion tracking", "GA4"],
    ),
    dict(
        key="invera", featured=False, img="invera",
        title="Invera Wedding",
        tagline="Wedding platform built for first impressions",
        type="Website development", date="2025", role="Website developer",
        client="Invera Wedding \u2014 via RIAS Strategic",
        url=("Visit inverawedding.web.id", "https://inverawedding.web.id"),
        intro="A wedding service platform built through the RIAS Strategic talent pool, one of several projects "
              "spanning SMEs, companies and factories.",
        scope=["WordPress and Elementor build",
               "Service and package presentation",
               "Gallery setup tuned so imagery stays sharp without bloating the page",
               "Local SEO fundamentals"],
        challenge="Wedding sites live or die on first impression. The design had to feel personal and unhurried "
                  "while still loading quickly on the phones most guests would actually open it on. Image-heavy "
                  "and fast are not natural allies.",
        approach="An image-led build with the couple's story and the enquiry flow as the spine of the layout, "
                 "with the photography compressed and sized so the emotional impact survives a mobile connection.",
        result="Delivered and live, with a structure that supports service enquiries rather than only looking "
               "good.",
        stack=["WordPress", "Elementor", "Local SEO"],
    ),
    dict(
        key="nyliem", featured=False, img="nyliem",
        title="Ny Liem Heritage",
        tagline="Heritage brand, translated to the web",
        type="Website development", date="2025", role="Website developer",
        client="Ny Liem Heritage \u2014 via RIAS Strategic",
        url=("Visit nyliem.com", "https://nyliem.com"),
        intro="A brand site for a heritage culinary business with a long story and an established product line, "
              "also delivered through RIAS Strategic.",
        scope=["WordPress design and build",
               "Brand storytelling layout that gives the history room",
               "Product presentation for an established range",
               "SEO-ready page structure"],
        challenge="Translating an established offline brand identity into a web presence without flattening the "
                  "character that made it recognisable in the first place. A generic modern template costs a "
                  "heritage brand more than it gains.",
        approach="The build leads with the brand's own visual language and keeps the interface deliberately "
                 "quiet, so the heritage does the talking rather than the layout.",
        result="A premium digital presence that carries the brand's story instead of replacing it.",
        stack=["WordPress", "Elementor", "Brand design"],
    ),
]

# ---------------------------------------------------------------- markup

STACK_ITEM = '''                          <!-- portfolio stack single item -->
                          <div class="stack-item">
                            <div data-mfp-src="#project-{key}" class="portfolio-stack__inner portfolio-item-{n} popup-trigger">
                              <div class="portfolio-stack__descr">
                                <h3 class="portfolio-stack__title light">{title}</h3>
                                <p class="portfolio-stack__tagline">{tagline}</p>
{visit}                              </div>
                            </div>
                          </div>
'''

TILE = '''                          <!-- other work single item -->
                          <div class="col-12 col-md-6 col-xl-4 grid-item animate-card-2">
                            <div data-mfp-src="#project-{key}" class="work-tile popup-trigger">
                              <div class="work-tile__image">
                                <img src="img/work/{img}.jpg" alt="{title} website" loading="lazy">
                              </div>
                              <div class="work-tile__descr">
                                <h4 class="work-tile__title animate-in-up">{title}</h4>
                                <p class="work-tile__text small type-basic-160lh animate-in-up">{tagline}</p>
{visit}                              </div>
                            </div>
                          </div>
'''

# Card-level shortcut to the live site. js/custom.js stops the click from
# bubbling to the card, which would otherwise open the case-study popup.
VISIT = '''                                <a class="project-visit" href="{url}" target="_blank" rel="noopener"
                                   aria-label="Open {title} in a new tab">
                                  <span>Visit live site</span>
                                  <i class="ph ph-arrow-up-right"></i>
                                </a>
'''


def visit_link(p):
    if not p["url"]:
        return ""
    return VISIT.format(url=p["url"][1], title=p["title"])

BLOCK = '''                          <!-- Project Block - {label} Start -->
                          <div class="project__block{extra}">
                            <div class="project__descr">
                              <div class="container-fluid p-0">
                                <div class="row g-0">
                                  <div class="col-12 col-xl-4">
                                    <h4 class="project__subtitle tagline-chapter">{label}</h4>
                                  </div>
                                  <div class="col-12 col-xl-8">
{body}                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <!-- Project Block - {label} End -->
'''

POPUP = '''              <!-- Project Popup - {title} Start -->
              <div id="project-{key}" class="popup mfp-hide">

                <button class="mfp-close permanent-dark"></button>

                <div class="popup__container">
                  <div class="container-fluid p-0">
                    <div class="row g-0">
                      <div class="col-12">
                        <div class="project">

                          <!-- Project Block - Title with Image Start -->
                          <div class="project__block no-padding no-margin project-image-bg">
                            <img class="project-image-bg__portrait" src="img/work/{img}.jpg" alt="{title} project cover" loading="lazy">
                            <img class="project-image-bg__landscape" src="img/work/{img}.jpg" alt="{title} project cover" loading="lazy">
                            <div class="project__title">
                              <h3 class="light">{title}</h3>
                            </div>
                          </div>
                          <!-- Project Block - Title with Image End -->

                          <!-- Project Block - Description Start -->
                          <div class="project__block grid-block grid-items">
                            <div class="project__data">
                              <div class="container-fluid p-0">
                                <div class="row g-0">
                                  <div class="col-12 col-xl-4">
                                    <div class="container-fluid p-0">
                                      <div class="row g-0">
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Type</p>
                                          <p class="data__descr small type-basic-160lh">{type}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Date</p>
                                          <p class="data__descr small type-basic-160lh">{date}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Role</p>
                                          <p class="data__descr small type-basic-160lh">{role}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Client</p>
                                          <p class="data__descr small type-basic-160lh">{client}</p>
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                  <div class="col-12 col-xl-8 grid-item">
                                    <p class="type-basic-160lh">{intro}</p>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <!-- Project Block - Description End -->

{blocks}{link}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
              <!-- Project Popup - {title} End -->
'''

LINK = '''
                          <!-- Project Block - Project Link Start -->
                          <div class="project__block small-size">
                            <div class="container-fluid p-0">
                              <div class="row g-0">
                                <div class="col-12 d-flex justify-content-center">
                                  <a class="btn btn-circle-text hover-circle" href="{url}" target="_blank" rel="noopener">
                                    <em></em>
                                    <span class="btn-caption">{label}</span>
                                  </a>
                                </div>
                              </div>
                            </div>
                          </div>
                          <!-- Project Block - Project Link End -->
'''


def para(text):
    return '                                    <p class="type-basic-160lh">%s</p>\n' % text


def bullets(items):
    out = ['                                    <ul class="project__list type-basic-160lh">\n']
    for it in items:
        out.append('                                      <li>%s</li>\n' % it)
    out.append('                                    </ul>\n')
    return "".join(out)


def tags(items):
    out = ['                                    <ul class="project__tags">\n']
    for it in items:
        out.append('                                      <li>%s</li>\n' % it)
    out.append('                                    </ul>\n')
    return "".join(out)


def build_popup(p):
    blocks = []
    blocks.append(BLOCK.format(label="What I built", body=bullets(p["scope"]), extra=" pre-grid-items"))
    blocks.append(BLOCK.format(label="The challenge", body=para(p["challenge"]), extra=""))
    blocks.append(BLOCK.format(label="How I approached it", body=para(p["approach"]), extra=""))
    blocks.append(BLOCK.format(label="Result", body=para(p["result"]), extra=""))
    blocks.append(BLOCK.format(label="Stack", body=tags(p["stack"]), extra=""))
    link = ""
    if p["url"]:
        label, url = p["url"]
        link = LINK.format(label=label, url=url)
    return POPUP.format(blocks="\n".join(blocks), link=link, **p)


featured = [p for p in PROJECTS if p["featured"]]
others = [p for p in PROJECTS if not p["featured"]]

stack_html = "".join(
    STACK_ITEM.format(n=5 + i, visit=visit_link(p), **p)
    for i, p in enumerate(featured))

tiles_html = "".join(TILE.format(visit=visit_link(p), **p) for p in others)

OTHER_SECTION = '''                  <!-- Content Block - Other Work Start -->
                  <div class="content__block grid-block pre-text-items">

                    <!-- Section Subtitle Start -->
                    <div class="block__subtitle grid-block-subtitle">
                      <h3 class="tagline-chapter animate-in-up">Other work</h3>
                    </div>
                    <!-- Section Subtitle End -->

                    <div class="container-fluid p-0">
                      <div class="row g-0 align-items-stretch">
%s                      </div>
                    </div>

                    <div class="work-note animate-in-up">
                      <p class="type-basic-160lh">Also built, outside client work:
                        <a class="link-small-underline" href="https://github.com/Dyrnzefanya/seoflow-ai-dashboard" target="_blank" rel="noopener">SEOFlow AI Dashboard</a>,
                        a full-stack SEO analytics SaaS on Next.js, TypeScript, Supabase and Vercel; and
                        <a class="link-small-underline" href="https://github.com/Dyrnzefanya/Watermark-Bulk" target="_blank" rel="noopener">WaterStamp</a>,
                        a bulk WebP watermarking tool that runs entirely in the browser in a single Vanilla JS
                        file, with no backend and no upload. App Store Optimisation work on a Play Store app
                        rounds out the list.</p>
                      <p class="type-basic-160lh">Two more corporate sites, Agromas Tapioca and Agromas Crackers,
                        are in development and will be added once they are live.</p>
                    </div>

                  </div>
                  <!-- Content Block - Other Work End -->
''' % tiles_html

popups_html = "\n".join(build_popup(p) for p in PROJECTS)

# ---------------------------------------------------------------- splice
#
# Idempotent: each region is delimited by markers this script itself emits, so
# running it repeatedly replaces its own output instead of stacking duplicates.

import os
import re

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "index.html")
path = os.path.normpath(path)
s = io.open(path, encoding="utf-8").read()


def replace_between(text, start_pat, end_pat, replacement, label):
    """Swap everything from the first start_pat to the last end_pat."""
    m1 = re.search(start_pat, text)
    if not m1:
        raise SystemExit("marker not found: %s" % label)
    matches = list(re.finditer(end_pat, text))
    if not matches:
        raise SystemExit("end marker not found: %s" % label)
    m2 = matches[-1]
    return text[:m1.start()] + replacement + text[m2.end():]


# 1. featured stack items
s = replace_between(
    s,
    r"[ \t]*<!-- portfolio stack single item -->",
    r"[ \t]*<!-- portfolio stack single item -->.*?\n(?:.*?\n)*?[ \t]*</div>\n(?=[ \t]*</div>\n[ \t]*</div>\n[ \t]*</div>\n[ \t]*<!-- Content Block - Portfolio Gallery Stack Grid End -->)",
    stack_html, "stack items")

# 2. the "other work" grid
mark = "                  <!-- Content Block - Portfolio Gallery Stack Grid End -->\n"
if "<!-- Content Block - Other Work Start -->" in s:
    s = replace_between(
        s,
        r"[ \t]*<!-- Content Block - Other Work Start -->",
        r"[ \t]*<!-- Content Block - Other Work End -->\n",
        OTHER_SECTION, "other work")
else:
    i = s.index(mark) + len(mark)
    s = s[:i] + "\n" + OTHER_SECTION + s[i:]

# 3. all case-study popups
if "<!-- Project Popup -" in s:
    s = replace_between(
        s,
        r"[ \t]*<!-- Project Popup - .*? Start -->",
        r"[ \t]*<!-- Project Popup - .*? End -->\n",
        popups_html, "project popups")
else:
    s = replace_between(
        s,
        r"[ \t]*<!-- Portfolio Single Item Popup .*? Start -->",
        r"[ \t]*<!-- Portfolio Single Item Popup .*? End -->\n",
        popups_html, "legacy popups")

io.open(path, "w", encoding="utf-8").write(s)
print("featured: %d, other: %d, popups: %d" % (len(featured), len(others), len(PROJECTS)))
