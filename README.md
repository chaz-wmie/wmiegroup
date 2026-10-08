# WMIE Group Website

WMIE — Wholesale Management & Infrastructure Expansion. Brand: We Make It Easy.
Live domain: https://wmiegroup.com. Existing hosting: Netlify project `wmie`.

## Source and build

Static multipage HTML with no framework or package dependencies. Edit `content/site.json` for service content and leadership, `scripts/build.mjs` for page composition, and `assets/site.css` for shared styles. Root `index.html`, `robots.txt`, and `sitemap.xml` are source mirrors of the generated deployment artifacts. When updating them, run the build and copy the generated root files back to these mirrors.

Requires Node for the build and Python 3 standard library for validation:

```sh
npm test
```

The build generates twelve pages (eleven indexable routes plus a noindex acknowledgment page), a 404 page, sitemap/robots, and an explicit asset allowlist in `dist/`. Original photographs, historical files, source data, and documentation are excluded from deployment. No installed packages are needed.

## Contact delivery

Existing co-owner email and LinkedIn links remain available. The contact page includes a static Netlify form with accessible labels, browser validation and a honeypot. `assets/contact.js` reveals it only when Netlify has removed the registration attribute during form processing. If form detection is disabled, direct email remains the visible inquiry path. This avoids publishing an unregistered submission flow.

To activate the form, enable Forms detection in the existing Netlify project and redeploy, then verify the form is registered and set approved email notifications. A detected form collects submissions in Netlify; registration alone does not prove mailbox delivery. Verify notifications with a consented test inquiry. No credentials are in the repository.

## Publishing

`netlify.toml` specifies `npm run build` and `dist`, with apex/index redirects. Keep the existing Netlify project and DNS. If the project is linked to GitHub main, merging to main starts its configured deploy; otherwise, the Netlify project must publish `dist` through its existing deployment flow.

See [audit and growth strategy](docs/SEO-AUDIT.md) for research, keyword mapping, test evidence, and outstanding business information. Main publishing was explicitly authorized by the owner on October 8, 2026.
