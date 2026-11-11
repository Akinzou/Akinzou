<a href="https://yelon.dev">
  <img src="./assets/header.svg" alt="Wiktor Jeleń, Backend &amp; Platform Engineer, Cracow, Poland. Open to new roles: root@yelon.dev" width="100%">
</a>

<p align="center">
  <a href="https://yelon.dev"><img src="https://img.shields.io/badge/yelon.dev-07070d?style=for-the-badge&logo=googlechrome&logoColor=00f0ff" alt="yelon.dev"></a>
  <a href="https://yelon.dev/Wiktor_Jelen_CV.pdf"><img src="https://img.shields.io/badge/CV-PDF-07070d?style=for-the-badge&logo=readdotcv&logoColor=00ff9d&labelColor=07070d&color=1c1c30" alt="CV (PDF)"></a>
  <a href="https://www.linkedin.com/in/yelon/"><img src="https://img.shields.io/badge/LinkedIn-yelon-07070d?style=for-the-badge&labelColor=07070d&color=1c1c30" alt="LinkedIn"></a>
  <a href="mailto:root@yelon.dev"><img src="https://img.shields.io/badge/root@yelon.dev-07070d?style=for-the-badge&logo=minutemailer&logoColor=ff00a0" alt="Email root@yelon.dev"></a>
</p>

I'm **Wiktor Jeleń**, a backend and platform engineer based in Cracow, Poland. I build multi-tenant production systems, infrastructure and security-critical backends, and I wrote [PythonMetaTrader5](https://github.com/Akinzou/MetaTrader5-Python), an open-source library with over 43,000 PyPI downloads.

I start from architecture, invariants and failure modes, then write the code and prove it with tests and CI. I work AI-native every day (Claude Code, OpenAI Codex, Antigravity), with the test suite and the pipeline deciding what ships.

Most of my commercial code lives in private client repositories, so the work is described below instead of linked.

> **Open to new roles:** backend, platform or automation engineering, in Cracow or remote. Write to [root@yelon.dev](mailto:root@yelon.dev).

## Production work

### B2B e-commerce automation
<sub>Backend & Automation Engineer · contract, under NDA · 09–11.2026</sub>

Four systems, all in production:
- Supplier integration platform, extended from 59 to 109 suppliers (73,000+ products). Playwright scrapers and API clients for suppliers with B2B panels; for the rest, an LLM reads email replies, XLSX, PDF or photos (OCR) and the team approves the result. A catalogue drop of more than 20% blocks publication.
- RFQ automation service built from scratch in 8 days: LLM extraction into a strict JSON schema, supplier matching, offer comparison per unit. Clean Architecture and TDD, OWASP ASVS L2 (23 of 23 scenarios passed), Semgrep and secret scanning on every merge.
- Marketing content generator with a Shoper integration: posts planned from the live catalogue, images and video from templates, copy in 15 languages.
- Takeover of a legacy PHP / Laravel PIM: closed a critical auth vulnerability, rotated keys, fixed margin calculation, set up continuous delivery with automatic rollback.

### KONIK
<sub>Lead Backend Developer · KonikSystems · 03–08.2026</sub>

Multi-tenant automation platform. TypeScript / NestJS backend, Temporal.io orchestration, PostgreSQL row-level security with isolation-leak tests in CI, a multi-provider LLM layer (Claude, OpenAI, Gemini, MCP) with an evaluation harness, and integrations with Stripe, Google Ads, Meta and n8n.

### Anatomy Project
<sub>Backend Engineer · Randlab Software · 09.2025–02.2026</sub>

NestJS backend for 450+ concurrent users at the Medical University of Silesia: LDAP / Active Directory authentication, JWT, an OpenAPI contract, OWASP Top 10 hardening.

### Earlier
R&D systems engineer with the GEEETECH team in Shenzhen (Klipper firmware, hardware redesign), sales systems at Polsat Plus Group, IoT monitoring on ThingsBoard with C++ and AWS. Full timeline on [yelon.dev](https://yelon.dev).

## Open source

| Project | What it does | |
| --- | --- | --- |
| [**PythonMetaTrader5**](https://github.com/Akinzou/MetaTrader5-Python) | Python layer over the MetaTrader 5 API for algorithmic trading: order normalization, full retcode handling, safeguards for live accounts. | [![Downloads](https://static.pepy.tech/badge/pythonmetatrader5)](https://pepy.tech/project/pythonmetatrader5) [![PyPI](https://img.shields.io/pypi/v/PythonMetaTrader5?color=00f0ff&labelColor=07070d)](https://pypi.org/project/PythonMetaTrader5/) |
| [**TradeLockerBot**](https://github.com/Akinzou/TradeLockerBot) | FastAPI service that turns TradingView alerts into TradeLocker orders. The webhook path is a random secret printed once at startup. Docker image built by GitHub Actions. | ![FastAPI, Docker](https://img.shields.io/badge/FastAPI-Docker-07070d?labelColor=07070d&color=bf00ff) |
| [**CapitalCom**](https://github.com/Akinzou/CapitalCom) | Python client for the Capital.com API. | ![Python API client](https://img.shields.io/badge/Python-API-07070d?labelColor=07070d&color=00ff9d) |
| [**TradingViewBacktester**](https://github.com/Akinzou/TradingViewBacktester) | Backtester for TradingView strategies in Python. | ![Python backtesting](https://img.shields.io/badge/Python-backtesting-07070d?labelColor=07070d&color=ff00a0) |

## Stack

<img src="./assets/stack.svg" alt="Stack. Backend and data: TypeScript, Node.js, NestJS, Python, FastAPI, Django / DRF, PHP / Laravel, PostgreSQL, MySQL, MongoDB, Redis, Temporal.io. Platform and infra: Linux, Docker, Kubernetes, Terraform, Nginx, AWS, GCP, Azure, GitHub Actions, GitLab, Hetzner. Architecture and security: multi-tenant isolation, PostgreSQL RLS, Clean Architecture / DDD, TDD, OWASP ASVS, LDAP / AD, JWT, Semgrep. AI and automation: Claude / OpenAI / Gemini APIs, MCP, RAG / vector search, LangChain / LangGraph, LLM evals, Playwright, n8n, Whisper. Also: React, Next.js, Vue.js, C++, embedded / Klipper, Fusion 360." width="100%">

---

<sub>Jeleń is Polish for deer, and Yelon is roughly how it sounds in English. The banner and stack graphics are plain SVG files in this repo, generated by <code>scripts/gen.py</code>.</sub>
