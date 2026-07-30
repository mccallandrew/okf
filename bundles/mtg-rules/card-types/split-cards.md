---
type: Rule Concept
title: Split Cards
description: Cards with two halves; cast one half (or fuse both), with combined characteristics off the stack.
tags: [mtg, card-types, layouts, split]
status: stable
generated: { by: okf-complete-agent/composer, at: 2026-07-29T06:00:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-709
    resource: /references/comprehensive-rules.md
    title: "CR 709 Split Cards"
---

# Definition

A **split card** has two halves side by side (often with distinct names and mana costs). You normally cast only one half; some split cards with fuse can be cast as both halves together.[^cr-709]

# Rules

* Only the chosen half is evaluated for legality and becomes the spell on the stack; the other half’s characteristics don’t exist while the spell is on the stack (fuse is an exception — a fused split spell has the combined characteristics of both halves).
* In every zone **except** the stack, a split card’s characteristics are those of its two halves combined (two names, combined mana cost / mana value, each type and ability from either half).
* If an effect instructs a player to choose a card name and the player wants to choose a split card, the player must choose one of its halves’ names (not both).
* Some newer split permanents share a single type line and use lock/unlock designations for each half; treat those as a specialized split layout under CR 709.5.

# Related

* [Casting Spells](/stack-and-priority/casting-spells.md)
* [Characteristics](/foundations/characteristics.md)
* [Modal Spells and Abilities](/stack-and-priority/modal-spells.md)
* [Double-Faced Cards](/card-types/double-faced-cards.md)
* [Adventure](/card-types/adventure.md)

[^cr]: Magic Comprehensive Rules
[^cr-709]: CR 709 Split Cards
