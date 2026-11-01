# docs-parallax-web-dyrn

Working context for **dyrn-site**, the personal website. Read this before changing
anything here.

`README.md` next door covers *how to build and deploy*. This file covers *why things
are the way they are*, what has already been decided, and what is deliberately unfinished.

- **Live:** https://dyrnzefanya.github.io/personal-site/
- **Repo:** `Dyrnzefanya/personal-site` (public, GitHub Pages from `main`, folder `/`)
- **Local:** `D:\CV\dyrn-site`
- **Last session:** 1 November 2026

---

## 1. The boundary: CV work vs website work

`D:\CV` holds two unrelated bodies of work that happen to share a parent folder. Mixing
them up is the single easiest way to break something, so this is the first section.

### This is website work

| Path | What it is |
|---|---|
| `D:\CV\dyrn-site\` | **This project.** The entire live site. Nothing outside it is deployed. |
| `D:\CV\Personal-HTML\` | The purchased HTML templates. Blayden is the one in use; the others were evaluated and rejected. Also holds `CONTENT-MAP.md`, the original content plan. |
| `D:\CV\Portfoliodyrn\` | The **old** portfolio site plus the source mockup images. Read-only reference now — project screenshots were taken from here. Not deployed. |

### This is CV / job-application work — do not touch it for website changes

| Path | What it is |
|---|---|
| `D:\CV\Docs\` | **The source of truth.** `Dyrn_Verified_Facts_Memory.md` governs every factual claim, on the CV *and* on the site. `Resume_Strategist_Instructions_v4.md` is the process doc. |
| `D:\CV\SecondBrain\` | Structured notes per project, employer and proof point. Richest source of project detail. |
| `D:\CV\master resume\` | Master CV files. `dyrn.jpg` — the hero portrait — came from here. |
| `D:\CV\cover letter\`, `CV EDIT\`, `CLAUDE CV\`, `Output\`, `tessa cv\`, `company\` | CV variants, cover letters, per-employer applications. Irrelevant to the site. |
| `D:\CV\templates\`, `tools\`, `SERP\` | Tooling for the CV/job-search workflow, not for the site. |

### Where they legitimately meet

Exactly two places:

1. **Facts.** Site copy and CV copy must agree, because a recruiter reads both. The
   Verified Facts Memory is the arbiter for both. If a claim changes there, it changes
   in both places.
2. **The CV PDF.** The site links to a downloadable CV. That file is produced by the CV
   workflow and *consumed* by the site. See §6 — it is currently withheld on purpose.

Everything else is separate. A website task should never require editing anything in
`Docs\`, `SecondBrain\` or `master resume\`; those are inputs, and they are read-only
from this side.

---

## 2. What the site is trying to do

One page, two audiences:

- **Recruiters** enter through *Resume* and *About*, and want to leave with a CV.
- **Freelance clients** enter through *Services* and *Portfolio*, and want to start a
  conversation.

The design decisions follow from that split: two peer calls-to-action in the hero, an
enquiry-type dropdown on the contact form, and a portfolio that has to prove both
"can build things" and "gets results".

Positioning, in the site's own words: WordPress developer and SEO specialist, Jakarta,
eight years across IT and digital. The through-line is that he has been an entire
digital and IT department by himself for four years.

---

## 3. Current state

**1 Nov 2026 update:** content re-aligned to the Master Portfolio 2026. Added the B2B Meta
Ads + CRM case (featured, `portfolio-item-8`, image from the portfolio PDF dashboard) and
Jakarta Law Firm (other work, screenshot taken headless). Featured stack is now 7 cards
(`.portfolio-item-5` … `-11`), other work 8 tiles (STIE Gentiaras added), 14 project popups
plus 6 service popups: Website development, SEO & GEO, Paid ads, CRM & lead tracking,
Analytics & reporting, AI automation. Services card 3 became
"Ads & analytics"; tech stack gained an "Ads & CRM" row; education gained a Training row.


Live and working:

- Single page: home · portfolio · about · services · resume · contact
- **12 project case studies**, each with type/date/role/client, an intro, a scope list,
  the challenge, the approach, the result, a stack tag row, and a live-site link
- Six featured in a scroll-driven stack, six in an "Other work" tile grid
- Real portrait in the hero, monochrome-treated
- `llms.txt`, `sitemap.xml`, JSON-LD entity graph, visible "last updated" date
- Accessibility: pinch zoom restored, real form labels, skip link, focus rings,
  heading hierarchy with no skipped levels

Commit history so far:

```
1ad4cee  Fix heading hierarchy, and remove a flower growing out of my shoulder
1045212  Add docs-parallax-web-dyrn: working context for future sessions
acfc929  Hero: real portrait, anchored bottom-right and treated for legibility
9a3eeca  Portfolio: deepen every case study and rebalance what it proves
5a44cfb  SEO, AI-search and accessibility pass
7d6cd61  Hero: use the template's cutout objects as placeholder decoration
2a14442  README: record the live Pages URL
6da9497  Personal site: portfolio, resume and services in one page
```

---

## 4. How the work went, and why

Chronological, because several decisions only make sense in order.

### 4.1 Template selection

Seven templates were in `Personal-HTML`. Each was served locally and rendered rather
than judged from its thumbnail. **Blayden demo-2** won because it was the only one with
both a *Services* section (freelance) and a *Resume* section (hiring), it scrolls
normally, and it was the newest and least jQuery-bound.

Rejected, with reasons worth remembering so they are not re-litigated: Gilber and Roger
hijack scrolling with `pagepiling` (bad for a long CV and bad for SEO); Roberto scrolls
horizontally; Profession looks like 2016; Merge is a WordPress theme, not HTML.

### 4.2 Content

Every line was written from `Docs\Dyrn_Verified_Facts_Memory.md`. The blocklist in that
file was applied literally — see §5.

The old portfolio's testimonials were **not** carried over. They carry their own
disclaimer: *"representational and pending formal client approval for publication."*
Unapproved quotes do not go on a public site.

### 4.3 Weight

The template shipped at 21 MB with 1054 KB of render-blocking CSS. Now 11 MB, with
`plugins.css` at 318 KB (~37 KB gzipped by Pages). Removed: FontAwesome (zero `fa-`
classes), unused Phosphor icon weights and ~5,800 unused glyph rules, legacy `.ttf`/`.svg`
font formats, demo image folders, `-demo.css` files, the Vegas plugin.

The icon subsetting is **scripted, not hand-edited** — it reads the icon list out of
`index.html`. If you add a new `ph-*` icon to the markup its CSS rule will be missing;
re-run the subsetter against a fresh `plugins.css` or add the one `content:` rule by hand.

### 4.4 Deployment

Deliberately a **project site** under a sub-path, not the root user site. The root repo
`dyrnzefanya.github.io` already exists, is live, and contains a `Personality-Test` folder;
overwriting it was not worth it. The cost of that choice is real and is documented in §7.

### 4.5 SEO / AI-search pass

Added `llms.txt`, `sitemap.xml`, a JSON-LD `@graph` (ProfilePage + WebSite + Person +
an ItemList of seven projects, cross-linked by `@id`), and a machine-readable
`dateModified` plus a visible "last updated" line.

Accessibility problems found — all of them shipped by the template, none introduced here:
`maximum-scale=1` disabled pinch zoom (WCAG 1.4.4); nine form inputs had no `<label>`,
only placeholders; no skip link; focus rings removed in places.

### 4.6 Rebalancing the portfolio

The portfolio was eleven website builds, which framed someone whose headline says
"IT, SEO and AI automation" as a web developer who also does SEO. The proof contradicted
the positioning.

Fixed by promoting two AI systems into the featured stack (Hermes, and the Quotation vs
PO validation layer, which had been one sentence buried inside another popup), rewriting
Tjikko as digital **and** IT ownership, and linking SEOFlow and WaterStamp as side work.
Copy went from roughly 2,600 to 3,450 words.

### 4.7 Copy humanisation

The skill's phrase-swapper found zero AI patterns, but it only does 1:1 phrase swaps and
is blind to structural tells. A manual scan found **25 lines carrying em-dashes** — the
loudest signal in machine-written prose. Now 8, of which 6 are legitimate label
separators (`Client — via RIAS Strategic`). What was removed was the rhetorical
mid-sentence dash used as a dramatic pause.

**If you write new copy for this site, do not reintroduce them.** Also watch rule-of-three
lists and "X, not Y" antithesis; both were already over-used here.

---

## 5. Content rules (non-negotiable)

From the blocklist in `Docs\Dyrn_Verified_Facts_Memory.md`. Re-read that file before
writing any new claim.

- **busabunga.com** — cite speed-to-rank ("#1 within about a month of launch"). Never the
  raw percentages (+1,500% clicks / +36,800% impressions) or raw click counts; the base
  was tiny and the numbers collapse under questioning.
- **tjikkofoam.com** — use ~40% organic growth / ~25% more leads. Never the raw GSC
  figures, which are modest in absolute terms.
- **RIAS Strategic** is a virtual assistant agency whose freelance talent pool he belongs
  to. **Never** his own agency.
- **Meta Ads: superseded on 1 Nov 2026.** The Master Portfolio 2026
  (`D:\CV\Portfoliodyrn\MasterPortfolio\`, Oct 2026) and the Oct 2026 resume record
  hands-on Meta Ads at Tjikko and the anonymised B2B corporate-gifting Meta Ads + CRM case.
  Those documents are newer than the Verified Facts Memory and win where they differ.
  Keep the client in that case anonymised. Lingga Florist Google Ads figures come from the
  same portfolio.
- **No marketplace sales results.** Shopee/Tokopedia: built and managed the listings, and
  is leading the current reactivation. Not results.
- **No hours-saved figures.** They conflict across old CVs.
- **AquaFoam** — the Docs say *ask before using anything AquaFoam*. It is absent from the
  site for that reason, not by oversight.
- **No testimonials** until real, approved quotes exist.
- **No website count on the site.** The portfolio says 10; with Jakarta Law Firm it is 11. Count is not used.
- **Jakarta, not Bekasi.** Older CVs get this wrong.
- **Never mention the hybrid/remote preference.** That is an offer-stage conversation.

---

## 6. Open items

| # | Item | Notes |
|---|---|---|
| 1 | **CV PDF** | Withheld on purpose. `master resume\Dyrn_Zefanya_Resume_Digital_Specialist.pdf` (24 Jun 2026) predates the Verified Facts Memory and contains "Bekasi", the AquaFoam +20% sales claim, Google/Meta Ads execution at Tjikko, and hours-saved figures — all blocklisted. Regenerate from Docs, drop it at `cv/Dyrn_Zefanya_CV.pdf`, remove `cv/` from `.gitignore`, and switch the three "Request my CV" buttons back to `href="cv/Dyrn_Zefanya_CV.pdf" download`. |
| 2 | **No IT case study** | Wazuh across 50+ devices with ~30% less downtime is only a bullet inside the Tjikko popup. Someone hiring for an IT role gets nothing from the portfolio. Needs its own card, ideally with a topology diagram or dashboard screenshot. |
| 3 | **IEEE publication is buried** | Sits at the bottom of the resume block. It is a genuine differentiator in the Indonesian market. |
| 4 | **No process / "how I work" section** | Freelance clients want to know this before they make contact. |
| 5 | **Third-party presence** | AI search engines cite Wikipedia, Reddit and review sites far more than personal domains. This is the biggest remaining lever for AI visibility and none of it lives on this page. |
| 6 | **OG image is generated, not designed** | Functional 1200×630 card. A properly designed one would do better. |

---

## 7. Constraints and gotchas

Things that cost time to discover. Read before debugging.

### The whole page goes blank if one image 404s

`js/app.js` hides all content until `imagesLoaded` fires its `done` event. That event only
fires when **every** image loads successfully. A single 404 means `done` never fires and
the page stays blank forever, with no console error. If the site renders as an empty dark
screen, check for a broken image path first.

### robots.txt and llms.txt cannot work from this repo

Both are **root-only**. Crawlers read `https://dyrnzefanya.github.io/robots.txt`, never
`.../personal-site/robots.txt`. That path belongs to the separate `dyrnzefanya.github.io`
repo. The `llms.txt` here is linked from the footer and some agents will follow it, but it
is not in the canonical location. The fix is to add `robots.txt` to the root repo (config
is in `README.md`) or move the site to the root / a custom domain.

