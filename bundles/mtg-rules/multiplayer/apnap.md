---
type: Game Procedure
title: APNAP
description: Active Player, Nonactive Player order for simultaneous choices and triggers.
tags: [mtg, multiplayer, apnap, priority]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-101
    resource: /references/comprehensive-rules.md
    title: "CR 101 The Magic Golden Rules"
  - id: cr-603
    resource: /references/comprehensive-rules.md
    title: "CR 603 Handling Triggered Abilities"
---

# Definition

**APNAP** (Active Player, Nonactive Player) is the order used when multiple players would make choices or take actions at the same time: the active player first, then each other player in turn order.[^cr-101]

# Rules

* Choices are made in APNAP order; then the resulting actions usually happen simultaneously.[^cr-101]
* When multiple triggered abilities wait to go on the stack, each player in APNAP order puts their triggers on the stack in an order they choose.[^cr-603]
* Objects put on the stack at the same time are ordered by APNAP (active player's objects lowest), with each player ordering their own relative stack positions.
* Multiplayer combat that attacks more than one player uses APNAP for declaring blockers and assigning combat damage among defending players. See [Attacking Multiple Players](/multiplayer/attacking-multiple-players.md).
* If a later nonactive player's choice forces an earlier player to choose again, APNAP restarts for outstanding choices.[^cr-101]

# Related

* [Golden Rules](/foundations/golden-rules.md)
* [Players](/foundations/players.md)
* [Priority](/turn/priority.md)
* [Triggered Abilities](/stack-and-priority/triggered-abilities.md)
* [Multiplayer Overview](/multiplayer/multiplayer-overview.md)

[^cr]: Magic Comprehensive Rules
[^cr-101]: CR 101 The Magic Golden Rules
[^cr-603]: CR 603 Handling Triggered Abilities
