# dyrn-site

Personal site for Dyrn Zefanya — freelance portfolio and job-application front door in one page.

**Live:** https://dyrnzefanya.github.io/personal-site/

- **Base template:** Blayden (ThemeForest), demo 2
- **Content source of truth:** `D:\CV\Docs\Dyrn_Verified_Facts_Memory.md`
- **Content plan:** `D:\CV\Personal-HTML\CONTENT-MAP.md`
- **Target hosting:** GitHub Pages (static, no server-side code)
- **Language:** English only

---

## Before this can go live

| # | Item | Status |
|---|---|---|
| 1 | **CV PDF** at `cv/Dyrn_Zefanya_CV.pdf` | **Deliberately not published.** See the warning below. The three buttons now read "Request my CV" and jump to the contact form, so nothing 404s. Once a clean PDF exists, drop it in `cv/`, remove `cv/` from `.gitignore`, and change the three `href="#contact"` buttons back to `href="cv/Dyrn_Zefanya_CV.pdf" download` with the caption "Download CV". |
| 2 | **Contact form endpoint** | **Blocker.** `index.html` still has `value="YOUR_FORM_ID"`. Replace with a Web3Forms access key or swap the `action` for a Formspree endpoint. GitHub Pages cannot run the template's PHP mailer, which has been removed. |
| 3 | **Portrait photo** | The hero currently uses the template's own decorative cutouts (`img/demo/`) as a placeholder — the composition the template ships with. `pas-foto-dyrn.jpg` was tried and is unusable: red ID-photo background, and it covered the headline. A portrait-orientation shot on a neutral or dark background would replace the `intro-bg-01` block. |
| 4 | **OG image** | Done. `img/og-image.jpg` is a generated 1200×630 card: name, role, location and years, with a dimmed busabunga screenshot on the right. Regenerate it if the headline copy changes. |
| 5 | **Favicon** | Done. The template's cat is gone. `icon.svg` is a "DZ" monogram that inverts with the system colour scheme; the PNGs and a 3-size `favicon.ico` were generated from it, and the web manifest now carries your name and relative icon paths (the template's were absolute, which breaks under a project sub-path). |

### ⚠️ Why the CV is not published

`Dyrn_Zefanya_Resume_Digital_Specialist.pdf` (24 Jun 2026) predates the Verified Facts
Memory and contains claims that document now blocklists. Someone who reads the site and then
opens the CV will find two different stories — and every one of these is a question you would
have to answer in an interview:

- **"Bekasi, Indonesia"** in the header — blocklist item 12; you live in Jakarta.
- **"an e-commerce launch that added 20% in sales"** and **"Led the AquaFoam product launch"** —
  blocklist item 10, unverified.
- **"ran Google and Meta Ads that lifted engagement about 35%"** at Tjikko — blocklist items 1
  and 2. Tjikko growth is SEO-only; Meta Ads is framework knowledge, never executed.
- **"more than 20 hours of manual work off the team each month"**, "5 to 8 hours each week",
  "15 hours off monthly project turnaround" — blocklist item 9; these figures conflict across
  older CVs and need re-confirmation per use.
- **Google Ads and Meta Ads listed under Marketing Technology skills** — the site deliberately
  omits both from its services for the same reason.

Regenerate it from the Verified Facts Memory, then add it as `cv/Dyrn_Zefanya_CV.pdf`.

## Deploying to GitHub Pages

This is a **project site**, so everything lives under a sub-path:

- Repo: `Dyrnzefanya/personal-site`
- Live: `https://dyrnzefanya.github.io/personal-site/`

That sub-path is baked into four places in `<head>` — `canonical`, `og:url`, `og:image` and the
JSON-LD `url`. Every other path in the project is relative, so nothing else needs touching.
If the site later moves to the root `dyrnzefanya.github.io` repo or a custom domain, those four
lines are the only edit.

```bash
cd D:/CV/dyrn-site
git add -A
git commit -m "Your message"
git push
```

## Layout

