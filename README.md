# Hi, I'm Cassie.

I'm a software engineer building AI systems people can actually use—from retrieval and agent memory to SwiftUI products.

I'm currently pursuing an M.S. in Artificial Intelligence at Northeastern University, where I'm also a graduate TA for Foundations of Generative AI. Before engineering, I studied accounting and worked in audit at Deloitte. That background still shows up in how I build: I care about where an answer came from, what the system is allowed to do, and how we know it works.

[Portfolio](https://liangyue.site) · [LinkedIn](https://www.linkedin.com/in/yue-liang-195960384/) · [Email](mailto:liangyue3666@gmail.com)

## What I'm building

### [MindBridge](https://github.com/cassieliang6709/mindbridge) — memory for AI coding agents

A local-first service that gives Claude Code, Codex, and other agents useful context across sessions.

- Incrementally parsed coding-agent logs into **13,072 turns and 242 session cards**
- Stored raw turns, searchable memories, and preferences in PostgreSQL / pgvector with links back to their sources
- Exposed the same write and search paths through MCP so multiple agents can share one memory service
- Fine-tuned Qwen2.5-3B with MLX LoRA for structured extraction, reaching **86.7% validity on 45 held-out cases**

[Code](https://github.com/cassieliang6709/mindbridge) · [Demo](https://mindbridge.liangyue.site/interview-demo)

### [Vance](https://github.com/cassieliang6709/fitness-coach-ios) — an AI fitness coach that can update the workout

I designed Vance in Figma, then built the iOS app and backend. It turns equipment photos, goals, and injuries into a training plan, then lets the user change weights or swap exercises without leaving the workout.

- Streams typed tool calls to the app; iOS executes only allowlisted actions
- Keeps **1,324 exercises** in D1, with 50 core exercises available offline
- Uses spoken feedback and TTS to announce the next set hands-free

[Code](https://github.com/cassieliang6709/fitness-coach-ios) · [Demo](https://vance.liangyue.site)

### [CorpCheck](https://github.com/cassieliang6709/corpcheck) — SEC filing retrieval that knows when not to answer

A financial research system built around evidence retrieval rather than a confident-sounding chatbot.

- Searches **1,662 SEC filings / 469,874 chunks** with pgvector, BM25, and reciprocal-rank fusion
- Filters by company, fiscal year, form, and amendment version before ranking
- Skips the LLM when the retrieved evidence falls below calibrated thresholds
- Reduced top-10 evidence misses from **19 to 4** on 35 FinanceBench questions

[Code](https://github.com/cassieliang6709/corpcheck) · [Demo](https://corpcheck.liangyue.site)

### [1Day](https://github.com/cassieliang6709/1day-ios) — a collaborative video diary for iOS

A local-first iOS app that turns short daily clips into a shared film without sending video rendering to a server.

- Renders orientation, transitions, captions, audio, and MP4 export on-device with AVFoundation
- Syncs rooms, participants, and clips through CloudKit while keeping solo mode account-free
- Currently in private beta with **28 / 28 XCTest cases passing**

[Code](https://github.com/cassieliang6709/1day-ios) · [Demo](https://1day.liangyue.site)

## Work and selected projects

- **Smith-Kettlewell Eye Research Institute:** built a React review UI and FastAPI pipeline using Whisper, VLM / LLM, and TTS for audio-description authoring. In a 30-participant study, manual authoring time fell **64%** from the baseline editor.
- **[VisoCode](https://github.com/cassieliang6709/new_manim_video):** LangGraph agents generate, audit, run, and repair Manim lessons inside Docker sandboxes. Winner of the **AdventureX 2025 Best Technical Award**.
- **[Cassie Capture](https://github.com/cassieliang6709/cassie-capture):** a Chrome extension that captures restricted long webpages in segments and merges them into a complete PDF.
- **[Tabspace](https://chromewebstore.google.com/detail/tabspace/pigfllmaggabolcjieedkilhpdfcddai):** a local-first Chrome workspace for tabs and bookmarks, with a review step before bulk changes.

## Tools I reach for

Python, TypeScript, Swift, SQL · FastAPI, PostgreSQL / pgvector, Redis, Docker · RAG, BM25 / RRF, MCP, MLX LoRA, offline evaluation · React, SwiftUI, AVFoundation, Chrome MV3
