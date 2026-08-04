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
        type="Website build + SEO", date="Launched June 2026",
        role="Design, build, SEO", client="PT Tjikko Sentral Industrial",
        url=("Visit busabunga.com", "https://busabunga.com"),
        intro="A commercial site for Tjikko's decorative foam (busa bunga) line, built end to end in React with "
              "Claude Code as the development partner. Design, build, content and search strategy were all mine. "
              "There was no existing site, no legacy traffic, and no ad budget to lean on.",
        scope=["Keyword and intent research before any code was written",
               "Information architecture built around buyer intent, not the product catalogue",
               "Full React build, AI-assisted with Claude Code",
               "Technical SEO foundation: crawlability, schema, Core Web Vitals",
               "Long-tail landing pages for florists, wholesale buyers and private-label enquiries",
               "Search Console and analytics set up from day one"],
        challenge="A brand-new domain competing for commercial keywords that established suppliers and marketplaces "
                  "already owned. No backlink profile, no history, and no paid support. The only route to visibility "
                  "was getting the technical foundation and the search intent right the first time.",
        approach="I mapped the commercial keyword set before writing a line of code, then shaped the site structure "
                 "around how buyers actually search rather than how the company organises its products. Primary terms "
                 "were floral foam, wet and dry floral foam, busa bunga and floral foam indonesia; secondary terms "
                 "covered supplier, distributor, grosir and private-label variations. Each target term got a single "
                 "page that clearly owned it, so no two pages competed with each other.",
        result="Within roughly one month of launch the site held #1 and page-one Google positions for its target "
               "commercial keywords \u2014 a result that came from structure and intent matching rather than from "
               "authority it had not had time to build.",
        stack=["React", "Claude Code", "Technical SEO", "Search Console", "GA4"],
    ),
    dict(
        key="trinitas", featured=True, img="trinitas",
        title="Sekolah Trinitas",
        tagline="#1 for five competitive local keywords",
        type="Local SEO", date="2026", role="SEO &amp; website developer",
        client="Sekolah Trinitas \u2014 via RIAS Strategic",
        url=("Visit sekolahtrinitasbdl.sch.id", "https://sekolahtrinitasbdl.sch.id"),
        intro="Local search work for a Christian trilingual school in Bandar Lampung, delivered through the RIAS "
              "Strategic freelance talent pool. The brief was simple to state and hard to win: own the terms parents "
              "actually type when they are choosing a school.",
        scope=["Keyword mapping across the five priority local terms",
               "On-page rewrite so each term had one page earning it",
               "Technical fixes and crawl clean-up",
               "Local relevance signals tightened",
               "Rank tracking against the target set"],
        challenge="Education keywords in a regional market are crowded with directories, aggregators and long-"
                  "established institutions. Ranking meant beating pages with far more authority, on terms where "
                  "realistically only the top result converts \u2014 parents do not scroll for a school.",
        approach="I rebuilt the on-page and technical foundation around the five keywords that mattered and made sure "
                 "each one had a clear, single page earning it, which removed the cannibalisation that was splitting "
                 "the site's own relevance. Local signals were tightened so the school read unambiguously as a "
                 "Bandar Lampung institution.",
        result="#1 Google rankings for all five target keywords: sekolah kristen lampung, sekolah kristen terbaik "
               "lampung, sekolah trilingual terbaik lampung, sekolah trilingual lampung, and sekolah kristen lampung "
               "paling bagus.",
        stack=["WordPress", "Technical SEO", "Local SEO", "Search Console"],
    ),
    dict(
        key="tjikko", featured=True, img="tjikko",
        title="Tjikko Foam",
        tagline="Four years owning an entire digital function",
        type="Website, SEO &amp; digital ownership", date="2021 \u2014 present",
        role="IT &amp; Digital Specialist", client="PT Tjikko Sentral Industrial",
        url=("Visit tjikkofoam.com", "https://tjikkofoam.com"),
        intro="For four years I have been the entire digital and IT function at a B2B polyurethane foam manufacturer. "
              "Websites, SEO, analytics, brand and packaging design, video, marketplace channels, cybersecurity, "
              "servers and procurement \u2014 with reporting that goes up to the Board.",
        scope=["Corporate site rebuilt on WordPress and Elementor with an SEO-first structure",
               "Technical SEO: Core Web Vitals, schema markup, crawl and index hygiene",
               "GA4, Google Tag Manager, Looker Studio and Search Console",
               "Indotrading listing built from scratch, including coordination with their account team",
               "Full design ownership: catalogues, company profile, logos, packaging, video, listing visuals",
               "Wazuh SIEM deployed across 50+ devices",
               "Servers, Cloudflare, Docker, and IT procurement",
               "Client-facing and Board-level presentations"],
        challenge="A B2B industrial manufacturer with a technical product, a long sales cycle and no paid advertising "
                  "budget. Every lead had to be earned through organic search. There was also no team \u2014 nothing "
                  "could be delegated, so everything had to be built to run without much maintenance.",
        approach="I rebuilt the site around the language buyers actually search with instead of internal product "
                 "naming, then fixed the technical foundation underneath it. Analytics went in so that performance "
                 "became something the business could see and argue about, rather than a black box. On the "
                 "infrastructure side I standardised monitoring so problems surfaced before they became downtime.",
        result="~40% growth in organic traffic and a ~25% increase in lead generation, entirely SEO-driven with no "
               "paid advertising. On the infrastructure side, roughly 30% less downtime.",
        stack=["WordPress", "Elementor", "Technical SEO", "GA4", "GTM", "Looker Studio", "Cloudflare", "Wazuh SIEM"],
    ),
    dict(
        key="hermes", featured=True, img="hermes",
        title="Hermes AI Agent System",
        tagline="A self-hosted agent stack doing real daily work",
        type="AI automation", date="2026 \u2014 ongoing",
        role="Architect &amp; builder", client="Self-hosted / internal",
        url=None,
        intro="A self-hosted multi-agent system running real daily work \u2014 not a demo and not a prototype. Claude "
              "API handles the reasoning, n8n orchestrates the workflows, and MCP connects the whole thing to live "
              "WordPress sites and analytics properties.",
        scope=["Multi-agent framework running on a self-hosted VPS",
               "Claude API as the reasoning engine",
               "n8n for scheduling and workflow orchestration",
               "Claude Desktop + MCP connected to live WordPress sites",
               "Claude Code and Git development workflow",
               "RAG architecture for document grounding",
               "Full multi-page client website builds executed through MCP",
               "SEO, GEO and AEO documentation systems",
               "GA4 audits and a daily reporting agent"],
        challenge="Most AI automation stops at the proof-of-concept stage \u2014 impressive in a screenshot, "
                  "unreliable the moment it has to run unattended against production systems. The hard part is not "
                  "the model call; it is everything around it: scheduling, error handling, credentials, and knowing "
                  "when the output is wrong.",
        approach="I built Hermes as infrastructure rather than as a script. Agents are composable skills with a Git "
                 "workflow behind them, MCP handles the integrations into live systems, and n8n owns scheduling and "
                 "retries. A separate system, built on Claude scheduled tasks with MCP into Google Drive and Gmail, "
                 "validates customer quotations against purchase orders on line items, pricing and expiry, and "
                 "reports hourly.",
        result="A GA4 Daily Reporter runs in production across three properties. The quotation validation layer has "
               "been live since July 2026. It is deliberately too early to claim a catch rate or a time saving \u2014 "
               "those numbers will exist once the system has a real track record behind it.",
        stack=["Claude API", "Claude Code", "MCP", "n8n", "Docker", "Self-hosted VPS", "RAG"],
    ),
    dict(
        key="invera", featured=True, img="invera",
        title="Invera Wedding",
        tagline="Wedding platform built for first impressions",
        type="Website development", date="2025", role="Website developer",
        client="Invera Wedding \u2014 via RIAS Strategic",
        url=("Visit inverawedding.web.id", "https://inverawedding.web.id"),
        intro="A wedding service platform built through the RIAS Strategic talent pool \u2014 one of a run of projects "
              "spanning SMEs, companies and factories.",
        scope=["WordPress and Elementor build",
               "Service and package presentation",
               "Gallery setup",
               "Local SEO fundamentals"],
        challenge="Wedding sites live or die on first impression. The design had to feel personal and unhurried while "
                  "still loading quickly on the phones most guests would actually open it on \u2014 image-heavy and "
                  "fast are not natural allies.",
        approach="An image-led build with the couple's story and the enquiry flow as the spine of the layout, tuned so "
                 "the photography stays sharp without making the page heavy.",
        result="Delivered and live, with a structure that supports service enquiries rather than just looking good.",
        stack=["WordPress", "Elementor", "Local SEO"],
    ),
    dict(
        key="nyliem", featured=True, img="nyliem",
        title="Ny Liem Heritage",
        tagline="Heritage brand, translated to the web",
        type="Website development", date="2025", role="Website developer",
        client="Ny Liem Heritage \u2014 via RIAS Strategic",
        url=("Visit nyliem.com", "https://nyliem.com"),
        intro="A brand site for a heritage culinary business with a long story and an established product line, also "
              "delivered through RIAS Strategic.",
        scope=["WordPress design and build",
               "Brand storytelling layout",
               "SEO-ready page structure"],
        challenge="Translating an established offline brand identity into a web presence without flattening the "
                  "character that made it recognisable in the first place. Heritage brands lose more than they gain "
                  "from a generic modern template.",
        approach="The build leads with the brand's own visual language and keeps the interface deliberately quiet, so "
                 "the heritage does the talking.",
        result="A premium digital presence that carries the brand's story rather than replacing it.",
        stack=["WordPress", "Elementor", "Brand design"],
    ),

    # ---------------------------------------------------------- other work
    dict(
        key="tjikko-global", featured=False, img="tjikko-global",
        title="Tjikko Foam Global",
        tagline="Export-facing platform",
        type="International website", date="2026", role="Build &amp; international SEO",
        client="PT Tjikko Sentral Industrial",
        url=("Visit global.tjikkofoam.com", "https://global.tjikkofoam.com"),
        intro="A dedicated global-facing site positioning Tjikko Foam for international wholesale buyers, distributors "
              "and export partners beyond Indonesia.",
        scope=["Next.js build",
               "Global information architecture with English-first messaging",
               "International on-page SEO",
               "Cloudflare performance and security layer",
               "Enquiry flow designed for cross-border leads"],
        challenge="Domestic B2B messaging does not transfer. International procurement teams look for specifications, "
                  "capacity and credibility signals long before they look at brand.",
        approach="I restructured the content around what an overseas buyer needs to verify first, kept the product "
                 "specifications explicit, and separated the export proposition from the domestic site so neither had "
                 "to compromise for the other.",
        result="A distinct international presence built to capture export demand and convert overseas visitors into "
               "qualified enquiries.",
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
              "distributors.",
        scope=["WordPress and Elementor design and build",
               "Product catalogue structure",
               "On-page SEO foundation"],
        challenge="Chemical distribution is a credibility-first category. The site had to make an unglamorous "
                  "catalogue legible and trustworthy to procurement buyers who compare on specification.",
        approach="A clean catalogue structure that puts specifications where buyers look for them, on a foundation "
                 "that can be found in search rather than only handed out as a link.",
        result="A professional digital presence that represents the brand credibly to industrial buyers.",
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
              "belong to as a UI/UX and website developer. Their own site was one of the projects I delivered.",
        scope=["WordPress design and build",
               "Service page structure",
               "Brand-aligned visual layout"],
        challenge="A services business has nothing physical to show. Credibility has to come from how clearly the "
                  "offer is structured and how easily a prospect can work out whether it applies to them.",
        approach="Service pages structured around the client's problem rather than the agency's internal divisions, "
                 "with a visual layout that stays consistent with the existing brand.",
        result="A platform ready for client acquisition and service promotion.",
        stack=["WordPress", "Elementor", "UX layout"],
    ),
    dict(
        key="pawcharm", featured=False, img="pawcharm",
        title="The Paw Charm",
        tagline="Direct-to-consumer pet accessories",
        type="E-commerce", date="2025", role="Store build",
        client="The Paw Charm",
        url=("Visit thepawcharmstore.com", "https://thepawcharmstore.com"),
        intro="An e-commerce store for a pet accessories brand selling directly to consumers \u2014 a different "
              "problem from the B2B work: impulse-led, mobile-first, and dependent on checkout not getting in the way.",
        scope=["Shopify store setup",
               "Product catalogue and collections",
               "Checkout optimisation"],
        challenge="Consumer retail forgives nothing at checkout. Every extra step between wanting the product and "
                  "owning it costs conversions.",
        approach="A catalogue organised the way shoppers browse rather than the way inventory is filed, with the "
                 "checkout path kept as short as the platform allows.",
        result="An operational store ready to sell, with the fulfilment and catalogue structure in place behind it.",
        stack=["Shopify", "E-commerce setup", "Product catalogue"],
    ),
    dict(
        key="lingga", featured=False, img="lingga",
        title="Lingga Florist",
        tagline="Florist site plus a paid search campaign",
        type="Website + Google Ads", date="2023", role="Build &amp; campaign",
        client="Lingga Florist",
        url=("Visit linggaflorist.com", "https://linggaflorist.com/"),
        intro="A florist store website, plus a Google Ads campaign I ran as a personal project between August and "
              "September 2023. It is the one place in my work where I have run paid search end to end rather than "
              "relying on organic.",
        scope=["Website build and product presentation",
               "Google Ads campaign structure and targeting",
               "Conversion tracking setup",
               "Ongoing optimisation across the campaign period"],
        challenge="Florists compete on immediacy \u2014 people buy flowers with a deadline. The campaign had to catch "
                  "high-intent searches at the moment of need on a small budget.",
        approach="Tight keyword targeting around purchase-intent terms, with conversion tracking in place from the "
                 "start so budget could be moved toward what was actually converting rather than what was getting "
                 "clicks.",
        result="Across the campaign period: 261,000+ impressions, 795 clicks, 275 conversions, and a 34.6% conversion "
               "rate on roughly Rp 1.04M of total spend.",
        stack=["WordPress", "Google Ads", "Conversion tracking"],
    ),
]

# ---------------------------------------------------------------- markup

STACK_ITEM = '''                          <!-- portfolio stack single item -->
                          <div class="stack-item">
                            <div data-mfp-src="#project-{key}" class="portfolio-stack__inner portfolio-item-{n} popup-trigger">
                              <div class="portfolio-stack__descr">
                                <h5 class="portfolio-stack__title light">{title}</h5>
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
                                    <p class="project__subtitle tagline-chapter">{label}</p>
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
                      <p class="tagline-chapter animate-in-up">Other work</p>
                    </div>
                    <!-- Section Subtitle End -->

                    <div class="container-fluid p-0">
                      <div class="row g-0 align-items-stretch">
%s                      </div>
                    </div>

                    <p class="type-basic-160lh animate-in-up work-note">Two more corporate sites \u2014 Agromas Tapioca
                      and Agromas Crackers \u2014 are in development and will be added once they are live.</p>

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
