---
type: Game Resource Category
title: Spell
description: "Spells as cast events, stack objects, counts, and copies—not just cards in hand."
tags: [mtg, deckbuilding, resources, category, spell]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-08-08T04:18:53Z }
---

# Definition

A **spell** resource is the act of casting and what exists on the stack: cast events, [spell count](/resources/spell/spell-count.md), [copies](/resources/spell/copies.md), and timing. Distinct from [Card](/resources/card/) (zone access to a card before or after it becomes a spell).

This branch is **not**:

* **Cards in hand/library/graveyard/exile** — [Card](/resources/card/) until cast (or cast-from-zone permissions bridge both).
* **Permanents** after resolution — [Permanent](/resources/permanent/).
* **[Spell Effects](/effects/spell/)** — cast/copy/recast/cost/counter *roles* (this tree links *to* those hubs).
* **Counterspells as answers** — denying *opponent* spells lives under [Spell → Counter](/effects/spell/counter/); your own spell density is still this resource.

# Deckbuilding notes

* Separate **fuel** (cheap cantrips, rituals, free spells) from **payoffs** (storm, magecraft, prowess, cascade).
* Instant-speed spells are a timing resource; sorcery-speed needs protected main phases.
* Do not explode every `copy-*` / `cost-reducer-*` subtype—link hubs.
* Bridge to [Cost Reduction](/resources/mana/cost-reduction.md) and [Alternative Costs](/resources/mana/alternative-costs.md) for paying; this branch owns the cast event itself.

# Related

* [Game Resources](/resources/)
* [Spell Effects](/effects/spell/)
* [Card](/resources/card/)
* [Cast](/effects/spell/cast/)
* [Copy](/effects/spell/copy/)
* [Mana](/resources/mana/)
