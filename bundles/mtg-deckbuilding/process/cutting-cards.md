---
type: Playbook
title: Cutting Cards
description: Deciding what leaves the list when something better needs a slot.
tags: [mtg, deckbuilding, process, cuts]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:20:00Z }
sources:
  - id: edhrec-upgrade
    resource: /references/edhrec-anatomy-of-upgrade.md
    title: Anatomy of an Upgrade
  - id: wiz-curve
    resource: /references/wizards-mana-curve.md
    title: How to Build a Mana Curve
  - id: flores-threat
    resource: /references/flores-threat-answer.md
    title: Threat Theory, Answer Theory
  - id: mtgedh-skeleton
    resource: /references/mtgedh-build-without-cutting-lands.md
    title: Build Without Cutting Lands First
  - id: goldfish-checklist
    resource: /references/mtggoldfish-deckbuilding-checklist.md
    title: Deckbuilding Checklist (MTGGoldfish)
---

# Definition

**Cutting** is removing cards that overlap roles, break the curve, or fail testing so stronger or more necessary cards can enter.

# Guidelines

* Cut cards that do not serve the [game plan](/foundations/game-plan.md), even if they are powerful in other decks.[^flores-threat]
* Prefer cutting from **overloaded curve slots** (too many fours) before cutting unique roles.[^wiz-curve]
* When two cards share a role, keep the one that is better on-curve or in expected matchups.
* Prefer **like-for-like** swaps (same card type / role) and keep net average mana value flat or lower when upgrading.[^edhrec-upgrade]
* Do not default to cutting lands for new toys—pair adds with intentional role cuts; under-manning mana is the classic brew trap.[^edhrec-upgrade][^mtgedh-skeleton][^goldfish-checklist]
* Resist “pet cards” that win spectacularly in 5% of games but dilute the other 95%.
* In singleton formats, cut the weakest card in an over-stocked category (e.g. 15th ramp spell).

# Related

* [Mana Curve Construction](/mana/mana-curve-construction.md)
* [Consistency and Redundancy](/foundations/consistency-and-redundancy.md)
* [Category Budgets](/commander/category-budgets.md)
* [Anatomy of an Upgrade](/references/edhrec-anatomy-of-upgrade.md)

[^edhrec-upgrade]: Anatomy of an Upgrade
[^wiz-curve]: How to Build a Mana Curve
[^flores-threat]: Threat Theory, Answer Theory
[^mtgedh-skeleton]: Build Without Cutting Lands First
[^goldfish-checklist]: Deckbuilding Checklist (MTGGoldfish)