### The four absolute URLs

`canonical`, `og:url`, `og:image` and the JSON-LD `url` all hard-code the sub-path. Every
other path in the project is relative. If the site moves, those four lines are the entire
change.

### Stack cards are absolutely positioned siblings

`.portfolio-stack__inner` **must keep `isolation: isolate`**. Without it, a `z-index` on a
card's caption escapes its own card and paints over every card that slides in afterwards —
the first project's title ends up stuck on screen for the whole stack.

### Popups only scroll because of the overflow:clip override

`main.css` gives `.popup` `overflow:hidden` plus `overscroll-behavior:contain`. Together
they swallow the mouse wheel: the card becomes a scroll container that cannot scroll and
refuses to pass the wheel to `.mfp-container`, so popups only scrolled with the pointer in
the margin. `custom.css` overrides it with `overflow:clip` and moves `contain` to the
container. **Do not remove that block.**

### Hermes images are designed, not screenshots

`img/work/hermes.jpg` (architecture diagram) and `hermes-seo-report.jpg` (audit card) were
rendered from HTML with headless Chrome at 2x, replacing raw Discord screenshots (Nitro
banner, server avatars, game ads). Rebuild them the same way rather than going back to a
screenshot.

### The popup cover image needs its height cap

The case-study popup scrolls fine, but with a full-height cover image the opening view is
all photo and nothing else, which reads as an image-only lightbox. `custom.css` caps it at
`min(58vh, 620px)` so the title and the first rows of data land in view. Keep the cap if
you swap the artwork.

