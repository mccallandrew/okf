---
type: Game Procedure
title: Timing Overview
description: How priority, the stack, and timing restrictions interact.
tags: [mtg, stack, timing]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-117
    resource: /references/comprehensive-rules.md
    title: "CR 117 Timing and Priority"
---

# Definition

Magic timing is: turn-based actions and triggers → [priority](/turn/priority.md) → spells/abilities on the [stack](/zones/stack.md) → resolve when all players pass.[^cr-117]

# Flow

1. Step or phase begins; perform turn-based actions.
2. Put pending triggered abilities on the stack.
3. Active player gets priority.
4. Players cast spells, activate abilities, or take special actions, or pass.
5. When all pass: resolve top of stack, or advance the turn if stack is empty.

# Timing restrictions

* Instants and abilities with flash-like timing: whenever you have priority.
* Sorceries and most permanents: main phase, your turn, empty stack (unless flash or an effect allows otherwise).

# Related

* [Priority](/turn/priority.md)
* [Stack](/zones/stack.md)
* [Casting Spells](/stack-and-priority/casting-spells.md)
* [Resolving](/stack-and-priority/resolving.md)
* [Flash](/keywords/flash.md)

[^cr]: Magic Comprehensive Rules
[^cr-117]: CR 117 Timing and Priority
