---
type: Format Guide
title: Category Budgets
description: Target counts for ramp, card draw, interaction, and win conditions in Commander.
tags: [mtg, deckbuilding, commander, budgets]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:20:00Z }
sources:
  - id: cz-template
    resource: /references/command-zone-deckbuilding-template.md
    title: Command Zone Deckbuilding Template
  - id: edhrec-build
    resource: /references/edhrec-how-to-build-commander.md
    title: How to Build a Commander Deck
  - id: karsten-edh
    resource: /references/karsten-commander-curve.md
    title: Commander Curve and Ramp
  - id: karsten-sources
    resource: /references/karsten-colored-sources.md
    title: How Many Sources (2022)
  - id: goldfish-checklist
    resource: /references/mtggoldfish-deckbuilding-checklist.md
    title: Deckbuilding Checklist (MTGGoldfish)
  - id: mtgedh-skeleton
    resource: /references/mtgedh-build-without-cutting-lands.md
    title: Build Without Cutting Lands First
  - id: 341-build
    resource: /references/threeforone-commander-build-guide.md
    title: How to Build a Commander Deck (Three for One Trading)
---

# Definition

**Category budgets** allocate the 99 across fixed functional roles—lands, ramp, draw, disruption, win conditions—so singleton variance does not leave you without mana, cards, or answers.

Exact numbers vary by power level and strategy; treat the following as starting ranges, then tune.[^cz-template][^edhrec-build][^goldfish-checklist]

This page is the **fixed-category template** view. For themed clusters you name and swap as units (Big Spells, Storm, finishers), see [Packages](/commander/packages.md).[^341-build]

# Starting ranges (common community baselines)

Command Zone–style diagnostic template (tune deliberately):[^cz-template]

* **Lands**: roughly **~36–38** (Karsten’s curve/ramp work still informs whether rocks replace or supplement lands).[^karsten-edh][^mtgedh-skeleton]
* **Ramp**: roughly **~8–12** (rocks, dorks, land ramp)—more for expensive commanders; some checklists target ~**50** total mana sources (lands + ramp).[^edhrec-build][^goldfish-checklist]
* **Card advantage / velocity**: roughly **~10–12** dedicated draw or selection engines.[^cz-template][^goldfish-checklist]
* **Targeted disruption**: roughly **~10–12** spot removal, counters, and hate (budget floors can start lower, e.g. ~6, then raise).[^cz-template][^goldfish-checklist]
* **Mass disruption**: roughly **~3–6** board wipes / sweepers.[^cz-template][^edhrec-build]
* **Plan cards**: remaining slots (~**30**) for enablers, payoffs, and **win conditions**—include enough closers that you are not hoping for a single card.[^cz-template][^edhrec-build][^mtgedh-skeleton]

Assign each card a primary role; multi-role cards free plan slots.[^edhrec-build]

Colored source needs still apply at 99-card scale—see Karsten’s tables and [Pip Distribution](/mana/pip-distribution.md).[^karsten-sources]

# Related framings

* **[Packages](/commander/packages.md)** — ~eight themed packages of ~eight cards; evaluate and iterate at package granularity.[^341-build]
* **[8-by-8 EDH](/references/eight-by-eight-edh.md)** — recipe of primary mandatory strategies vs secondary spice before shopping for pets.

Use category budgets as a health check even when you build primarily in packages: thin ramp/draw/interaction packages still fail the same way thin category counts do.

# Related

* [Packages](/commander/packages.md)
* [Land Counts](/mana/land-counts.md)
* [Pip Distribution](/mana/pip-distribution.md)
* [Cutting Cards](/process/cutting-cards.md)
* [Archidekt](/resources/archidekt.md)
* [Ramp](/archetypes/ramp.md)
* [Command Zone Deckbuilding Template](/references/command-zone-deckbuilding-template.md)
* [Deckbuilding Checklist (MTGGoldfish)](/references/mtggoldfish-deckbuilding-checklist.md)
* [How to Build a Commander Deck (Three for One Trading)](/references/threeforone-commander-build-guide.md)

[^cz-template]: Command Zone Deckbuilding Template
[^edhrec-build]: How to Build a Commander Deck
[^karsten-edh]: Commander Curve and Ramp
[^karsten-sources]: How Many Sources (2022)
[^goldfish-checklist]: Deckbuilding Checklist (MTGGoldfish)
[^mtgedh-skeleton]: Build Without Cutting Lands First
[^341-build]: How to Build a Commander Deck (Three for One Trading)