```
index.html          single page: home · portfolio · about · services · resume · contact
css/custom.css      all site-specific overrides — main.css is untouched so the
                    template stays updatable
img/work/           project mockups, resized to 1600px and recompressed
                    (9.9 MB of originals → 1.8 MB)
cv/                 CV PDF, linked from three Download buttons
tools/              gen_projects.py — regenerates the whole portfolio section
                    (stack, tile grid and all 11 popups) from one data list
```

To add or edit a project, change the `PROJECTS` list in `tools/gen_projects.py` and run it:

```bash
python tools/gen_projects.py
```

It rewrites the portfolio markup in place. Hand-editing a popup works too, but the next run
of the script will overwrite it.

### Portfolio

Eleven projects, each with a full case-study popup: **Type / Date / Role / Client**, an intro,
a *What I built* scope list, *The challenge*, *How I approached it*, *Result*, and a *Stack*
tag row, plus a live link where one exists.

- **Six featured** in the scrolling stack: busabunga.com, Sekolah Trinitas, Tjikko Foam,
  Hermes, Invera Wedding, Ny Liem Heritage. Stack backgrounds come from `.portfolio-item-5`
  … `-10` in `custom.css`.
- **Five under "Other work"** as a tile grid: Tjikko Foam Global, Soka Chemical, RIAS
  Strategic, The Paw Charm, Lingga Florist.

Popup IDs are `#project-<key>` (e.g. `#project-busabunga`), wired to their triggers via
`data-mfp-src`. To add a project, edit the `PROJECTS` list in the generator script rather than
hand-writing ~120 lines of markup per popup.

**Card treatment.** The template put the project title straight onto the artwork with no
scrim — fine against its flat grey placeholders, unreadable against real screenshots. Each
stack card now carries two layers in `custom.css`: a permanent bottom gradient (`::after`) so
the title is always legible at rest, and a `backdrop-filter` blur plus dim (`::before`) that
fades in on hover, at which point the tagline fades in too. The "Other work" tiles use the
same blur so the two families read as one system. Three details worth keeping if you edit it:

- `@supports not (backdrop-filter)` falls back to a heavier plain dim, so older browsers still
  get readable text rather than none.
- `@media (hover: none)` keeps the tagline visible on touch devices, which never fire hover.
- `main.css` hid the card title entirely below 768px — six unlabelled images on a phone. The
  scrim makes it legible, so `custom.css` shows it again.
- **`.portfolio-stack__inner` must keep `isolation: isolate`.** The stack cards are
  `position: absolute` siblings layered on top of each other, so a `z-index` on the caption
  escapes its own card and paints over every card that slides in afterwards — the first
  project's title ends up stuck on screen for the whole stack. Isolating each card scopes
  that `z-index` locally.

**Popup cover height.** The case-study popup scrolls normally, but the cover image was taller
than the viewport, so opening a project filled the screen with photo and nothing else — it
read as an image-only lightbox and gave no hint there was anything below. `custom.css` caps
the cover at `min(58vh, 620px)` and adds the same gradient scrim, so the title plus the first
rows of project data land in the opening view. Keep the cap if you swap the artwork.

**Live-site buttons.** Every project with a public URL has two ways through to it: a
"Visit live site" pill on the card itself, and the circular button at the bottom of its case
study. On the featured stack the pill fades in with the tagline on hover; on the tiles it is
always visible.

The cards are Magnific Popup triggers, so a plain link inside them would open the case study
*and* follow the href. `js/custom.js` catches `.project-visit` clicks in the capture phase and
stops propagation, which keeps the two actions separate. Both paths are worth re-testing if
you touch that file: clicking the pill must not open the popup, and clicking anywhere else on
the card must.

**Hermes has no live button** — it is a self-hosted internal system with no public URL. That is
correct, not an oversight.

**Two projects were deliberately left out:**

- **AquaFoam** — the Verified Facts Memory says to *ask before using anything AquaFoam*: the
  role and the sales figure are both unverified. Add it once you have confirmed what you
  actually own there.
- **Agromas Tapioca / Agromas Crackers** — still in development, and there are no mockups for
  either. They are named in a one-line note under the grid instead.

## Content rules baked into this build

These follow the blocklist in the Verified Facts Memory. Re-read that file before editing copy.

- **busabunga.com** — cite speed-to-rank ("#1 within a month of launch"). Never the raw
  percentages (+1,500% clicks / +36,800% impressions) or raw click counts; the base was tiny.
