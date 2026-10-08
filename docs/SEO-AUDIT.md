# WMIE Group ownership and SEO review

Audit date: October 8, 2026. Base commit: `bd3f56ced54a423693e59b0769cefb414eabf7d2`.
Branch: `update/ownership-seo-2026-10-08`. Production is unchanged. This report describes proposed source changes, not a deployed result.

## Verified business and platform

The live homepage exactly matched `main:index.html` at audit time. WMIE expands to Wholesale Management & Infrastructure Expansion. The existing homepage identifies it as Oklahoma-based strategic support for broadband and infrastructure opportunities, including tribal/corporate relations, sales development/marketing, engineering referrals, commercial insurance/surety bond guidance, and bandwidth partnerships. Target visitors described by the content are organizations pursuing broadband infrastructure, funded initiatives, and regional expansion. The site does not establish an exact service territory, street address, phone, license jurisdictions, or legal entity name. No additional geography or credentials were added.

Live HTTPS response: 200 with `server: Netlify`, `cache-status: Netlify Edge`, and an `x-nf-request-id`. The README identifies Netlify project `wmie`. HTTP and www both resolve to the HTTPS apex homepage. Netlify hosting is confirmed; its dashboard settings, connected repository, production branch, and deployment mechanism have not been inspected. GitHub main has no recorded checks or status contexts. The repository has no framework, package dependencies, prior build/test scripts, backend, form handler, or CI workflow; it is a static HTML site with inline CSS/JavaScript. The search engine's older cached content mentions a form and additional services that are absent from both the current live site and repository; that cached material was not used to expand business claims.

## Ownership changes

- Removed Jayna's visible card, biography, email, and LinkedIn links from current website HTML.
- Todd Segress, Janie, and David each have the exact title **Co-Owner** in the team section and organization schema.
- Preserved the three existing photographs as optimized derivatives, with updated alt text.
- Replaced the mouse-only profile modal with native expandable profiles that work with a keyboard and without JavaScript. Short responsibilities are derived only from the old site; no new credentials or biographies were invented. Older titles and last names for Janie/David are not presented as the new approved identity.
- Original photographs, unused historical assets, and Git history remain in the repository. The deployment build uses an explicit allowlist that excludes those assets, documentation, and internal files. Public source history is not erased.

## Before and after

| Priority / finding | Before | Proposed result |
|---|---|---|
| P0 ownership | Four profiles including Jayna; inconsistent ownership titles | Three consistent co-owner profiles; no Jayna references or assets in `dist` |
| P1 content access | Fixed slide layout, desktop overflow hidden, inactive mobile sections display none | All ten sections in normal document flow, usable without runtime JavaScript |
| P1 navigation | Buttons and click handlers; no link destinations or section URLs | Native section anchors, main/nav/footer landmarks, skip link, visible keyboard focus |
| P1 canonical | Missing; `/index.html` returns a duplicate 200 | Apex canonical plus proposed Netlify `/index.html` 301 |
| P1 sitemap / robots | Both return 404 | Valid single-URL XML sitemap and permissive robots with sitemap reference |
| P2 titles and headings | Brand/tagline title; vague service headings; H1 to H3 jump | Service-focused title/H1, descriptive H2s, one H1, corrected hierarchy |
| P2 structured data | Absent | Organization, co-owner roles, and WebSite JSON-LD; no invented LocalBusiness address or service area |
| P2 conversions | Service discovery/team CTA; contact only through later slide | Direct project email CTA, contextual service/contact links, clearer inquiry instructions |
| P2 social previews | Sparse Twitter metadata; 1536-square logo | Actual 1200×630 JPEG using the original logo, complete title/description/alt metadata |
| P2 page images | 1,071,502 bytes across logo and four people | 90,736 bytes across compact logo and three WebP photos: 91.5% smaller |
| P2 responsive access | Desktop sections risk clipping; mobile menu removed | Wrapping sticky navigation, 1000/620px breakpoints, single-column narrow layouts, no forced hidden content |
| P3 errors / deployment | Default error page; repository root may expose obsolete files | Branded noindex 404; reproducible nine-file deployment allowlist |

Existing HTTPS, the brand palette, source photographs/logo, all five service categories, engineering-referral distinction, and remaining contact/social links were preserved. Scrollable sections replace the slide presentation because the old interaction materially harms content access. No new thin service/location pages were created.

## Keyword strategy and evidence

Research checked current search results on October 8, 2026. This is a relevance/search-intent strategy, not a search-volume, difficulty, or competitor-ranking measurement. There is no Search Console, paid keyword database, or conversion data available. Competitors establish related vocabulary; they do not establish WMIE's capabilities.

| Current destination | Recommended terms | Intent / constraint |
|---|---|---|
| Homepage | WMIE Group; broadband infrastructure strategic support; Oklahoma broadband consulting support | Brand and business discovery; Oklahoma means existing base, not confirmed statewide coverage |
| `#tribal-corporate-relations` | tribal broadband partnership support; tribal relations for broadband projects; infrastructure stakeholder engagement | Organizations seeking communication/partner support; avoid claiming government authority or tribal affiliation |
| `#insurance-surety-bonds` | broadband project insurance guidance; infrastructure surety bond requirements; BEAD insurance and bonding readiness | Commercial research; any jurisdiction/program-specific material needs licensed review and current primary sourcing |
| `#sales-marketing` | broadband sales development support; infrastructure proposal positioning; telecom partner marketing | B2B growth support, not household internet service |
| `#engineering-readiness` | broadband engineering referrals; infrastructure bid readiness support; technical planning partner coordination | Referral/coordination only, not direct engineering design |
| `#bandwidth-partnerships` | bandwidth sales partnerships; broadband provider partnership development | B2B partner search, not internet plan shopping |
| Team / contact | WMIE co-owners; contact WMIE Group | Branded trust and inquiry |

