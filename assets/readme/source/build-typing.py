"""Generate the typing-line SVGs for the profile README.

Edit LINES or the timing below, then run:  python3 assets/readme/source/build-typing.py
Writes assets/readme/typing-light.svg and assets/readme/typing-dark.svg.
"""

from pathlib import Path
from xml.sax.saxutils import escape

LINES = [
    "M.S. in AI @ Northeastern · SWE intern @ Tiiny AI",
    "a video diary you can make with friends",
    "one memory shared by Claude Code and Codex",
    "an AI coach that changes the workout mid-session",
]

TYPE_MS = 55  # per character
DELETE_MS = 22  # per character
HOLD_MS = 1900  # full line on screen
GAP_MS = 380  # empty line before the next one

FONT_SIZE = 28
CHAR_W = FONT_SIZE * 0.6  # monospace advance; textLength pins every line to this grid
HEIGHT = 60
TEXT_X = 44  # after the prompt
WIDTH = round(TEXT_X + max(map(len, LINES)) * CHAR_W + 24)  # canvas fits the longest line
BASELINE = 39

THEMES = {
    "light": {"text": "#1f2328", "prompt": "#0969da", "cursor": "#0969da"},
    "dark": {"text": "#e6edf3", "prompt": "#4493f8", "cursor": "#4493f8"},
}


def pct(ms: float, total: float) -> str:
    return f"{ms / total * 100:.3f}%"


def build(theme: dict[str, str]) -> str:
    segments = []  # (start, typed, held, deleted) in ms per line
    t = 0.0
    for line in LINES:
        n = len(line)
        start, typed = t, t + n * TYPE_MS
        held = typed + HOLD_MS
        deleted = held + n * DELETE_MS
        segments.append((start, typed, held, deleted))
        t = deleted + GAP_MS
    total = t

    css = [
        f".t{{font:{FONT_SIZE}px ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace;fill:{theme['text']}}}",
        f".p{{font:700 {FONT_SIZE}px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;fill:{theme['prompt']}}}",
        ".r,.cur{transform-box:view-box;transform-origin:0 0}",
    ]
    cursor_frames = []
    clips, texts = [], []
    for i, (line, (start, typed, held, deleted)) in enumerate(zip(LINES, segments)):
        n = len(line)
        w = n * CHAR_W
        frames = [
            f"0%{{transform:scaleX(0)}}",
            f"{pct(start, total)}{{transform:scaleX(0);animation-timing-function:steps({n},end)}}",
            f"{pct(typed, total)}{{transform:scaleX(1);animation-timing-function:linear}}",
            f"{pct(held, total)}{{transform:scaleX(1);animation-timing-function:steps({n},end)}}",
            f"{pct(deleted, total)}{{transform:scaleX(0)}}",
            "100%{transform:scaleX(0)}",
        ]
        css.append(f"@keyframes k{i}{{{''.join(frames)}}}")
        css.append(f".r{i}{{animation:k{i} {total / 1000:.2f}s infinite}}")
        cursor_frames += [
            f"{pct(start, total)}{{transform:translateX(0);animation-timing-function:steps({n},end)}}",
            f"{pct(typed, total)}{{transform:translateX({w:.1f}px);animation-timing-function:linear}}",
            f"{pct(held, total)}{{transform:translateX({w:.1f}px);animation-timing-function:steps({n},end)}}",
            f"{pct(deleted, total)}{{transform:translateX(0)}}",
        ]
        clips.append(
            f'<clipPath id="c{i}"><rect class="r r{i}" x="{TEXT_X}" y="0" width="{w:.1f}" height="{HEIGHT}" '
            f'transform="scale(0 1)" style="transform-origin:{TEXT_X}px 0"/></clipPath>'
        )
        texts.append(
            f'<text class="t" x="{TEXT_X}" y="{BASELINE}" textLength="{w:.1f}" lengthAdjust="spacingAndGlyphs" '
            f'clip-path="url(#c{i})">{escape(line)}</text>'
        )
    css.append(f"@keyframes kc{{0%{{transform:translateX(0)}}{''.join(cursor_frames)}100%{{transform:translateX(0)}}}}")
    css.append(f".cur{{animation:kc {total / 1000:.2f}s infinite}}")
    css.append("@keyframes blink{0%,50%{opacity:1}50.01%,100%{opacity:0}}")
    css.append(".blink{animation:blink 1.06s infinite}")
    # Without motion, show the first line typed out.
    first_w = len(LINES[0]) * CHAR_W
    css.append(
        "@media (prefers-reduced-motion:reduce){.r,.cur,.blink{animation:none}"
        f".r0{{transform:scaleX(1)}}.cur{{transform:translateX({first_w:.1f}px)}}}}"
    )

    desc = " / ".join(LINES)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
<title id="title">What Cassie builds</title>
<desc id="desc">A typing animation cycling through: {escape(desc)}</desc>
<style>{''.join(css)}</style>
<defs>{''.join(clips)}</defs>
<text class="p" x="8" y="{BASELINE}">&gt;</text>
{''.join(texts)}
<g class="cur"><rect class="blink" x="{TEXT_X + 2}" y="{BASELINE - FONT_SIZE + 5}" width="3" height="{FONT_SIZE}" rx="1" fill="{theme['cursor']}"/></g>
</svg>
"""


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent
    for name, theme in THEMES.items():
        (out / f"typing-{name}.svg").write_text(build(theme))
        print("wrote", out / f"typing-{name}.svg")
