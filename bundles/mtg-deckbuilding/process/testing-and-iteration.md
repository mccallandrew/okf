---
type: Playbook
title: Testing and Iteration
description: Structured playtesting and disciplined list changes.
tags: [mtg, deckbuilding, process, testing]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:20:00Z }
sources:
  - id: edhrec-upgrade
    resource: /references/edhrec-anatomy-of-upgrade.md
    title: Anatomy of an Upgrade
  - id: flores-beatdown
    resource: /references/flores-whos-the-beatdown.md
    title: Who's the Beatdown?
  - id: flores-threat
    resource: /references/flores-threat-answer.md
    title: Threat Theory, Answer Theory
  - id: edhrec-power
    resource: /references/edhrec-misrepresenting-power.md
    title: Misrepresenting Power
  - id: mtgedh-skeleton
    resource: /references/mtgedh-build-without-cutting-lands.md
    title: Build Without Cutting Lands First
---

# Definition

**Testing** turns anecdotes into evidence. **Iteration** changes the list against recorded failure modes—not against the last loss alone.

# Guidelines

* Log matchups, sideboard plans, and why games were lost (mana, role misassignment, missing answers, slow clock)—one sentence per loss is enough to start.[^flores-beatdown][^flores-threat][^mtgedh-skeleton]
* Change **one axis** at a time when possible (mana, threat density, or hate—not all three).[^mtgedh-skeleton]
* Name the swap type: match [bracket](/commander/power-level-and-brackets.md), replace an under-performer, fix a weakness, or run a deliberate “homework” test card.[^edhrec-upgrade]
* Prefer larger samples against the expected metagame; one viral list is a hypothesis, not proof—check [MTGTop8](/resources/mtgtop8.md) / [MTGGoldfish](/resources/mtggoldfish.md) for Constructed.
* After changes, re-goldfish and retest the previously failing matchup.
* Use pre- and **post-game** Rule 0 in Commander: if a list consistently dominates its claimed band, retune or move brackets rather than blaming “luck.”[^edhrec-power]

# Format notes

* **Limited**: Set knowledge expires; test fundamentals (curve, removal count) more than pet cards.
* **Commander**: Power-band mismatches look like “deck failures”—align [brackets](/commander/power-level-and-brackets.md) before rewriting the 99.

# Related

* [Cutting Cards](/process/cutting-cards.md)
* [Sideboarding](/process/sideboarding.md)
* [Deckbuilding Process](/process/deckbuilding-process.md)

[^edhrec-upgrade]: Anatomy of an Upgrade
[^flores-beatdown]: Who's the Beatdown?
[^flores-threat]: Threat Theory, Answer Theory
[^edhrec-power]: Misrepresenting Power
[^mtgedh-skeleton]: Build Without Cutting Lands First