### `loading="lazy"` does nothing for the popup images

They live inside `display: none` containers and Chrome loads lazy images it cannot
position. Roughly 1.7 MB of project imagery still loads up front. Genuinely deferring it
means swapping `src` in JS on popup open. WebP would help more; no encoder was available
on this machine, so the mockups are JPEG at 1600 px.

### The contact form is wired by hand, not by Formspree's SDK
**The honeypot must be `display:none`, not visually-hidden.** This bit us once: the
`_gotcha` field was hidden with the `.visually-hidden` class, which keeps an element
laid out and reachable so screen readers can still read it. Browser autofill and
password managers duly filled it, and Formspree rejected every submission with
*"Honeypot field _gotcha is not empty"*. A honeypot is a bot trap, not content — it
should be hidden from everything. The `display:none` is inline rather than in a class
so it survives the stylesheet failing to load, and `js/custom.js` also blanks the field
on submit in case a password manager ignores it anyway.


The template ships its own jQuery submit handler pointed at `mail.php`, and it only
implements `.done()` — a failed request did nothing visible, so a visitor would believe
a message had been sent when it had not. `js/custom.js` removes that handler
(`$form.off("submit")` from a *later* `jQuery(function)`, so it runs after app.js has
bound) and replaces it with a fetch.

Formspree's `@formspree/ajax` CDN bundle was not used: the template already has a styled
success panel, and the site otherwise loads no third-party JavaScript. The `Accept:
application/json` header is what stops Formspree replying with a redirect to its own
thank-you page.