Fragment destinations are sections of one page, not independently indexable service pages. Later standalone pages should be created only after scope, expertise, evidence, and demand are confirmed. The proposed homepage uses natural service vocabulary, not repetitions of every keyword variant.

Potential FAQ topics: “Does WMIE perform engineering work?”, “Who handles bandwidth delivery and operations?”, and “What project details should I include in an inquiry?” These can be answered from current scope. Questions about BEAD bonding thresholds, eligible costs, or grant deadlines require up-to-date program sources and qualified review before publication.

Comparable research: TICOM describes tribal broadband engineering/technical consulting; Reagan Smith/ESPS describe tribal/municipal/private-sector broadband project support; JW Surety's BEAD page targets program-specific bonding intent. WMIE's opportunity is to explain its narrower strategic/relationship/referral scope clearly, with real project evidence. Do not copy competitors' direct engineering, grant-writing, permitting, funding-success, or operational claims.

Sources:
- Current business: https://wmiegroup.com/ and repository base commit above (HTTP/code comparison)
- https://www.turtleislandcom.com/services/
- https://rsenergysolutions.squarespace.com/broadband
- https://www.jwsuretybonds.com/contractor-bonds/bead-bond
- https://oklahoma.gov/broadband.html (program context, not WMIE affiliation)

## Performance and verification

`npm test` builds the allowlisted artifact and checks ownership, schema JSON, sitemap XML, metadata, 39 links, four image references/dimensions, heading hierarchy, fragment targets, and absence of runtime event handlers/hidden sections. `git diff --check` passes. There was no existing lint/type-check/test suite or typed language to run. The new build requires Node; validation requires Python 3 standard library. Neither requires installed package dependencies. Build output totals 145,186 bytes including the social image and error page.

Optimizations: zero runtime JavaScript, no framework bundle, lazy decoding/loading for team images, image dimensions, WebP, small header logo, reduced expensive blur effects, and moderate asset caching without immutable names. Original static HTML already exposed text to crawlers; the old slide UI is an access/visibility problem, not proof that Google could not parse its HTML. The new site serves all text directly in HTML and does not need prerendering.

Rendered local-preview verification could not complete: the cloud browser rejects localhost and the Chrome-for-Testing download returned an invalid archive. Responsive CSS and content were inspected statically, but no rendered mobile/device audit, Lighthouse score, axe audit, or LCP/INP/CLS measurement is claimed. Field Core Web Vitals require real-user data. JSON/XML parse checks are not a Google rich-result eligibility guarantee. External LinkedIn and mailbox delivery were not verified; internal file/fragment references are valid.

## Local SEO and information needed

Keep only the verified Oklahoma-based wording until exact geographic coverage is supplied. Do not create city pages or invent NAP. Organization schema is appropriate at present; a LocalBusiness classification/address would require verification.

Please confirm official business/entity name, public phone, physical versus service-area operating model, service territory, and whether the existing @wmie.org mailboxes and LinkedIn profiles remain current. Optional: approved full names, current responsibilities/credentials, and bios for Janie/David. Needed for meaningful future SEO: real project/case-study evidence, permitted partner references, and Search Console access/data.

Recommend a Google Business Profile eligibility check based on actual in-person customer operations. If eligible, verify real business name/category, public contact information, and service area; keep an unstaffed/private address hidden where appropriate. Do not create duplicate profiles or claim multiple offices. No profile changes were made.

## Hosting and Lovable

Keep Netlify for this change: static HTML is sufficient and avoids a framework migration. Proposed `netlify.toml` specifies `npm run build` and `dist`, keeping legacy source assets out of production. This file takes effect only when deployed. Verify dashboard overrides/base directory and production branch before publishing. No hosting disconnection, DNS edits, main pushes, or production deployment were performed.

Lovable's current FAQ states that existing Git repositories cannot directly seed/connect a new project; Lovable creates a new repository. A recreation from the website/design is possible, but this would be a separate migration, requiring preservation of content, paths, contact behavior, ownership, metadata, and redirects. New Lovable projects use TanStack Start according to current documentation. Recommendation: consider it later if regular visual editing or application features justify the rebuild, not as a prerequisite for SEO.

Sources: https://docs.lovable.dev/introduction/faq and https://docs.lovable.dev/tips-tricks/external-deployment-hosting

## Readiness and release gate

Source/build checks pass; production approval has not been requested or granted. The branch is ready for code review, with rendered/device testing and Netlify configuration confirmation pending before a production release.

Before release: review ownership/content, run `npm test`, inspect a non-production preview at 375/390/768/1440px with keyboard and JavaScript disabled, validate contact links/profiles and the social image, run performance/accessibility audits, and verify Netlify's active build settings. On explicit approval, merge and release through the existing process; then verify canonical/index redirects, robots/sitemap HTTP statuses, no Jayna asset exposure, and 404 status in production. Removing a legacy file does not erase externally cached copies.

After release: submit sitemap in Search Console and inspect indexing. Establish impressions/clicks, nonbrand queries, inquiry conversions, and field performance baselines. Over 30–90 days, prioritize proven service demand, approved case studies, and partner/community links. Publish separate useful service pages only with substantial verified content. Evaluate qualified inquiries and query relevance rather than promising ranking or traffic increases.
