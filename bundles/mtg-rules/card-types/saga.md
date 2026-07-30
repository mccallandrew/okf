---
type: Card Type
title: Saga
description: Enchantment subtype that advances with lore counters and chapter abilities, then is sacrificed.
tags: [mtg, card-types, enchantment, saga]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-303-5
    resource: /references/comprehensive-rules.md
    title: "CR 303.5 Sagas"
  - id: cr-714
    resource: /references/comprehensive-rules.md
    title: "CR 714 Saga Cards"
---

# Definition

A **Saga** is an enchantment subtype. Sagas track progress with **lore counters**; chapter symbols represent triggered **chapter abilities** that fire as counters reach each chapter number.[^cr-714]

# Rules

* A Saga without read ahead enters with one lore counter; as its controller’s precombat main phase begins, that player puts another lore counter on each Saga they control (turn-based action).
* A chapter ability triggers when lore counters on the Saga go from below that chapter’s number to at least that number.
* Chapter abilities use the stack and can be responded to.
* A Saga’s final chapter number is the greatest chapter number among its chapter abilities.
* After the number of lore counters is greater than or equal to the final chapter number, and that Saga is not the source of a chapter ability still on the stack, its controller sacrifices it as a state-based action.

# Related

* [Enchantment](/card-types/enchantment.md)
* [Main Phase](/turn/main-phase.md)
* [Triggered Abilities](/stack-and-priority/triggered-abilities.md)
* [Aura](/card-types/aura.md)

[^cr]: Magic Comprehensive Rules
[^cr-303-5]: CR 303.5 Sagas
[^cr-714]: CR 714 Saga Cards
