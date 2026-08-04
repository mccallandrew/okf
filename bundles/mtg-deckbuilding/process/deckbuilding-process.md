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
  - id: 341-build
    resource: /references/threeforone-commander-build-guide.md
    title: How to Build a Commander Deck (Three for One Trading)
---

# Definition

A repeatable **deckbuilding process** turns a plan into a legal, testable list without random card stuffing.

# Steps

1. **Choose the plan** — Write the win condition and archetype; see [Game Plan](/foundations/game-plan.md).[^flores-threat][^mtgedh-skeleton] In Commander, start from a [deck vision](/commander/deck-vision.md) and note whether you are building [top-down or bottom-up](/process/top-down-vs-bottom-up.md).[^341-build]
2. **Gather candidates** — Role piles: threats, answers, mana, card selection (use [Scryfall](/resources/scryfall.md) / format tools). Optional: write an [8-by-8](/references/eight-by-eight-edh.md) recipe or name ~[eight packages](/commander/packages.md) before shopping for pets.[^eight-by-eight][^341-build]
3. **Build the skeleton** — In Commander, fill lands/ramp/draw/interaction/finishers (or their packages) before theme flex; do not cut lands to jam cool cards.[^mtgedh-skeleton]
4. **Build the curve** — Lay out on-curve vs off-curve; cut high CMC first.[^wiz-curve]
5. **Build the mana** — Land count, [pip distribution](/mana/pip-distribution.md), colored sources, fixing.
6. **Goldfish** — Confirm early turns and keep rates; see [Goldfishing](/process/goldfishing.md).
7. **Playtest** — Record failures; change one axis (or one package) at a time; see [Testing and Iteration](/process/testing-and-iteration.md).
8. **Sideboard** — Encode plan B and hate; see [Sideboarding](/process/sideboarding.md).

# Format notes

* **Commander**: Vision → commander (lock or discover) → packages → mana → tune against the [local meta](/commander/local-meta.md).[^341-build] Consult [EDHREC](/resources/edhrec.md) after the plan is set, not before—creativity first, then tools.[^341-build]
* **Limited**: Pool → colors → curve → splash; see [Limited Overview](/formats/limited-overview.md).

# Related

* [Top-Down vs Bottom-Up](/process/top-down-vs-bottom-up.md)
* [Packages](/commander/packages.md)
* [Deck Vision](/commander/deck-vision.md)
* [Cutting Cards](/process/cutting-cards.md)
* [Mana Curve Construction](/mana/mana-curve-construction.md)
* [Constructed Overview](/formats/constructed-overview.md)
* [Build Without Cutting Lands First](/references/mtgedh-build-without-cutting-lands.md)
* [How to Build a Commander Deck (Three for One Trading)](/references/threeforone-commander-build-guide.md)

[^wiz-curve]: How to Build a Mana Curve
[^flores-threat]: Threat Theory, Answer Theory
[^mtgedh-skeleton]: Build Without Cutting Lands First
[^eight-by-eight]: 8-by-8 EDH
[^341-build]: How to Build a Commander Deck (Three for One Trading)
