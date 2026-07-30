---
type: Card Type
title: Aura
description: Enchantment subtype that enters attached to an object or player via enchant.
tags: [mtg, card-types, enchantment, aura]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-303-4
    resource: /references/comprehensive-rules.md
    title: "CR 303.4 Auras"
  - id: cr-704-5m
    resource: /references/comprehensive-rules.md
    title: "CR 704.5m Illegal Aura attachment"
---

# Definition

An **Aura** is an enchantment subtype. An Aura enters the battlefield attached to an object or player; what it can enchant is defined by its **enchant** keyword ability.[^cr-303-4]

# Rules

* An Aura spell requires a target defined by its enchant ability; if that target is illegal on resolution, the Aura spell is countered.
* As it resolves (or otherwise enters), the Aura enters attached to the chosen object or player.
* If an Aura is attached to an illegal object or player, is not attached to anything, or the enchanted object no longer exists, it is put into its owner’s graveyard as a state-based action.[^cr-704-5m]
* Control of an Aura is separate from control of what it enchants.
* An Aura that’s also a creature can’t enchant anything; if that occurs, it becomes unattached and then goes to the graveyard.

# Related

* [Enchantment](/card-types/enchantment.md)
* [Targets](/stack-and-priority/targets.md)
* [Permanents](/foundations/permanents.md)
* [Continuous Effects](/effects/continuous-effects.md)

[^cr]: Magic Comprehensive Rules
[^cr-303-4]: CR 303.4 Auras
[^cr-704-5m]: CR 704.5m Illegal Aura attachment
