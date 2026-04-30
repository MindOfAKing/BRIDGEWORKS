# Codex Session: Bing Webmaster Tools and IndexNow

**Date:** 2026-04-30  
**Status:** Site-repo patch applied  

## Applied Update

Codex found the source repo at:

`C:\Users\ELITEX21012G2\ceefm-astro`

Applied on 2026-04-30:

- Bing verification meta tag added to `src/layouts/BaseLayout.astro`.
- Wikidata entity `Q139592822` added to the CEEFM organisation JSON-LD.
- IndexNow key file created at `public/d9916e6c1f394ddd97bf35b81cfa2e7f.txt`.
- Vite alias added in `astro.config.mjs` for Astro's prerender entry after the local build could not resolve `astro/entrypoints/prerender`.

Build note: `npm.cmd install` completed. `npm.cmd run build` was attempted with Astro telemetry disabled. The first run failed on `astro/entrypoints/prerender`; after the alias fix, the build progressed and then failed on local Windows sandbox error `spawn EPERM` inside Vite's realpath handling. Re-run in the normal developer shell or deployment environment.

## Bing Verification Value

Emmanuel provided the Bing Webmaster Tools verification tag:

```html
<meta name="msvalidate.01" content="BA08FF5FB45EA54364C56B7D914AB85D" />
```

This should be added inside the `<head>` of:

`ceefm-astro/src/layouts/BaseLayout.astro`

## IndexNow Key

Generated key:

```txt
d9916e6c1f394ddd97bf35b81cfa2e7f
```

Create this file in the site repo:

`ceefm-astro/public/d9916e6c1f394ddd97bf35b81cfa2e7f.txt`

File contents:

```txt
d9916e6c1f394ddd97bf35b81cfa2e7f
```

If the current Bing UI requests an IndexNow meta tag, add:

```html
<meta name="indexnow" content="d9916e6c1f394ddd97bf35b81cfa2e7f" />
```

## Manual Bing Steps After Deploy

1. Deploy the site with the Bing verification meta tag.
2. In Bing Webmaster Tools, click verify.
3. Submit sitemap:

```txt
https://ceefm.eu/sitemap-index.xml
```

4. Trigger IndexNow ping for:

```txt
https://ceefm.eu/
https://ceefm.eu/hu/
https://ceefm.eu/contact
https://ceefm.eu/hu/kapcsolat
```

## Previous Blocker

Resolved. The repo path was `C:\Users\ELITEX21012G2\ceefm-astro`.
