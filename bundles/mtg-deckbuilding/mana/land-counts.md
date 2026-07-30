---
type: Strategy Concept
title: Land Counts
description: Heuristics for how many lands and virtual mana sources to include by format and curve.
tags: [mtg, deckbuilding, mana, lands]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:00:00Z }
sources:
  - id: wiz-mana
    resource: /references/wizards-basics-of-mana.md
    title: The Basics of Mana
  - id: karsten-sources
    resource: /references/karsten-colored-sources.md
    title: How Many Sources (2022)
  - id: karsten-edh
    resource: /references/karsten-commander-curve.md
    title: Commander Curve and Ramp
---

# Definition

**Land count** is the number of lands in the deck, adjusted for **virtual lands**—mana dorks, rocks, rituals, and MDFC lands that sometimes act as spells.[^wiz-mana]

# Guidelines

* **60-card Constructed**: Common baselines cluster around the low-to-mid 20s; lower for hyper-aggro with cheap curves, higher for control and greedy mana. A useful calibration is roughly scaling with average mana value of spells (Karsten-style formulas appear in community tools citing his work).[^karsten-sources]
* **40-card Limited**: Often 16–18 lands depending on curve, fixing, and card quality; splash colors need thoughtful sources.
* **Commander (99)**: Community baselines often sit in the mid-30s lands plus a ramp package; tune with commander cost and draw density.[^karsten-edh]
* Count untapped colored sources carefully when mixing utility lands that enter tapped.

# Format notes

* Fast mana (dorks/rocks) can reduce land count slightly but increases flood risk if you cut too far.
* Card draw and looting change how punishing flood/screw feel—do not copy a land count from a deck with different draw density.

# Related

* [Colored Sources](/mana/colored-sources.md)
* [Fixing and Utility Lands](/mana/fixing-and-utility-lands.md)
* [Category Budgets](/commander/category-budgets.md)
* [The Basics of Mana](/references/wizards-basics-of-mana.md)

[^wiz-mana]: The Basics of Mana
[^karsten-sources]: How Many Sources (2022)
[^karsten-edh]: Commander Curve and Ramp