- **tjikkofoam.com** — use ~40% organic growth / ~25% more leads. Never the raw GSC figures.
- **RIAS Strategic** — a freelance talent pool Dyrn belongs to. Never his own agency.
- **No Meta Ads or Google Ads** appear as services. Meta Ads is framework knowledge only;
  Google Ads was one personal project.
- **No testimonials.** The old portfolio's quotes are marked "representational and pending
  formal client approval" — they were deliberately not carried over. Add them only once
  real, approved quotes exist.
- **No website count** in the copy. The Docs flag the RIAS project count as unverified.
- **No hybrid/remote preference** anywhere. That is an offer-stage conversation.

## What was stripped out, and why

The repo went from **21 MB to 5 MB**, and render-blocking CSS from **1054 KB to 539 KB**.
Nothing removed was reachable from this page — verified by re-auditing every asset and CSS
`url()` reference afterwards, and by confirming the icon font still renders.

| Removed | Size | Why it was safe |
|---|---|---|
| `fonts/Fontawesome/` + its CSS section | ~1 MB files, 190 KB CSS | Zero `fa-` classes in the markup, and nothing in the JS injects them |
| Phosphor Bold / Duotone / Fill weights + their CSS | ~1.4 MB files, 338 KB CSS | Only `ph`, `ph-light` and `ph-thin` appear in the markup |
| Phosphor `.ttf` and `.svg` font files | ~5 MB | Legacy fallbacks after `.woff2` in the `@font-face` list; no target browser reaches them. The `src` lists were trimmed to match so nothing dangles |
| `img/demo`, `img/avatars`, `img/marquee`, `img/services`, `img/testimonials`, `img/works`, `img/backgrounds` | ~1.8 MB | Belonged to template sections this build does not use |
| `css/main-demo.css`, `css/plugins-demo.css`, `js/demo/` | ~1 MB | Only used by the template's own sales landing page |
| The commented-out background-video block | — | Its `video/*.mp4` references pointed at files that were never shipped |

Note that the local `python -m http.server` does not gzip. GitHub Pages does, so the real CSS
transfer will be roughly a tenth of the figure above.

A second pass took `plugins.css` from **1054 KB to 318 KB**:

| Removed | Was | Now | Why it was safe |
|---|---|---|---|
| Unused Phosphor glyph rules | 548 KB | 4 KB | The page uses 11 icons; the font shipped ~5,800 rules per weight. The subsetter reads the icon list out of `index.html` rather than hard-coding it |
| Fontawesome section | 190 KB | — | Zero `fa-` classes anywhere |
| Vegas plugin CSS | 20 KB | — | No `.vegas` elements, no init call |

The icon subsetting is scripted, not hand-edited. If you add an icon to the markup, its rule
will be missing — re-run the subsetter against a fresh `plugins.css` from the template, or add
the one `content:` rule by hand.

Still there and worth knowing about:

- **`css/main.css` contains dummyimage.com URLs** for template classes this build does not use.
  They never fire a request because no element carries those classes. The one that *is* used,
  `.main-image-2`, is overridden in `custom.css`.
- **Bootstrap's grid is 254 KB of the remaining CSS.** It is used throughout, so trimming it
  needs a real purge tool rather than a regex.
- **`loading="lazy"` on the popup cover images buys nothing.** They live inside `display: none`
  containers, and Chrome loads lazy images it cannot position. The attribute is left in place
  because it is correct in principle, but roughly 1.7 MB of project imagery still loads up
  front. Genuinely deferring it would mean swapping `src` in JS when a popup opens. The other
  route is WebP — no encoder was available on this machine, so the mockups are JPEG at 1600 px.
- **`js/libs.min.js` is ~600 KB** — jQuery, GSAP, Swiper, PhotoSwipe and Magnific bundled
  together by the template. Only a rebuild from the Gulp source would slim it down.

## Working on it locally

```bash
cd D:/CV/dyrn-site
python -m http.server 8877
```

Note: the page hides all content until `imagesLoaded` fires its `done` event. If any single
image 404s, `done` never fires and **the entire page stays blank** — a confusing failure mode
worth remembering when adding images.
