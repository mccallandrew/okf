---
type: Strategy Concept
title: Mana Curve Construction
description: Practical steps for building and reading a mana curve for a chosen game plan.
tags: [mtg, deckbuilding, mana, curve]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:00:00Z }
sources:
  - id: wiz-curve
    resource: /references/wizards-mana-curve.md
    title: How to Build a Mana Curve
  - id: wiz-mana
    resource: /references/wizards-basics-of-mana.md
    title: The Basics of Mana
---

# Definition

**Mana curve construction** is the practice of laying out spells by expected cast turn, trimming clumped expensive slots, and ensuring early actions exist for the plan.[^wiz-curve]

# Guidelines

1. Separate **on-curve** plays (usually creatures / proactive permanents) from **off-curve** interaction.[^wiz-curve]
2. Count how many spells you want on turns 1–5 for your archetype; cut extras at high CMC first.
3. Ask whether each expensive card is necessary or whether a cheaper substitute keeps the same role.
4. After the spell curve is set, choose [land counts](/mana/land-counts.md) and [colored sources](/mana/colored-sources.md) to support it.[^wiz-mana]

# Format notes

* **Limited**: Aim for a creature curve with a peak at two and three; see [Limited Curves](/limited/limited-curves.md).
* **Commander**: Average mana value and commander cost dominate; rocks shift effective curve—see Karsten’s Commander analysis via [references](/references/karsten-commander-curve.md).

# Related

* [Mana Curve](/foundations/mana-curve.md)
* [Land Counts](/mana/land-counts.md)
* [Goldfishing](/process/goldfishing.md)

[^wiz-curve]: How to Build a Mana Curve
[^wiz-mana]: The Basics of Mana
