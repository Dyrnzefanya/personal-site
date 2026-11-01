# -*- coding: utf-8 -*-
"""Rebuild the whole portfolio section of dyrn-site: featured stack, an
'other work' grid, and one detailed case-study popup per project.

Every factual claim traces to the Master Portfolio 2026 (Oct 2026), which
supersedes D:\\CV\\Docs\\Dyrn_Verified_Facts_Memory.md (Aug 2026) where they
differ - notably Meta Ads, which is now executed work.
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
        intro="A commercial site for Tjikko's floral foam line, built end to end in Next.js (React) with Claude "
              "Code as the development partner. Keyword research, information architecture, build, content "
              "and search strategy were all mine. There was no existing site, no legacy traffic, no backlink "
              "profile and no advertising budget, so the only lever available was getting the structure and "
              "the search intent right before anything shipped.",
        scope=["16 target keywords grouped into four intent clusters (product, supplier, wholesale, private label), "
               "each mapped to a page before design started",
               "Information architecture organised around buyer intent rather than the internal product catalogue",
               "Full Next.js build, AI-assisted through Claude Code and Git, deployed on Vercel behind Cloudflare",
               "Schema markup: Organization, WebSite, FAQPage, ItemList",
               "Dedicated pages for florists, wholesale buyers and private-label enquiries",
               "WhatsApp-first enquiry flow, matching how Indonesian B2B buyers actually make contact",
               "Search Console and Google Business Profile set up from day one, not retrofitted",
               "Post-launch Screaming Frog crawl: 100% of internal URLs indexable, none blocked",
               "A daily AI SEO audit, run by Hermes, that flags issues with a reason and a fix"],
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
               "commercial keywords, including floral foam, wet floral foam and busa bunga, ranking above the "
               "marketplace listings. That came from structure and intent matching, not from authority the domain "
               "had not had time to build. It is the cleanest evidence I have that the method is repeatable: same "
               "approach, no inherited advantages, measurable outcome.",
        stack=["Next.js", "Claude Code", "Technical SEO", "Schema.org", "Search Console", "Screaming Frog",
               "Vercel", "Cloudflare"],
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
        tagline="#1 for \u201cpabrik busa\u201d, and the whole digital function",
        type="Digital &amp; IT ownership", date="Jul 2021 \u2014 present",
        role="IT &amp; Digital Specialist", client="PT Tjikko Sentral Industrial",
        url=("Visit tjikkofoam.com", "https://tjikkofoam.com"),
        intro="Since 2021 I have been the entire digital and IT function at a B2B polyurethane foam "
              "manufacturer. Not the marketing person with IT help, and not the IT person who also runs the "
              "website: both jobs, alone. Websites, SEO, analytics, Meta Ads, brand and packaging design, video, "
              "marketplace channels, servers, security and procurement, with reporting that goes to the Board.",
        scope=["Removed an injected spam attack from the corporate site and hardened it",
               "Corporate site rebuilt on WordPress and Elementor with one content structure per product",
               "Technical SEO: Core Web Vitals, schema markup, crawl and index hygiene",
               "Analytics stack: GA4, Google Tag Manager, Looker Studio, Search Console",
               "Hands-on Meta Ads for company products: audience, creative and monitoring",
               "AI content pipeline (Claude API plus image generation) producing 50+ brand assets a month",
               "Indotrading B2B listing built from scratch, including direct coordination with their account team",
               "Shopee and Tokopedia listings built and managed, and currently leading their redesign",
               "Full design ownership: print and online catalogues, company profile, logos, packaging, product "
               "photography direction and video",
               "Wazuh SIEM deployed and monitored across 50+ devices",
               "Server, Cloudflare and Docker administration, plus IT procurement and hardware rollout",
               "Client-facing sales material and Board-level reporting"],
        challenge="A B2B industrial manufacturer with a technical product and a long sales cycle, competing with "
                  "larger factories for industrial keywords on a site that had just been hit by a spam injection "
                  "attack. Most enquiries had to be earned through organic search. There was also no "
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
        result="Roughly 40% growth in organic traffic and a 25% increase in lead generation after the rebuild and "
               "technical SEO. tjikkofoam.com ranks #1 on Google for “pabrik busa”, “produsen "
               "busa” and “busa molded”, and is cited as a source in Google’s AI Overview for "
               "“pabrik busa”. On the infrastructure side, around 30% less downtime across 50+ monitored "
               "devices after the Wazuh rollout.",
        stack=["WordPress", "Elementor", "Technical SEO", "GA4", "GTM", "Looker Studio", "Search Console",
               "Meta Ads", "Cloudflare", "Docker", "Wazuh SIEM", "Adobe CC"],
    ),
    dict(
        key="meta-ads", featured=True, img="meta-ads",
        title="B2B Meta Ads + CRM",
        tagline="Judging ads on qualified leads, not chat counts",
        type="Performance marketing", date="2026",
        role="Meta Ads, tracking, dashboard, AI analysis",
        client="B2B corporate gifting company (anonymised)",
        url=None,
        intro="A social enterprise selling handcrafted corporate gifts ran Meta Click-to-WhatsApp ads. In Ads "
              "Manager the ads looked efficient. Sales kept receiving chats asking about trousers, motorbike "
              "spare parts and uniforms. I set up and optimised the account, and built the measurement layer that "
              "ties every ad to what Sales actually marked in the CRM.",
        scope=["Meta Ads setup and optimisation: 10 active ads, one ad per ad set, six B2B audiences",
               "An ad naming taxonomy (month, audience code, creative brief) used as the join key across every system",
               "A Google Sheet tracker joining Meta spend and chats with Mekari Qontak CRM leads, per ad, per day",
               "Coefficient pulling Meta data every morning",
               "Ads Monitor: a Google Apps Script dashboard showing which ad produces qualified leads, which passed "
               "the cut-off without one, and where Meta actually spent",
               "A daily Claude report: observation, why it matters, action, metric to watch, per ad",
               "Business rules written into the prompt: cut-off, scaling steps, scepticism towards Meta’s own "
               "recommendations"],
        challenge="Meta counts conversations started, not leads. For premium B2B gifts a chat means little until "
                  "Sales marks it relevant, and that verdict lived in the CRM while spend lived in Meta. Ad names "
                  "drifted between periods so the two never matched, the CEO’s cut-off rule was being applied "
                  "to chats rather than qualified leads, and ads set to Instagram were quietly serving on WhatsApp "
                  "Status and Facebook Reels.",
        approach="Sales is the source of truth: a lead is qualified only when Sales marks it, and neither the "
                 "system nor the AI guesses. A strict naming taxonomy let Meta, the CRM, the dashboard and the AI "
                 "refer to the same ad. Placement setting and actual delivery are tracked separately so leakage "
                 "shows up. The AI reads the data every morning and recommends KEEP, SCALE, FIX or PAUSE; I review "
                 "each one and make the change in Ads Manager myself.",
        result="Over 1 May to 15 October 2026 the tracker traced 105 CRM-qualified leads, out of 2,573 WhatsApp "
               "chats, back to individual ads, plus three deals worth Rp167M. The joined data changed real "
               "decisions: one creative brief produced qualified leads in all five audiences, WhatsApp Status "
               "turned out to deliver the cheapest chats and none of the useful ones, and an ad that looked "
               "expensive per lead had in fact produced a Rp112M deal. Client data is anonymised.",
        stack=["Meta Ads Manager", "Click-to-WhatsApp", "Mekari Qontak", "Coefficient", "Google Sheets",
               "Apps Script", "Claude"],
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
               "report and delivering it to Discord without a human in the loop. A daily SEO audit job for "
               "busabunga.com runs alongside it, reporting what works and then each issue with why it matters and "
               "a fix. The system is part of a 90-day "
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
        key="gentiaras", featured=False, img="gentiaras",
        title="STIE Gentiaras",
        tagline="Admissions-first site for a business school in Lampung",
        type="Website + SEO", date="2026", role="Website developer &amp; SEO",
        client="Sekolah Tinggi Ilmu Ekonomi Gentiaras",
        url=("Visit gentiaras.ac.id", "https://gentiaras.ac.id"),
        intro="A new website for a business school in Lampung that has taught management and accounting since "
              "2000. The audience is prospective students and their parents, who compare campuses on "
              "accreditation, cost, career outcomes and scholarships before they ever visit.",
        scope=["WordPress and Elementor Pro design and build",
               "Homepage organised around the questions applicants ask: accreditation, cost, career, scholarships",
               "Study-programme, admissions, partnership and news sections with a mega menu",
               "A persistent “Daftar Sekarang” call to action and a floating WhatsApp button",
               "On-page SEO and structured data through All in One SEO, aimed at “kuliah di Lampung” searches",
               "Google Site Kit connecting Search Console and GA4 from launch"],
        challenge="Private campuses in a regional market compete with state universities and with each other for "
                  "the same applicants. Prospective students decide quickly and on a phone, and an old-looking "
                  "site reads as an old-looking campus.",
        approach="I led with the reasons a student would choose the campus (26 years of history, BAN-PT "
                 "accreditation, the tax Brevet certification, affordable fees) and kept the path to registration "
                 "one tap away on every page. Each programme gets its own page so it can be found for its own "
                 "searches, and measurement was in place before launch rather than added later.",
        result="Delivered and live at gentiaras.ac.id. Too recently launched for post-launch search data, so no "
               "ranking claim is made here yet.",
        stack=["WordPress", "Elementor Pro", "All in One SEO", "Site Kit", "GA4", "Search Console"],
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
        intro="A local florist that needed enquiries from people already searching for flowers. I built the "
              "WordPress site and ran the Google Ads search campaign that sent traffic to it, as a personal "
              "project between August and September 2023.",
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
        tagline="Heritage brand, now visible in Google’s AI answers",
        type="Website development", date="2025", role="Website developer",
        client="Ny Liem Heritage \u2014 via RIAS Strategic",
        url=("Visit nyliem.com", "https://nyliem.com"),
        intro="A brand site for a heritage culinary business with a long story and an established product line, "
              "also delivered through RIAS Strategic.",
        scope=["WordPress design and build",
               "Brand storytelling layout that gives the history room",
               "Product presentation for an established range",
               "SEO-ready page structure",
               "Looker Studio SEO dashboard with an opportunity-queries table for positions 10 to 20"],
        challenge="Translating an established offline brand identity into a web presence without flattening the "
                  "character that made it recognisable in the first place. A generic modern template costs a "
                  "heritage brand more than it gains.",
        approach="The build leads with the brand's own visual language and keeps the interface deliberately "
                 "quiet, so the heritage does the talking rather than the layout.",
        result="Search Console shows 1.4K impressions in Google’s Generative AI features between 30 July and "
               "12 October 2026, up from near zero in early August to 25–75 a day from September. Over the "
               "same period the site took 342 clicks from 13K impressions at an average position of 5.4. AI "
               "Overview inclusion is Google’s call and cannot be guaranteed; clean structure and pages that "
               "answer real questions improve the odds.",
        stack=["WordPress", "Elementor", "SEO / GEO", "Search Console", "Looker Studio"],
    ),
    dict(
        key="lawfirm", featured=False, img="lawfirm",
        title="Jakarta Law Firm",
        tagline="Bilingual law firm site with a WhatsApp-first path",
        type="Website + local SEO", date="2026", role="Website developer",
        client="Jakarta Law Firm",
        url=("Visit jakarta-lawfirm.com", "https://www.jakarta-lawfirm.com"),
        intro="A website for an advocates and legal consultants firm with offices in South and East Jakarta. "
              "People looking for a lawyer arrive worried and short on time, so the site leads with a plain "
              "promise and one obvious way to start a conversation.",
        scope=["WordPress and Elementor design and build",
               "Bilingual site, Indonesian and English",
               "Practice-area pages, advocate profiles and an articles section",
               "LegalService and Organization schema with both office addresses",
               "WhatsApp-first enquiry path, with the phone number in the header on every page",
               "XML sitemaps and on-page SEO for local legal searches"],
        challenge="Legal services is a trust-first category with crowded local search. A visitor is often "
                  "comparing several firms at once, and a site that reads like a brochure loses them to one that "
                  "simply tells them what happens next.",
        approach="Copy written around the visitor’s situation rather than the firm’s credentials, with "
                 "each practice area on its own page so it can be found for its own searches. Structured data "
                 "tells Google exactly what the firm is and where its two offices are, and the WhatsApp call to "
                 "action stays visible wherever the visitor scrolls.",
        result="Delivered and live at jakarta-lawfirm.com. Too recently launched for post-launch search data, so "
               "no ranking claim is made here yet.",
        stack=["WordPress", "Elementor", "Local SEO", "Schema.org", "Bilingual"],
    ),
]

# ---------------------------------------------------------------- services
#
# Each card in #services opens a detail popup. Proof lines must point to a
# project on this page, so a reader can check them.

SERVICES = [
    dict(
        key="web", title="Website<br>development", name="Website development",
        card="WordPress and Elementor, Shopify, or Next.js and React when the project calls for it. Built to load "
             "fast, be found and turn visitors into enquiries, not merely to look finished.",
        intro="A website is finished when it can be found, measured and acted on. Every build starts from who "
              "searches for it, what they need to see before they get in touch, and how the result will be "
              "measured. Looking good is the starting point, not the goal.",
        best_for="Factories, schools, campuses, law firms, SMEs and service businesses",
        platforms="WordPress + Elementor, Shopify, Next.js / React",
        deliverable="A live site, instrumented with GA4 and Search Console from day one",
        evidence="Every site in the portfolio is live and linked",
        scope=["Information architecture planned from search demand, one clear page per intent",
               "Design and build on the platform that fits: WordPress for teams that edit themselves, Shopify for "
               "stores, Next.js for speed-critical or custom builds",
               "Enquiry paths that match how Indonesian buyers actually make contact: WhatsApp first, forms second",
               "B2B specifics: specifications early on the page, wholesale and distributor intent kept apart from "
               "retail, credibility signals for procurement readers",
               "Bilingual or export-facing sites built as their own structure, not a translated page",
               "Performance and security: Core Web Vitals, image weight, Cloudflare, hardening and malware cleanup",
               "Handover with a site the client can update without breaking it"],
        process=["Understand what counts as a result: an enquiry, a registration, a sale",
                 "Map the searches and questions the audience brings",
                 "Structure and wireframe the pages around those intents",
                 "Build, then wire up GA4, Tag Manager and Search Console before launch",
                 "Launch, check indexing, and fix what the first weeks of data show"],
        proof=["busabunga.com: Next.js build, #1 on Google within about a month of launch",
               "tjikkofoam.com: rebuilt after a spam injection attack, now the company’s main inbound channel",
               "Sekolah Trinitas, STIE Gentiaras, Jakarta Law Firm, Soka Chemical, The Paw Charm and more in the "
               "portfolio above"],
        tools=["WordPress", "Elementor Pro", "Shopify", "Next.js", "React", "TypeScript", "Vercel", "Cloudflare",
               "Claude Code"],
    ),
    dict(
        key="seo", title="SEO &amp;<br>GEO", name="SEO &amp; GEO",
        card="Technical and on-page SEO, local SEO, and visibility in Google’s AI answers. #1 rankings on three "
             "separate sites, across a manufacturer, a school and a brand-new domain.",
        intro="SEO is a technical and strategic discipline, not a keyword list. Rankings depend on whether the "
              "site can be crawled, whether each page matches one intent, and whether the result is checked "
              "against real Search Console data. GEO extends the same work to AI Overviews, ChatGPT and "
              "Perplexity: clean structure and pages that answer real questions are what machines can read and "
              "cite.",
        best_for="Sites that should bring in buyers but don’t, and new domains that need to rank fast",
        platforms="Any CMS; deepest on WordPress and Next.js",
        deliverable="A prioritised fix list, executed, then tracked in Search Console",
        evidence="#1 for target keywords on three sites",
        scope=["Technical audit: crawl, status codes, canonicals, indexability, Core Web Vitals",
               "Keyword and search-intent research with DataForSEO and live SERP analysis",
               "Intent clustering and keyword-to-page mapping, including fixing cannibalisation",
               "On-page work: titles, headings, copy, images and internal links",
               "Schema markup: Organization, LocalBusiness / LegalService, FAQPage, ItemList and more",
               "Local SEO and Google Business Profile",
               "GEO: structure and content that Google’s AI features and LLMs can cite",
               "Monitoring through Search Console and Looker Studio, with an opportunity list for positions 10–20"],
        process=["Technical discovery: platform, hosting, security, speed",
                 "Crawl and indexation audit with Screaming Frog",
                 "Search demand, SERP and competitor research",
                 "Map one intent to one page, then fix architecture and on-page",
                 "Validate in Search Console and monitor, including AI-feature impressions"],
        proof=["tjikkofoam.com: #1 for “pabrik busa”, “produsen busa” and “busa molded”, "
               "cited in the AI Overview, ~40% more organic traffic",
               "Sekolah Trinitas: #1 for five competitive local keywords, no link building",
               "busabunga.com: #1 and page one within a month, new domain, no ads, no links",
               "nyliem.com: 1.4K impressions in Google’s Generative AI features in under three months"],
        tools=["Search Console", "Screaming Frog", "DataForSEO", "Schema.org", "Google Business Profile",
               "Looker Studio", "Claude + MCP"],
    ),
    dict(
        key="ads", title="Paid<br>ads", name="Paid ads",
        card="Meta Ads (Click-to-WhatsApp) and Google Ads, judged on the leads Sales actually qualifies, not on "
             "cheap clicks or chat counts.",
        intro="Ads that look cheap in Ads Manager can still send Sales nothing useful. I run Meta and Google "
              "campaigns, but the part that makes them work is deciding on the metric closest to revenue: cost "
              "per qualified lead, not cost per chat. That means the ads are set up so every result can be traced "
              "back to the ad that produced it.",
        best_for="B2B and local businesses selling through WhatsApp or enquiry forms",
        platforms="Meta Ads Manager, Google Ads (Search)",
        deliverable="A running account with written rules for when to keep, scale, fix or pause",
        evidence="105 CRM-qualified leads traced to individual Meta ads",
        scope=["Account and campaign structure: one ad per ad set where testing needs a clean read",
               "Audience planning and B2B segmentation",
               "Creative briefs and testing, one variable at a time: hook, format, audience, placement",
               "An ad naming taxonomy so Meta, the CRM and reports all refer to the same ad",
               "Placement control, catching Advantage+ leakage into WhatsApp Status and Reels",
               "Cut-off and scaling rules written down before reading the data",
               "Google Ads search campaigns with conversion tracking set up before spend starts"],
        process=["Review historical ad data and agree what a qualified lead is",
                 "Set up naming, tracking and the link to the CRM",
                 "Launch small, with pause / fix / scale rules agreed in advance",
                 "Read results daily against CRM-qualified leads",
                 "Move budget to what produces qualified leads and deals"],
        proof=["B2B corporate gifting (anonymised): 105 qualified leads out of 2,573 chats and 3 deals worth Rp167M "
               "traced to ads, 1 May – 15 Oct 2026",
               "Found that the cheapest chats (WhatsApp Status) produced zero qualified leads",
               "Lingga Florist Google Ads: 795 clicks, 275 conversions (34.6%) on about Rp1.04M",
               "Hands-on Meta Ads for Tjikko’s own products"],
        tools=["Meta Ads Manager", "Click-to-WhatsApp", "Google Ads", "GA4", "Google Tag Manager", "Higgsfield AI"],
    ),
    dict(
        key="crm", title="CRM &amp;<br>lead tracking", name="CRM &amp; lead tracking",
        card="Connecting ad spend to what Sales marks in the CRM, so every lead, qualified lead and deal can be "
             "traced back to the ad or page that produced it.",
        intro="Most teams have their spend in one place and their lead quality in another. Until the two are "
              "joined, nobody can say which ad or page actually produces customers. I build that join: a single "
              "source of truth where marketing data and Sales’ own verdicts sit side by side, per ad, per day.",
        best_for="Teams running ads into WhatsApp or forms, with a CRM that Sales already uses",
        platforms="Mekari Qontak, Google Sheets, Coefficient, Apps Script",
        deliverable="A tracker plus a dashboard the CEO can open without sheet access",
        evidence="Ads Monitor dashboard in production since 2026",
        scope=["Lead definitions agreed with Sales: chat, relevant lead, qualified lead, deal",
               "Daily join of Meta data and CRM leads in Google Sheets, pulled automatically with Coefficient",
               "Setting versus actual delivery tracked separately so placement leakage shows",
               "WhatsApp lead workflows and marketing-to-sales handoff",
               "An Apps Script dashboard: which ad produces qualified leads, which passed the cut-off without "
               "one, where the spend went, which creative travels across audiences",
               "Deal value traced back to the ad name",
               "Data hygiene: no public CSV links, so spend and lead data stay private"],
        process=["Map where each number lives today",
                 "Agree definitions and naming with Sales",
                 "Build the joined tracker and automate the pulls",
                 "Put a dashboard on top that answers specific questions",
                 "Hand the daily reading to an AI report, with a person deciding"],
        proof=["B2B Meta Ads + CRM case: Meta + Qontak + Sheets + Ads Monitor + daily AI analysis",
               "The joined data saved an ad that looked expensive but had produced a Rp112M deal",
               "Caught tracking errors that distort decisions, from a CPM formula to a mis-pasted WhatsApp code"],
        tools=["Mekari Qontak", "Google Sheets", "Coefficient", "Apps Script", "WhatsApp", "Looker Studio"],
    ),
    dict(
        key="analytics", title="Analytics &amp;<br>reporting", name="Analytics &amp; reporting",
        card="GA4, Google Tag Manager, Search Console and Looker Studio, set up so the numbers answer a business "
             "question instead of filling a dashboard nobody opens.",
        intro="Optimisation is only as good as the instrumentation underneath it. Where one link in the chain is "
              "missing, decisions fall back to platform metrics. Most of my measurement work is closing those "
              "gaps, then building reports that a director can read in two minutes.",
        best_for="Businesses that can’t tell what’s working, and boards that want one clear report",
        platforms="GA4, Google Tag Manager, Search Console, Looker Studio",
        deliverable="Working tracking plus a dashboard built around specific questions",
        evidence="Looker Studio dashboards reported to Tjikko’s Board",
        scope=["GA4 property setup and event design, implemented through Google Tag Manager",
               "Conversion measurement: WhatsApp clicks, forms, calls",
               "UTM conventions so campaign traffic is attributable",
               "Search Console setup, verification and query analysis",
               "Looker Studio dashboards, including SEO performance and opportunity queries",
               "Board-level reporting that separates fact from hypothesis"],
        process=["Agree the business questions first",
                 "Audit what is tracked today and what is broken",
                 "Implement events and conversions through GTM",
                 "Build the dashboard around the questions",
                 "Automate the recurring report"],
        proof=["Tjikko: GA4/GTM tracking and Looker Studio dashboards for the Board of Directors",
               "nyliem.com: Looker Studio SEO dashboard, 89 queries in positions 1–10 (+23.6%)",
               "Hermes GA4 Daily Reporter across three properties"],
        tools=["GA4", "Google Tag Manager", "Search Console", "Looker Studio", "Google Sheets", "Site Kit"],
    ),
    dict(
        key="ai", title="AI<br>automation", name="AI automation",
        card="Claude, MCP and n8n workflows that take recurring manual checks and reports off a team’s plate, "
             "running in production with a person kept on the decision.",
        intro="AI is useful where a task repeats every day and follows rules: reading data, checking documents, "
              "flagging anomalies, drafting a report. I build those systems on infrastructure I run myself, and "
              "keep them as decision support: the AI reads and recommends, a person decides and acts.",
        best_for="Teams with a daily manual check, report or reconciliation",
        platforms="Claude API, Claude Code, MCP, n8n, self-hosted VPS",
        deliverable="A scheduled workflow in production, with its failure handling",
        evidence="Three AI systems running in production",
        scope=["Scheduled AI checks on business documents, e.g. purchase orders against quotations",
               "Daily AI analysis of ads and CRM data with a fixed format: observation, why it matters, action, "
               "metric to watch",
               "Automated GA4 and SEO audit reports delivered to Discord or email",
               "MCP connections into Google Drive, Gmail, WordPress, DataForSEO and analytics",
               "n8n workflows for scheduling, retries and content drafts that a person reviews before publishing",
               "AI content pipelines for brand assets, editing real product photos rather than inventing products",
               "Internal tools and sites built with Claude Code"],
        process=["Pick a task that repeats and has clear rules",
                 "Write the business rules down, then into the prompt",
                 "Connect to the data where it already lives, via MCP",
                 "Run on a schedule with visible failures, not silent ones",
                 "Keep a person on the decision and measure before claiming time saved"],
        proof=["Quotation vs PO validation: hourly Claude check, live at Tjikko since July 2026",
               "Hermes: GA4 Daily Reporter across three properties and a daily SEO audit for busabunga.com",
               "Daily AI Meta Ads report recommending KEEP / SCALE / FIX / PAUSE per ad",
               "AI content pipeline producing 50+ brand assets a month"],
        tools=["Claude API", "Claude Code", "MCP", "n8n", "RAG", "Docker", "Self-hosted VPS", "Git"],
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

                <button class="mfp-close permanent-dark" type="button" aria-label="Close"></button>

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
                        <a class="link-small-underline" href="https://seoflow-ai.vercel.app" target="_blank" rel="noopener">SEOFlow AI Dashboard</a>,
                        a full-stack SEO and AI-visibility dashboard on Next.js, TypeScript, Supabase and Vercel; an n8n
                        workflow that drafts articles with an AI agent and posts them to WordPress for review; and
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

SERVICE_CARD = '''                          <!-- services cards grid single item -->
                          <div class="col-12 col-md-6 cards__item grid-item animate-card-2">
                            <div data-mfp-src="#service-{key}" class="cards__card cards__card--text service-card popup-trigger d-flex flex-column"
                                 role="button" tabindex="0" aria-label="Read more about {name}">
                              <div class="cards__descr">
                                <h3 class="cards__title animate-in-up">{title}</h3>
                                <p class="cards__text type-basic-160lh animate-in-up">{card}</p>
                                <span class="service-card__more">Read more <i class="ph ph-arrow-up-right"></i></span>
                              </div>
                            </div>
                          </div>
'''

SERVICE_CARDS = '''                  <!-- Content Block - Services/Features Cards V2 Block Start -->
                  <div class="content__block grid-block">
                    <div class="container-fluid p-0">
                        <div class="row g-0 align-items-stretch cards">
%s                        </div>
                      </div>
                  </div>
                  <!-- Content Block - Services/Features Cards V2 Block End -->
'''

# Service popups reuse the project popup chrome minus the cover image. They
# carry the "Project Popup" markers so the popup splice below owns them too.
SERVICE_POPUP = '''              <!-- Project Popup - Service: {key} Start -->
              <div id="service-{key}" class="popup mfp-hide">

                <button class="mfp-close permanent-dark" type="button" aria-label="Close"></button>

                <div class="popup__container">
                  <div class="container-fluid p-0">
                    <div class="row g-0">
                      <div class="col-12">
                        <div class="project">

                          <!-- Project Block - Service Title Start -->
                          <div class="project__block service-popup__head">
                            <p class="tagline-chapter small">Service</p>
                            <h3 class="service-popup__title">{name}</h3>
                          </div>
                          <!-- Project Block - Service Title End -->

                          <!-- Project Block - Description Start -->
                          <div class="project__block grid-block grid-items">
                            <div class="project__data">
                              <div class="container-fluid p-0">
                                <div class="row g-0">
                                  <div class="col-12 col-xl-4">
                                    <div class="container-fluid p-0">
                                      <div class="row g-0">
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Best for</p>
                                          <p class="data__descr small type-basic-160lh">{best_for}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Platforms</p>
                                          <p class="data__descr small type-basic-160lh">{platforms}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">You get</p>
                                          <p class="data__descr small type-basic-160lh">{deliverable}</p>
                                        </div>
                                        <div class="col-12 col-md-6 grid-item pdata__item">
                                          <p class="data__title tagline-chapter small type-basic-160lh">Evidence</p>
                                          <p class="data__descr small type-basic-160lh">{evidence}</p>
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

{blocks}
                          <!-- Project Block - Contact Link Start -->
                          <div class="project__block small-size">
                            <div class="container-fluid p-0">
                              <div class="row g-0">
                                <div class="col-12 d-flex justify-content-center">
                                  <a class="btn btn-circle-text hover-circle popup-to-contact" href="#contact">
                                    <em></em>
                                    <span class="btn-caption">Discuss a project</span>
                                  </a>
                                </div>
                              </div>
                            </div>
                          </div>
                          <!-- Project Block - Contact Link End -->

                        </div>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
              <!-- Project Popup - Service: {key} End -->
'''


def build_service_popup(sv):
    blocks = [
        BLOCK.format(label="What I do", body=bullets(sv["scope"]), extra=" pre-grid-items"),
        BLOCK.format(label="How I work", body=bullets(sv["process"]), extra=""),
        BLOCK.format(label="Proof on this page", body=bullets(sv["proof"]), extra=""),
        BLOCK.format(label="Tools", body=tags(sv["tools"]), extra=""),
    ]
    return SERVICE_POPUP.format(blocks="\n".join(blocks), **sv)


service_cards_html = SERVICE_CARDS % "".join(SERVICE_CARD.format(**sv) for sv in SERVICES)

popups_html = "\n".join([build_popup(p) for p in PROJECTS] + [build_service_popup(sv) for sv in SERVICES])

# ---------------------------------------------------------------- process
#
# "How I work on a project": an interactive stepper (js/custom.js) with a mini
# Trello board whose card moves to the list the current step lives in. Without
# JavaScript every step stays visible as a plain list.
# Payment terms and revision counts are deliberately not stated here: they are
# set per project in the proposal.

BOARD = ["Brief", "Planned", "In progress", "Client review", "Done"]

STEPS = [
    dict(title="Discuss your needs", short="Discovery call", board=0, time="30–60 minute call",
         text="We talk about the business first: what the project is for, who it has to reach, what counts as a "
              "result (an enquiry, a registration, a qualified lead), the deadline and the budget range. I look at "
              "your current site, ads or data before the call so the time goes on decisions, not on explaining.",
         you_get="A short written summary of what I understood, so we agree on the problem before any price.",
         your_part="Your goals, examples you like, and access to whatever already exists."),
    dict(title="Proposal &amp; quote", short="Proposal", board=0, time="A few working days",
         text="A written proposal with the scope, the deliverables, what is out of scope, the timeline, the price, "
              "the payment terms and how many revision rounds are included. If something is uncertain, the "
              "proposal says so and prices it as an option rather than hiding it.",
         you_get="A clear proposal you can compare, forward to your team, and sign off.",
         your_part="Read it, ask anything, and say what to change."),
    dict(title="Agreement &amp; kickoff", short="Kickoff", board=1, time="Same week as sign-off",
         text="Once the proposal is approved and the first payment is in, we hold a kickoff. I collect the access "
              "I need (hosting, domain, CMS, GA4, Search Console, ad accounts) and the content you already have, "
              "and we confirm one contact person on your side for approvals.",
         you_get="A confirmed start date and a list of what I still need from you.",
         your_part="Access, existing content and brand files, one decision-maker."),
    dict(title="Timeline on Trello", short="Timeline", board=1, time="Shared at kickoff",
         text="The project is planned on a Trello board that you can open any time: every task is a card, every "
              "milestone has a date, and cards move from Planned to In progress to Client review to Done. You "
              "always know what is happening without having to ask, and comments stay attached to the task they "
              "are about.",
         you_get="A live Trello board with milestones and due dates.",
         your_part="Watch progress, comment on cards whenever you like."),
    dict(title="Build &amp; execute", short="Build", board=2, time="Per the timeline",
         text="Design, build, SEO, tracking or ads set-up, depending on the project. Work happens on a staging link "
              "or in draft so nothing breaks your live site, and GA4 and Search Console are wired in before launch "
              "rather than after. You get a progress update every week, with a link to see it for yourself.",
         you_get="Weekly updates and a staging link to preview the work.",
         your_part="Send content on time; flag anything that changes in the business."),
    dict(title="Review &amp; revisions", short="Revisions", board=3, time="Rounds agreed in the proposal",
         text="You review the work on staging. Feedback goes onto the Trello board as one card per point, so nothing "
              "gets lost in a chat thread and each fix can be checked off. Revisions follow the rounds agreed in the "
              "proposal; anything new is quoted separately before I start it, so there are no surprises on the bill.",
         you_get="Every point addressed and ticked off on the board.",
         your_part="Consolidated feedback per round, from the agreed decision-maker."),
    dict(title="Launch &amp; handover", short="Launch", board=4, time="Launch day + handover",
         text="Go live, then check what matters on day one: indexing, redirects, forms and WhatsApp links, "
              "conversions in GA4, and speed. You get the handover: credentials back in your name, a short guide or "
              "video on how to update the site, and the final invoice.",
         you_get="A live, measured site you own, plus a handover guide.",
         your_part="Final approval and the last payment."),
    dict(title="Aftercare &amp; growth", short="Aftercare", board=4, time="After launch",
         text="A support window after launch for anything that turns up. For SEO and ads retainers, a monthly "
              "report built on Search Console, GA4 and CRM data, with what changed, why, and what I will do next. "
              "The findings feed straight back into step one.",
         you_get="Support after launch and, on retainers, a monthly report.",
         your_part="Tell me what the business needs next."),
]

STEP_TAB = '''                          <li role="presentation">
                            <button class="process__tab" type="button" role="tab" id="process-tab-{n}"
                                    aria-controls="process-panel-{n}" aria-selected="{sel}" tabindex="{ti}"
                                    data-board="{board}">
                              <span class="process__num">{num}</span>
                              <span class="process__name">{short}</span>
                            </button>
                          </li>
'''

STEP_PANEL = '''                        <div class="process__panel" role="tabpanel" id="process-panel-{n}" aria-labelledby="process-tab-{n}">
                          <p class="process__eyebrow tagline-chapter small">Step {num} &middot; {time}</p>
                          <h3 class="process__title">{title}</h3>
                          <p class="process__text type-basic-160lh">{text}</p>
                          <div class="process__meta">
                            <div>
                              <p class="process__label small">You get</p>
                              <p class="small type-basic-160lh">{you_get}</p>
                            </div>
                            <div>
                              <p class="process__label small">Your part</p>
                              <p class="small type-basic-160lh">{your_part}</p>
                            </div>
                          </div>
                        </div>
'''

PROCESS_SECTION = '''      <!-- Inner Section - Process - Start -->
      <section id="process" class="inner inner-grid-bottom">
        <div class="inner__wrapper">
          <div class="container-fluid p-0">
            <div class="row g-0">

              <!-- Inner Section Name Start -->
              <div class="col-12 col-xl-2">
                <div class="inner__name">
                  <div class="content__block name-block">
                    <span class="section-name icon-right animate-in-up">
                      <span class="section-name-caption">Process</span>
                      <i class="ph ph-arrow-down-right"></i>
                    </span>
                  </div>
                </div>
              </div>
              <!-- Inner Section Name End -->

              <!-- Inner Section Content Start -->
              <div class="col-12 col-xl-8">
                <div class="inner__content">

                  <div class="content__block section-grid-title">
                    <div class="block__descr">
                      <h2 class="reveal-type animate-in-up">How I work<br>on a project</h2>
                    </div>
                  </div>

                  <div class="content__block">
                    <p class="process__intro type-basic-160lh animate-in-up">The same eight steps on every
                      project, from the first call to aftercare. Every task lives on a shared Trello board, so you can
                      see where things stand at any time. Click a step.</p>

                    <div class="process" data-process>
                      <div class="process__progress" aria-hidden="true"><span></span></div>
                      <ol class="process__tabs" role="tablist" aria-label="Project steps">
{tabs}                      </ol>

                      <div class="process__body">
                        <div class="process__panels">
{panels}                        </div>

                        <div class="process__board" aria-label="Trello board preview">
                          <p class="process__board-title small"><i class="ph ph-squares-four"></i> Trello &middot; project board</p>
                          <div class="process__lists">
{lists}                          </div>
                        </div>
                      </div>

                      <div class="process__nav">
                        <button class="process__btn process__btn--prev" type="button" data-step="-1" aria-label="Previous step">
                          <i class="ph ph-arrow-right"></i>
                        </button>
                        <span class="process__count small" aria-live="polite">Step <b>1</b> of {total}</span>
                        <button class="process__btn" type="button" data-step="1" aria-label="Next step">
                          <i class="ph ph-arrow-right"></i>
                        </button>
                      </div>
                    </div>

                    <div class="process__cta animate-in-up">
                      <a class="btn btn-default hover-default" href="#contact">
                        <em></em>
                        <span class="btn-caption">Start with step 1</span>
                      </a>
                    </div>
                  </div>

                </div>
              </div>
              <!-- Inner Section Content End -->

              <div class="col-12 col-xl-2"></div>

            </div>
          </div>
        </div>
      </section>
      <!-- Inner Section - Process - End -->

'''

BOARD_LIST = '''                            <div class="process__list" data-list="{i}">
                              <p class="process__list-name">{name}</p>
                              <div class="process__slot"></div>
                            </div>
'''

process_html = PROCESS_SECTION.format(
    tabs="".join(STEP_TAB.format(n=i + 1, num="%02d" % (i + 1), sel="true" if i == 0 else "false",
                                 ti="0" if i == 0 else "-1", **st) for i, st in enumerate(STEPS)),
    panels="".join(STEP_PANEL.format(n=i + 1, num="%02d" % (i + 1), **st) for i, st in enumerate(STEPS)),
    lists="".join(BOARD_LIST.format(i=i, name=name) for i, name in enumerate(BOARD)),
    total=len(STEPS))

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

# 4. service cards
s = replace_between(
    s,
    r"[ \t]*<!-- Content Block - Services/Features Cards V2 Block Start -->",
    r"[ \t]*<!-- Content Block - Services/Features Cards V2 Block End -->\n",
    service_cards_html, "service cards")

# 5. process section, between Services and Resume
if "<!-- Inner Section - Process - Start -->" in s:
    s = replace_between(
        s,
        r"[ \t]*<!-- Inner Section - Process - Start -->",
        r"[ \t]*<!-- Inner Section - Process - End -->\n\n",
        process_html, "process")
else:
    i = s.index("      <!-- Inner Section - Resume - Start -->")
    s = s[:i] + process_html + s[i:]

io.open(path, "w", encoding="utf-8").write(s)
print("featured: %d, other: %d, services: %d, popups: %d"
      % (len(featured), len(others), len(SERVICES), len(PROJECTS) + len(SERVICES)))
