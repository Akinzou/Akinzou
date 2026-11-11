"""Generates assets/header.svg and assets/stack.svg.

Self-hosted on purpose: third-party README widgets go down or get rate-limited,
these are plain files GitHub serves itself. Run: python scripts/gen.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

BLUE, GREEN, PINK, PURPLE, YELLOW = "#00f0ff", "#00ff9d", "#ff00a0", "#bf00ff", "#ffe600"
BG, PANEL, LINE, DIM, TEXT = "#07070d", "#0d0d18", "#1c1c30", "#5b5b7a", "#d8d8ee"
MONO = "'JetBrains Mono','Cascadia Code','Fira Code',Consolas,'DejaVu Sans Mono','Courier New',monospace"

# ---------------------------------------------------------------- header.svg
W, H = 1200, 470

ascii_art = [
    r"__   __ _____ _      ___  _   _ ",
    r"\ \ / /| ____| |    / _ \| \ | |",
    r" \ V / |  _| | |   | | | |  \| |",
    r"  | |  | |___| |___| |_| | |\  |",
    r"  |_|  |_____|_____|\___/|_| \_|",
]

# (prompt-or-None, text, colour, start delay s, duration s)
term = [
    ("~ $ ", "cat ./about", TEXT, 0.6, 0.6),
    (None, "production backends · multi-tenant platforms · security-critical systems", BLUE, 1.3, 1.4),
    ("~ $ ", "ls ./builds", TEXT, 2.9, 0.6),
    (None, "multi-tenant-platforms/  workflow-orchestration/  llm-integration/  ci-cd/", GREEN, 3.4, 1.4),
    ("~ $ ", "cat ./status", TEXT, 5.0, 0.6),
    (None, "open to new roles · backend / platform / automation · root@yelon.dev", PINK, 5.7, 1.3),
]

grid = "".join(
    f'<line x1="{x}" y1="0" x2="{x}" y2="{H}"/>' for x in range(0, W + 1, 40)
) + "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}"/>' for y in range(0, H + 1, 40))

term_svg = []
anim_css = []
y0, dy = 250, 30
for i, (prompt, text, colour, delay, dur) in enumerate(term):
    y = y0 + i * dy
    cls = f"t{i}"
    anim_css.append(
        f".{cls}{{animation:type {dur}s steps({max(len(text), 1)},end) {delay}s backwards}}"
    )
    prompt_svg = (
        f'<tspan fill="{PURPLE}">{escape(prompt)}</tspan>' if prompt else '<tspan fill="#3a3a55">  › </tspan>'
    )
    term_svg.append(
        f'<text x="64" y="{y}" class="mono {cls}" font-size="19">{prompt_svg}'
        f'<tspan fill="{colour}">{escape(text)}</tspan></text>'
    )
last_y = y0 + len(term) * dy
end_delay = term[-1][3] + term[-1][4]

ascii_svg = "".join(
    f'<text x="760" y="{96 + i * 22}" class="mono" font-size="18" fill="url(#neon)" '
    f'xml:space="preserve">{escape(line)}</text>'
    for i, line in enumerate(ascii_art)
)

header = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" aria-labelledby="title desc">
<title id="title">Wiktor Jeleń — Backend &amp; Platform Engineer</title>
<desc id="desc">Terminal-style banner: Wiktor Jeleń, backend and platform engineer in Cracow, Poland. Builds multi-tenant platforms, workflow orchestration, LLM integration and CI/CD. Open to new roles: root@yelon.dev</desc>
<defs>
  <linearGradient id="neon" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
    <stop offset="0" stop-color="{BLUE}"/><stop offset="0.5" stop-color="{PURPLE}"/><stop offset="1" stop-color="{PINK}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.4 0;0.4 0;-0.4 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}" stop-opacity="1"/>
  </linearGradient>
  <filter id="glow" x="-20%" y="-50%" width="140%" height="200%">
    <feGaussianBlur stdDeviation="6" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  <style>
    .mono{{font-family:{MONO};}}
    @keyframes type{{from{{clip-path:inset(0 100% 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}
    @keyframes blink{{50%{{opacity:0}}}}
    @keyframes hide{{from,to{{opacity:0}}}}
    @keyframes scan{{from{{transform:translateY(-60px)}}to{{transform:translateY({H}px)}}}}
    @keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
    .cursor{{animation:hide {end_delay}s, blink 1s step-end {end_delay}s infinite}}
    .scan{{animation:scan 7s linear infinite}}
    .rise{{animation:rise .8s ease-out .1s backwards}}
    {''.join(anim_css)}
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.scan{{display:none}}}}
  </style>
</defs>
<g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  <g stroke="{LINE}" stroke-width="1" opacity="0.55">{grid}</g>
  <rect y="{H - 160}" width="{W}" height="160" fill="url(#fade)"/>
  <rect class="scan" width="{W}" height="60" fill="{BLUE}" opacity="0.035"/>

  <!-- title bar -->
  <rect width="{W}" height="40" fill="{PANEL}"/>
  <line x1="0" y1="40" x2="{W}" y2="40" stroke="{LINE}"/>
  <circle cx="26" cy="20" r="6.5" fill="#ff5f57"/><circle cx="48" cy="20" r="6.5" fill="#febc2e"/><circle cx="70" cy="20" r="6.5" fill="#28c840"/>
  <text x="{W / 2}" y="26" text-anchor="middle" class="mono" font-size="14" fill="{DIM}">yelon@cracow: ~</text>

  <!-- name -->
  <g class="rise">
    <text x="62" y="128" class="mono" font-size="66" font-weight="800" fill="url(#neon)" filter="url(#glow)" letter-spacing="2">WIKTOR JELEŃ</text>
    <text x="66" y="172" class="mono" font-size="20" fill="{BLUE}" letter-spacing="5">BACKEND &amp; PLATFORM ENGINEER</text>
    <text x="66" y="202" class="mono" font-size="15" fill="{DIM}" letter-spacing="1">TypeScript · Python · PostgreSQL · Temporal · LLM integration · CI/CD</text>
  </g>
  <g opacity="0.85">{ascii_svg}</g>
  <text x="762" y="222" class="mono" font-size="14" fill="{DIM}">jeleń = deer · yelon.dev</text>

  {''.join(term_svg)}
  <text x="64" y="{last_y}" class="mono" font-size="19" fill="{PURPLE}">~ $ </text>
  <rect class="cursor" x="112" y="{last_y - 17}" width="11" height="21" fill="{GREEN}"/>
</g>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{LINE}"/>
</svg>
"""
(ASSETS / "header.svg").write_text(header, encoding="utf-8")

