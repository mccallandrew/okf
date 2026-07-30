---
type: Step
title: End Step
description: Step where "until end of turn" effects are still active and end-of-turn triggers fire.
tags: [mtg, turn, end-step]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-513
    resource: /references/comprehensive-rules.md
    title: "CR 513 End Step"
---

# Definition

In the **end step**, "at the beginning of the end step" / "at end of turn" triggers are put on the stack, then players receive priority.[^cr-513]

# Rules

* "Until end of turn" effects still apply during the end step.
* After all players pass with an empty stack, the game moves to cleanup.
* Instant-speed interaction is allowed while players have priority.

# Related

* [Ending Phase](/turn/ending-phase.md)
* [Cleanup Step](/turn/cleanup-step.md)
* [Triggered Abilities](/stack-and-priority/triggered-abilities.md)

[^cr]: Magic Comprehensive Rules
[^cr-513]: CR 513 End Step
