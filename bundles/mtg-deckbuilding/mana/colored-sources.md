---
type: Strategy Concept
title: Colored Sources
description: How many sources of each color you need to cast spells on curve consistently.
tags: [mtg, deckbuilding, mana, colored-sources]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:00:00Z }
sources:
  - id: karsten-sources
    resource: /references/karsten-colored-sources.md
    title: How Many Sources (2022)
  - id: wiz-mana
    resource: /references/wizards-basics-of-mana.md
    title: The Basics of Mana
---

# Definition

A **colored source** is a card that can produce a given color of mana in time to cast a spell on curve. Frank Karsten’s tables target roughly **90%** on-curve castability given deck size, pip count, and assumed land totals.[^karsten-sources]

This concept summarizes the idea; use the [full reference](/references/karsten-colored-sources.md) for detailed tables.

# Guidelines (60-card intuition)

Approximate sources for ~90% on-curve casts (illustrative; verify against Karsten for decisions):[^karsten-sources]

* Turn-one single pip (`C`): on the order of **14** sources.
* Turn-two double pip (`CC`): on the order of **21** sources.
* Turn-three double pip (`1CC`): on the order of **18** sources.
* Later single-pip costs need fewer sources than early ones.

40-card and 99-card decks have their own columns—do not reuse 60-card numbers unchanged.[^karsten-sources]

# What counts as a source?

* Dual lands usually count for both colors when untapped on time.
* Fetch lands count when they can find the color.
* Filter lands, pain lands, and tapped duals depend on timing.
* Mana dorks/rocks count only if they are reliably in play by the turn you need them.

# Related

* [Land Counts](/mana/land-counts.md)
* [Fixing and Utility Lands](/mana/fixing-and-utility-lands.md)
* [Consistency and Redundancy](/foundations/consistency-and-redundancy.md)
* [How Many Sources (2022)](/references/karsten-colored-sources.md)

[^karsten-sources]: How Many Sources (2022)
[^wiz-mana]: The Basics of Mana