# ----------------------------------------------------------------- stack.svg
groups = [
    ("BACKEND & DATA", BLUE, ["TypeScript", "Node.js", "NestJS", "Python", "FastAPI", "Django / DRF",
                              "PHP / Laravel", "PostgreSQL", "MySQL", "MongoDB", "Redis", "Temporal.io"]),
    ("PLATFORM & INFRA", PURPLE, ["Linux", "Docker", "Kubernetes", "Terraform", "Nginx", "AWS", "GCP",
                                  "Azure", "GitHub Actions", "GitLab", "Hetzner"]),
    ("ARCHITECTURE & SECURITY", GREEN, ["Multi-tenant isolation", "PostgreSQL RLS", "Clean Architecture / DDD",
                                        "TDD", "OWASP ASVS", "LDAP / AD", "JWT", "Semgrep"]),
    ("AI & AUTOMATION", PINK, ["Claude / OpenAI / Gemini APIs", "MCP", "RAG / vector search",
                               "LangChain / LangGraph", "LLM evals", "Playwright", "n8n", "Whisper"]),
    ("ALSO", YELLOW, ["React", "Next.js", "Vue.js", "C++", "Embedded / Klipper", "Fusion 360"]),
]

SW = 1200
FS = 15
CHAR = FS * 0.62  # generous monospace advance so wider fallback fonts still fit
PAD_X, CHIP_H, GAP = 14, 30, 10
LABEL_W = 250
x_start, x_max = 40 + LABEL_W, SW - 40

rows = []
y = 64
for label, colour, items in groups:
    x = x_start
    chips = []
    row_y = y
    for item in items:
        w = round(len(item) * CHAR + PAD_X * 2)
        if x + w > x_max:
            x = x_start
            y += CHIP_H + GAP
        chips.append(
            f'<g transform="translate({x},{y})"><rect width="{w}" height="{CHIP_H}" rx="7" fill="{colour}" '
            f'fill-opacity="0.08" stroke="{colour}" stroke-opacity="0.55"/>'
            f'<text x="{w / 2}" y="20" text-anchor="middle" class="mono" font-size="{FS}" fill="{TEXT}">'
            f"{escape(item)}</text></g>"
        )
        x += w + GAP
    rows.append(
        f'<g class="row"><rect x="40" y="{row_y + 4}" width="4" height="22" rx="2" fill="{colour}"/>'
        f'<text x="56" y="{row_y + 20}" class="mono" font-size="14" font-weight="700" fill="{colour}" '
        f'letter-spacing="1.5">{escape(label)}</text>{"".join(chips)}</g>'
    )
    y += CHIP_H + 26
SH = y + 8

all_items = "; ".join(f"{label.title()}: {', '.join(items)}" for label, _, items in groups)
stack = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SW} {SH}" width="100%" role="img" aria-labelledby="title desc">
<title id="title">Tech stack</title>
<desc id="desc">{escape(all_items)}</desc>
<defs><style>.mono{{font-family:{MONO};}}</style></defs>
<rect x="0.5" y="0.5" width="{SW - 1}" height="{SH - 1}" rx="18" fill="{BG}" stroke="{LINE}"/>
<text x="40" y="38" class="mono" font-size="14" fill="{DIM}">~ $ <tspan fill="{TEXT}">cat stack.yml</tspan></text>
{"".join(rows)}
</svg>
"""
(ASSETS / "stack.svg").write_text(stack, encoding="utf-8")
print("header.svg", W, "x", H, "| stack.svg", SW, "x", SH)
