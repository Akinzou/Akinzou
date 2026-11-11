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

I start from architecture, invariants and failure modes, then write the code and prove it with tests and CI. I work AI-native every day with Claude Code, OpenAI Codex and Antigravity.

Most of my commercial code is in private client repositories; [yelon.dev](https://yelon.dev) describes those systems.

> **Open to new roles:** backend, platform or automation engineering, in Cracow or remote. Write to [root@yelon.dev](mailto:root@yelon.dev).

## Open source

**Contributions**

| Project | What I did |
| --- | --- |
| [**ros2_medkit**](https://github.com/selfpatch/ros2_medkit)<br>[![Stars](https://img.shields.io/github/stars/selfpatch/ros2_medkit?color=bf00ff&labelColor=07070d)](https://github.com/selfpatch/ros2_medkit) | Diagnostics gateway for ROS 2 robots (C++). [Merged fix](https://github.com/selfpatch/ros2_medkit/pull/775) in the fault manager: a snapshot topic whose publisher starts after the node used to be skipped for good; now it is picked up as soon as the graph reports its type. |
| [**pytripgui**](https://github.com/pytrip/pytripgui)<br>[![Stars](https://img.shields.io/github/stars/pytrip/pytripgui?color=bf00ff&labelColor=07070d)](https://github.com/pytrip/pytripgui) | GUI for PyTRiP, radiotherapy treatment planning with ions (Python). Moved the plan and field models to Pythonic properties as part of the MVC refactor. |

**My projects**

| Project | What it does |
| --- | --- |
| [**PythonMetaTrader5**](https://github.com/Akinzou/MetaTrader5-Python) | Python layer over the MetaTrader 5 API for algorithmic trading: order normalization, full retcode handling, safeguards for live accounts.<br>[![Downloads](https://static.pepy.tech/badge/pythonmetatrader5)](https://pepy.tech/project/pythonmetatrader5) [![PyPI](https://img.shields.io/pypi/v/PythonMetaTrader5?color=00f0ff&labelColor=07070d)](https://pypi.org/project/PythonMetaTrader5/) |
| [**TradeLockerBot**](https://github.com/Akinzou/TradeLockerBot) | FastAPI service that turns TradingView alerts into TradeLocker orders. The webhook path is a random secret printed once at startup. Docker image built by GitHub Actions. |
| [**CapitalCom**](https://github.com/Akinzou/CapitalCom) | Python client for the Capital.com API.<br>[![Downloads](https://static.pepy.tech/badge/capitalcom)](https://pepy.tech/project/capitalcom) [![PyPI](https://img.shields.io/pypi/v/capitalcom?color=00f0ff&labelColor=07070d)](https://pypi.org/project/capitalcom/) |
| [**TradingViewBacktester**](https://github.com/Akinzou/TradingViewBacktester) | Backtester for TradingView strategies in Python. |

## Stack

<img src="./assets/stack.svg" alt="Stack. Backend and data: TypeScript, Node.js, NestJS, Python, FastAPI, Django / DRF, PHP / Laravel, PostgreSQL, MySQL, MongoDB, Redis, Temporal.io. Platform and infra: Linux, Docker, Kubernetes, Terraform, Nginx, AWS, GCP, Azure, GitHub Actions, GitLab, Hetzner. Architecture and security: multi-tenant isolation, PostgreSQL RLS, Clean Architecture / DDD, TDD, OWASP ASVS, LDAP / AD, JWT, Semgrep. AI and automation: Claude / OpenAI / Gemini APIs, MCP, RAG / vector search, LangChain / LangGraph, LLM evals, Playwright, n8n, Whisper. Also: React, Next.js, Vue.js, C++, embedded / Klipper, Fusion 360." width="100%">

<details>
<summary>Stack as text</summary>

- **Backend & data:** TypeScript, Node.js, NestJS, Python, FastAPI, Django / DRF, PHP / Laravel, PostgreSQL, MySQL, MongoDB, Redis, Temporal.io
- **Platform & infra:** Linux, Docker, Kubernetes, Terraform, Nginx, AWS, GCP, Azure, GitHub Actions, GitLab, Hetzner
- **Architecture & security:** multi-tenant isolation, PostgreSQL RLS, Clean Architecture / DDD, TDD, OWASP ASVS, LDAP / AD, JWT, Semgrep
- **AI & automation:** Claude / OpenAI / Gemini APIs, MCP, RAG / vector search, LangChain / LangGraph, LLM evals, Playwright, n8n, Whisper
- **Also:** React, Next.js, Vue.js, C++, embedded / Klipper, Fusion 360

</details>

---

<sub>Jeleń is Polish for deer, and Yelon is roughly how it sounds in English. The banner and stack graphics are plain SVG files in this repo, generated by <code>scripts/gen.py</code>.</sub>