The `action` attribute is the no-JavaScript fallback. Keep it pointing at the real
endpoint even though the fetch normally handles submission.

### Heading tags are chosen by rank, not by size

Fixed on 5 Aug 2026. The template picked tags by how big it wanted the text; the
document now runs h1 → h2 → h3 → h4 with no skips, and `custom.css` pins the sizes
so nothing moved. **If you add a heading, pick the tag by its place in the outline
and pin the size in `custom.css` if it needs to look different.** Do not reach for
h5/h6 to make text smaller — there are none left on the page.

### Em-dashes in the generator are escape sequences

`tools/gen_projects.py` stores them as the six characters `\u2014`, not the character. A
find-and-replace using the literal character silently matches nothing. This wasted a cycle
once: the edit appeared to work on `index.html`, then regenerating put every dash back.

### Hero portrait legibility was measured, not eyeballed

The browser in the working session could not produce screenshots, so white-text contrast
over the photo was computed by sampling the JPEG and applying the CSS filter maths.
Colour at `brightness(.72)` scored **2.0:1** against the brightest pixels — below the 3:1
WCAG minimum for large text. Monochrome at `brightness(.55) contrast(1.15)` scores
**3.3:1** worst-pixel, 10.4:1 average, and matches the site's desaturated imagery. If you
change the photo or the filter, re-check this rather than trusting it.

The hero was finally seen on 5 Aug 2026 once the browser recovered, and the maths held:
the headline stays legible where it crosses the portrait. Seeing it also caught something
no measurement could — a leftover decorative magnolia sitting on his shoulder, since
removed. **It has still only been viewed at one width (1707px).** Narrow and mid widths
deserve human eyes.

### Pushing has been slow

Pushes to this repo have stalled for minutes at a time and been reported as hung when they
had actually succeeded. **Always `git fetch` before concluding a push failed** — a stale
`origin/main` ref caused a false report once. `http.version HTTP/1.1` and a large
`http.postBuffer` are already set locally.

