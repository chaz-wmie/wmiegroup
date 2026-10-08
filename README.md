# WMIE Website

Official website for WMIE — Wholesale Management & Infrastructure Expansion.
Live domain: https://wmiegroup.com. Existing hosting: Netlify (README project name: `wmie`).

## Build and validate

Requires Node and Python 3. No package installation required.

```sh
npm test
```

`npm run build` produces `dist/` using an explicit public-file allowlist. `npm run check` validates that artifact, including ownership, links, metadata, schema and sitemap. For a local preview: `python3 -m http.server 8000 --directory dist`.

`netlify.toml` proposes the build command and publish directory; verify the existing Netlify dashboard before release. Do not publish the repository root. Original/historical assets remain source-only and are excluded from the deployment build. Team images are optimized derivatives of existing photographs. Social preview uses the original WMIE logo.

See [ownership and SEO audit](docs/SEO-AUDIT.md) for findings, keyword strategy, verification limits, missing business information, and release requirements. Main/production publishing requires the owner's explicit approval.
