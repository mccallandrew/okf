---
type: Step
title: Cleanup Step
description: Step where hand size is enforced, damage is removed, and "until end of turn" effects end.
tags: [mtg, turn, cleanup]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-514
    resource: /references/comprehensive-rules.md
    title: "CR 514 Cleanup Step"
---

# Definition

The **cleanup step** ends the turn: discard to maximum hand size, remove damage from permanents, and end "until end of turn" effects. Players usually do not get priority unless something triggers.[^cr-514]

# Rules

* Active player discards down to maximum hand size (normally seven).
* Damage marked on permanents is removed; "until end of turn" and similar effects wear off.
* If anything goes on the stack during cleanup, players get priority, then another cleanup step occurs after the stack empties.
* After cleanup completes with nothing pending, the next player's turn begins.

# Related

* [End Step](/turn/end-step.md)
* [Hand](/zones/hand.md)
* [Damage](/combat/damage.md)

[^cr]: Magic Comprehensive Rules
[^cr-514]: CR 514 Cleanup Step
