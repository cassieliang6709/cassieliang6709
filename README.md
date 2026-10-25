# Hi, I'm Cassie.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/readme/typing-dark.svg">
  <img src="./assets/readme/typing-light.svg" width="640" alt="M.S. in AI at Northeastern, SWE intern at Tiiny AI · a video diary you can make with friends · one memory shared by Claude Code and Codex · now learning AI infra and RL post-training · GRPO on GSM8K: 34.7% to 52.2% on one RTX 4090">
</picture>

AI master's student at Northeastern, SWE intern at Tiiny AI. I'm focusing on **LLM inference and training systems** — reading SGLang and nano-vllm, working through CS336, and running small, controlled experiments on one GPU. On the side I ship products: 1Day is on the App Store.

[Portfolio](https://liangyue.site) · [Notes](https://notes.liangyue.site) · [LinkedIn](https://www.linkedin.com/in/yue-liang-195960384/) · [Email](mailto:liangyue3666@gmail.com)

## Open source

| Project | Contribution | Status |
|---|---|---|
| [SGLang](https://github.com/sgl-project/sglang) | Cache CPU image-preprocessing artifacts for MiniMax-M3 multimodal serving — [#44181](https://github.com/sgl-project/sglang/pull/44181) | 🟡 Open |
| [OpenLess](https://github.com/Open-Less/openless) | Prefer the microphone's native format and reject empty recordings — [#1135](https://github.com/Open-Less/openless/pull/1135) | ✅ Merged |
| [Raycast-Easydict](https://github.com/tisfeng/Raycast-Easydict) | Send favorite words to Anki — [#109](https://github.com/tisfeng/Raycast-Easydict/pull/109) | ✅ Merged |
| [modular-diary](https://github.com/IvyYang1999/modular-diary) | 6 PRs: checkbox-list todos, drag-to-timeline, current-time marker, CI test-runner fix — [#2–#7](https://github.com/IvyYang1999/modular-diary/pulls?q=is%3Apr+author%3Acassieliang6709) | ✅ Merged |

## LLM systems & research

**GRPO on GSM8K** — baseline → LoRA SFT → GRPO reproduction on a single RTX 4090: 34.7% → 52.2%.
[Code](https://github.com/cassieliang6709/ai-infra-gsm8k)

**Stop-token study** — does a chat model learn to stop if its end token never appeared in pretraining? A controlled MiniMind pretraining experiment.
[Code](https://github.com/cassieliang6709/stop-token-study)

**Agent honesty eval** — does a coding agent admit a task is impossible? MBPP-derived tasks with contradictory tests, a tamper-proof grader, Qwen2.5-Coder 3B/7B results.
[Code](https://github.com/cassieliang6709/agent-honesty-eval)

**CorpCheck** — SEC filing search that knows when not to answer: vector + full-text retrieval fused with RRF, revision-aware filtering, deterministic IR evaluation, refusal on weak evidence.
[Code](https://github.com/cassieliang6709/corpcheck) · [Demo](https://corpcheck.liangyue.site)

## Products

**1Day** — a video diary you can make with friends. Follow filming prompts and the app assembles a short film entirely on-device (AVFoundation); shared stories sync through CloudKit. Built end to end.
[App Store](https://apps.apple.com/us/app/1-day/id6794565199) · [Website](https://1day.liangyue.site) · [Code](https://github.com/cassieliang6709/1day-ios)

**MindBridge** — one memory shared by Claude Code and Codex. Turns agent logs into searchable memories in PostgreSQL / pgvector, served over MCP.
[Code](https://github.com/cassieliang6709/mindbridge) · [Demo](https://mindbridge.liangyue.site/interview-demo)

**VisoCode** — LangGraph agents that write, audit, run and repair Manim lessons in Docker sandboxes. AdventureX 2025 Best Technical Award.
[Code](https://github.com/cassieliang6709/new_manim_video)

**OpenTranscript** — a searchable transcript beside any YouTube / Bilibili video, exported as a Markdown note with clickable timestamps.
[Code](https://github.com/cassieliang6709/open-transcript) · [Download](https://github.com/cassieliang6709/open-transcript/releases/latest)

**Vance** — an AI fitness coach that edits your workout mid-session through allowlisted tool calls.
[Code](https://github.com/cassieliang6709/fitness-coach-ios) · [Demo](https://vance.liangyue.site)

## Work

**Tiiny AI** — SWE intern, Jul 2026–present. Agent skills platform: catalog APIs, desktop install/update flow, and a Rust/Python distribution backend with versioning, validation, rollback and permission checks.

**Northeastern** — TA, CS6180 Foundations of Generative AI.

**Deloitte** — audit assistant, 2023–2024. Automated ledger reconciliation; encoded recurring review checks as configurable rules.

## Stack

Python · TypeScript · Swift · Rust · SQL — PyTorch, SGLang, MLX · FastAPI, PostgreSQL / pgvector, Redis, Docker · RAG, MCP, LoRA / GRPO · SwiftUI, AVFoundation, React
