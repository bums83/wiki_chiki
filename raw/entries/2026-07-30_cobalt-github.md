---
id: github-imputnet-cobalt-2026-07-30
date: 2026-07-30
source_type: url
source_url: https://github.com/imputnet/cobalt
title: imputnet/cobalt GitHub repository
domain: tools
tags: [tools, video, self-hosted, open-source, docker, api-platform]
---

# imputnet/cobalt GitHub repository

Canonical source: https://github.com/imputnet/cobalt

Observed repository state on 2026-07-30:

- Repository: `imputnet/cobalt`.
- Git HEAD inspected: `a636575b09de1fc55d9b8cd98cac88f5f2f16b42` on `main` (commit date 2026-04-06).
- Monorepo: `api/` (Express/Node processing API), `web/` (SvelteKit/Vite static frontend), `packages/` and Docker/docs.
- API package version: `11.7.1`; web package version: `11.7`.
- Main/API code: AGPL-3.0. Frontend code: CC-BY-NC-SA-4.0; cobalt branding/mascots are explicitly copyrighted and excluded from that frontend license.

## What the source says

Cobalt is a media downloader for links to free, publicly accessible content. The repository states that Cobalt does not persistently cache media and works as a proxy/tunnel layer. It says responsibility for downloaded, used and distributed content remains with the end user; source-platform terms and copyright law still apply.

The checked `api/README.md` lists 21 source services: Bilibili, Bluesky, Dailymotion, Instagram, Facebook, Loom, Newgrounds, OK.ru, Pinterest, Reddit, RuTube, Snapchat, SoundCloud, Streamable, TikTok, Tumblr, Twitch Clips, X/Twitter, Vimeo, VK and YouTube. Capabilities vary by service. The table is version-specific and declares itself expandable rather than a stable guarantee.

## Architecture

The API accepts a source URL plus requested output options. Schema validation restricts options such as audio/video mode, quality, container, codec, subtitle/dub language, metadata and local-processing preference. `POST /` returns one structured status:

- `redirect` — direct service URL;
- `tunnel` — Cobalt proxies/remuxes/transcodes;
- `local-processing` — browser/client receives tunnels and performs merge/mute/audio/GIF/remux work locally;
- `picker` — multiple media objects need a user choice;
- `error` — machine-readable failure code.

For tunnels, the API creates expiring links with ID, expiry, signature, secret and IV. Stream metadata is encrypted before storage. The default store is in-memory; Redis is used when configured, and is required for multi-instance operation so sub-instances share tunnel state. This is short-lived processing state, not a persistent media library.

The static web client is SvelteKit/Vite and has browser-side Libav workers for remux/encoding. The API uses Express, strict JSON headers/body schema, rate-limit middleware, optional API keys, optional Turnstile-to-JWT sessions, service allowlists and `ffmpeg-static` for server-side media work.

## Hosting and security facts

There is no public hosted API meant for third-party projects. The source tells API consumers to operate their own instance or obtain explicit owner permission. The provided Docker Compose sample runs `ghcr.io/imputnet/cobalt:11` on port 9000; `API_URL` is required because tunnel URLs are built from it.

Security matters for a public instance:

- the documented defaults include `API_LISTEN_ADDRESS=0.0.0.0` and `CORS_WILDCARD=1`;
- request, session and tunnel rate limits exist, but are not an access-control policy;
- public instances are advised to put Cobalt behind a reverse proxy and configure Turnstile, API keys, or both;
- `API_AUTH_REQUIRED=1` makes authentication mandatory; key records can restrict request limits, IP/CIDR ranges, user agents and allowed services;
- cookies can be mounted only for services where authentication is required to view otherwise public content. They are credentials and must not be committed, logged or exposed.

The frontend supports optional Plausible configuration (`WEB_PLAUSIBLE_HOST`). Therefore the repository's product claim about a tracker-free public site should not be generalized to every self-hosted build: analytics behavior depends on the deployment configuration.

## Version/documentation caveat

The inspected package metadata reports API `11.7.1` and web `11.7`, while `docs/protect-an-instance.md` says its Turnstile walkthrough is reliably compatible with the latest official version 10. This is a documentation-version mismatch in the source tree. Operators should validate protection settings against their exact image version before exposing an instance.

## Local verification

No end-to-end service download test was run: the repository's API test suite installs dependencies, starts a local server and sends live requests to external media services, which makes its outcome network/service-rate-limit dependent. Instead, Node syntax checks passed for the API entrypoint, API router, request schema and stream manager; `api/package.json` and `web/package.json` also parsed successfully as JSON.

## Wiki integration notes

Nearest Wiki Chiki neighbors:

- [[Coolify]] — deployment/control plane for a private Docker service; Cobalt still needs explicit reverse-proxy, access-control and secret handling.
- [[OpenScreen]] — records and edits one's own screen/demo material; Cobalt saves an existing public media source. They occupy different parts of a media workflow.
- [[Video Summary]] — starts from text/PDF/URL and makes an explanatory MP4. Cobalt can supply a local public-media artifact to a separate transcription/extraction stage, but Video Summary does not directly accept Cobalt's downloaded video as input.
