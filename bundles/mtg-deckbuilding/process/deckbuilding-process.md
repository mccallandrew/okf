---
type: Playbook
title: Deckbuilding Process
description: End-to-end loop from game plan to tested list.
tags: [mtg, deckbuilding, process, playbook]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:00:00Z }
sources:
  - id: wiz-curve
    resource: /references/wizards-mana-curve.md
    title: How to Build a Mana Curve
  - id: flores-threat
    resource: /references/flores-threat-answer.md
    title: Threat Theory, Answer Theory
  - id: mtgedh-skeleton
    resource: /references/mtgedh-build-without-cutting-lands.md
    title: Build Without Cutting Lands First
  - id: eight-by-eight
    resource: /references/eight-by-eight-edh.md
    title: 8-by-8 EDH
---

# Definition

A repeatable **deckbuilding process** turns a plan into a legal, testable list without random card stuffing.

# Steps

1. **Choose the plan** — Write the win condition and archetype; see [Game Plan](/foundations/game-plan.md).[^flores-threat][^mtgedh-skeleton]
2. **Gather candidates** — Role piles: threats, answers, mana, card selection (use [Scryfall](/resources/scryfall.md) / format tools). Optional: write an [8-by-8](/references/eight-by-eight-edh.md) recipe of primary vs secondary strategies first.[^eight-by-eight]
3. **Build the skeleton** — In Commander, fill lands/ramp/draw/interaction/finishers before theme flex; do not cut lands to jam cool cards.[^mtgedh-skeleton]
4. **Build the curve** — Lay out on-curve vs off-curve; cut high CMC first.[^wiz-curve]
5. **Build the mana** — Land count, colored sources, fixing.
6. **Goldfish** — Confirm early turns and keep rates; see [Goldfishing](/process/goldfishing.md).
7. **Playtest** — Record failures; change one axis at a time; see [Testing and Iteration](/process/testing-and-iteration.md).
8. **Sideboard** — Encode plan B and hate; see [Sideboarding](/process/sideboarding.md).

# Format notes

* **Commander**: Start from commander and category budgets; consult [EDHREC](/resources/edhrec.md) after the plan is set, not before.
* **Limited**: Pool → colors → curve → splash; see [Limited Overview](/formats/limited-overview.md).

# Related

* [Cutting Cards](/process/cutting-cards.md)
* [Mana Curve Construction](/mana/mana-curve-construction.md)
* [Constructed Overview](/formats/constructed-overview.md)
* [Build Without Cutting Lands First](/references/mtgedh-build-without-cutting-lands.md)

[^wiz-curve]: How to Build a Mana Curve
[^flores-threat]: Threat Theory, Answer Theory
[^mtgedh-skeleton]: Build Without Cutting Lands First
[^eight-by-eight]: 8-by-8 EDH