---

## 8. Making changes

### Project content

Do **not** hand-edit the portfolio markup. Edit the `PROJECTS` list in
`tools/gen_projects.py` and run:

```bash
python tools/gen_projects.py
```

It rewrites the featured stack, the tile grid and all 12 popups in place, and is
idempotent — running it twice produces the same file. Hand edits to that region get
overwritten on the next run.

Adding a featured project also needs a background image rule (`.portfolio-item-5` …
`-10` in `custom.css`, matched to the featured order) and, ideally, an entry in the
JSON-LD `ItemList` so the structured data matches what the page shows.

### Services

The six service cards and their detail popups (`#service-<key>`) are generated too,
from the `SERVICES` list in `tools/gen_projects.py`. Each popup has Best for /
Platforms / You get / Evidence, then What I do, How I work, Proof on this page and
Tools. **Proof lines must point to a project visible on the page.** Service popups
carry the `Project Popup` comment markers so the same splice replaces them.
"Discuss a project" closes the popup via `.popup-to-contact` in `js/custom.js`.

### Process section ("How I work on a project")

Generated from `STEPS` and `BOARD` in `tools/gen_projects.py` and spliced between
Services and Resume (`#process`). Eight steps, from discovery call to aftercare; each
step names the Trello list (`board` index) its card sits in, and `js/custom.js` moves
one card across the mini board as the visitor clicks. Without JS all panels show as a
list. Payment terms and revision counts are deliberately left to the proposal; add
numbers only once Dyrn decides them. Not in the top menu yet: a 7th item would crowd
the bottom bar on phones.

### Popup close button

Pinned to the viewport as a light "Close" pill (`custom.css`, "always visible"). It
needs `.mfp-ready .mfp-content { transform: none }`, otherwise `position: fixed` is
trapped by the fade-in transform and the button scrolls away with the content.

### Styling

All site-specific CSS lives in `css/custom.css`. `main.css` and `plugins.css` are template
files, kept unmodified apart from the icon subsetting, so the template stays updatable.
`custom.css` loads last and wins.

### Behaviour

`js/custom.js` holds site-specific JS. Currently one thing: it stops clicks on
"Visit live site" from bubbling to the card, which would otherwise open the case study
*and* follow the link. Both paths are worth re-testing if you touch it — clicking the pill
must not open the popup, and clicking anywhere else on the card must.

### Verification without a browser

The browser tooling was unreliable throughout. These checks catch most breakage:

```bash
# every local asset referenced by the page exists
# every in-page anchor resolves
# every popup trigger has a target
# JSON-LD parses
# CSS braces balance
python - <<'EOF'
import io, os, re, json
s = io.open("index.html", encoding="utf-8").read()
refs = set(re.findall(r'(?:src|href)="(?!https?:|mailto:|tel:|#)([^"]+)"', s))
print("missing assets:", [r for r in sorted(refs) if not os.path.exists(r.split('?')[0])] or "none")
ids = set(re.findall(r'id="([^"]+)"', s))
anchors = set(re.findall(r'href="#([a-zA-Z][\w-]*)"', s))
print("broken anchors:", sorted(a for a in anchors if a not in ids) or "none")
mfp = set(re.findall(r'data-mfp-src="#([^"]+)"', s))
print("popup wiring  :", "ok" if mfp <= ids else sorted(mfp - ids))
json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S).group(1))
print("JSON-LD       : valid")
c = io.open("css/custom.css", encoding="utf-8").read()
print("custom.css    :", "balanced" if c.count("{") == c.count("}") else "UNBALANCED")
EOF
```

Then serve it and look at it properly:

```bash
python -m http.server 8877
```

---

## 9. Quick reference

| Need | Go to |
|---|---|
| Change a project's copy | `tools/gen_projects.py` → `PROJECTS`, then re-run it |
| Change any styling | `css/custom.css` |
| Change site behaviour | `js/custom.js` |
| Check a factual claim | `D:\CV\Docs\Dyrn_Verified_Facts_Memory.md` |
| Find richer project detail | `D:\CV\SecondBrain\03-Projects\` |
| Source mockups and screenshots | `D:\CV\Portfoliodyrn\` |
| Deploy steps, asset inventory | `README.md` |
| Original content plan | `D:\CV\Personal-HTML\CONTENT-MAP.md` |
