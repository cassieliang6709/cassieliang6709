# Hi, I'm Cassie.

I'm a software engineer building AI systems people can actually use—from retrieval and agent memory to SwiftUI products.

I'm currently pursuing an M.S. in Artificial Intelligence at Northeastern University, where I'm also a graduate TA for Foundations of Generative AI, and I'm a software engineering intern at Tiiny AI working on an agent skills platform. Before engineering, I studied accounting and worked in audit at Deloitte. That background still shows up in how I build: I care about where an answer came from, what the system is allowed to do, and how we know it works.

[Portfolio](https://liangyue.site) · [LinkedIn](https://www.linkedin.com/in/yue-liang-195960384/) · [Email](mailto:liangyue3666@gmail.com)

## 1Day — a video diary you can make with friends

**On the App Store.** 1Day asks how you want to spend today. You pick a theme, follow a few filming prompts, and the app turns the clips into a short film. You can do it alone or invite friends into a shared story.

I built the iOS app end to end. The film is assembled entirely on the device with AVFoundation—orientation, transitions, captions, audio, and the MP4 export—so no footage is uploaded for rendering. Shared stories sync rooms, participants, and clips through CloudKit, and solo mode needs no account at all.

[App Store](https://apps.apple.com/cn/app/1-day/id6794565199) · [Website](https://1day.liangyue.site) · [Code](https://github.com/cassieliang6709/1day-ios)

## Other things I've built

### [MindBridge](https://github.com/cassieliang6709/mindbridge) — memory for AI coding agents

A local-first service that gives Claude Code, Codex, and other agents context that survives between sessions. It reads their logs, turns them into searchable memories and preferences in PostgreSQL / pgvector, and serves the same read and write paths over MCP so several agents can share one memory. A locally fine-tuned Qwen2.5-3B does the structured extraction.

[Code](https://github.com/cassieliang6709/mindbridge) · [Demo](https://mindbridge.liangyue.site/interview-demo)

### [Vance](https://github.com/cassieliang6709/fitness-coach-ios) — an AI fitness coach that can change the workout

I designed Vance in Figma, then built the iOS app and the backend. It reads photos of your equipment and turns your goals and injuries into a training plan. During the session you can ask it to change a weight or swap an exercise and it just does it—the model streams tool calls from Cloudflare Workers, and the app runs only the actions on its allowlist.

[Code](https://github.com/cassieliang6709/fitness-coach-ios) · [Demo](https://vance.liangyue.site)

### [CorpCheck](https://github.com/cassieliang6709/corpcheck) — SEC filing search that knows when not to answer

A research tool over SEC filings that returns evidence instead of a confident-sounding paragraph. It fuses vector and full-text search, filters by company, fiscal year, form, and amendment version before ranking, and refuses outright when the retrieved evidence is too weak to support an answer.

[Code](https://github.com/cassieliang6709/corpcheck) · [Demo](https://corpcheck.liangyue.site)

### [OpenTranscript](https://github.com/cassieliang6709/open-transcript) — read a video instead of watching it

A Chrome extension and a local service that put a searchable transcript next to a YouTube or Bilibili video. You keep the passages that matter, ask questions grounded in the captions, and get a Markdown note with clickable timestamps. Whole Bilibili collections keep processing in the background after you close the panel.

[Code](https://github.com/cassieliang6709/open-transcript) · [Download](https://github.com/cassieliang6709/open-transcript/releases/latest)

## Work and smaller projects

- **Tiiny AI (SWE intern, Jul 2026–present):** building an agent skills platform—skill sourcing and catalog APIs, the desktop install and update experience, and a Rust/Python distribution backend that handles versioning, validation, rollback, offline caching, and permission checks.
- **[VisoCode](https://github.com/cassieliang6709/new_manim_video):** LangGraph agents that write, audit, run, and repair Manim lessons inside Docker sandboxes. Winner of the **AdventureX 2025 Best Technical Award**.
- **[Cassie Capture](https://github.com/cassieliang6709/cassie-capture):** a Chrome extension that captures long webpages in segments and merges them into one PDF.
- **[Tabspace](https://chromewebstore.google.com/detail/tabspace/pigfllmaggabolcjieedkilhpdfcddai):** a local-first Chrome workspace for tabs and bookmarks, with a review step before any bulk change.

## Tools I reach for

Python, TypeScript, Swift, Rust, SQL · FastAPI, PostgreSQL / pgvector, Redis, Celery, Docker · RAG, Postgres FTS / RRF, MCP, structured outputs, MLX LoRA, offline evaluation · React, SwiftUI, AVFoundation, Electron, Chrome MV3
