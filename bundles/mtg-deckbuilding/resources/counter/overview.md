---
type: Game Resource Category
title: Counter
description: "Counters and derived numeric resources on players or permanents."
tags: [mtg, deckbuilding, resources, category, counter]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-08-08T04:03:24Z }
---

# Definition

**Counters** are markers that track numeric or keyword state on permanents or players: +1/+1, loyalty, energy, experience, rad, charge, keyword counters, and many storage types (oil, lore, time, shield). Some “counts” decks care about—especially [Devotion](/resources/counter/devotion.md)—are **derived** from the board rather than stored as counters.

This branch is **not**:

* **[Spell → Counter](/effects/spell/counter/)** — counterspells and stack denial (unrelated naming collision).
* **[Poison](/resources/progress/poison.md)** as a win clock — poison counters are a [progress](/resources/progress/) resource; linked from here for discoverability.
* **Effect inventories** under [Permanent → Modify](/effects/permanent/modify/) (`counters matter`, `gives pp counters`, `counter fuel`, keyword-counter tags)—this tree links *to* those tags.

[Rad Counters](/resources/counter/rad-counters.md) are **dual-homed** with [Privilege → Rad Counters](/resources/privilege/rad-counters.md) (player pressure / designation-like framing).

# Deckbuilding notes

* Separate **player counters** (energy, experience, rad, poison) from **permanent counters** (+1/+1, loyalty, charge, keywords).
* Build produce → pay off → protect: counters matter payoffs need enablers; [hate-counters](/effects/interaction/hate/hate-counters.md) and [prevent put counter](/effects/interaction/hate/prevent-put-counter.md) punish greedy piles.
* Proliferation and doubling multiply *all* kinds you care about—and sometimes kinds you do not.
* Do not explode every keyword-counter subtype or `counter fuel-*` tag into its own resource leaf; link hubs.

# Related

* [Game Resources](/resources/)
* [Permanent Modify Effects](/effects/permanent/modify/)
* [Counters Matter](/effects/permanent/modify/counters-matter.md)
* [Hate-Counters](/effects/interaction/hate/hate-counters.md)
* [Poison](/resources/progress/poison.md)
* [Rad Counters](/resources/counter/rad-counters.md)
* [Rad Counters (privilege)](/resources/privilege/rad-counters.md)
* [Mana](/resources/mana/) (energy is not mana)
* [Spell Counter Effects](/effects/spell/counter/) (counterspells—different concept)
