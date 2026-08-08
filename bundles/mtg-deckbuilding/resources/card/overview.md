---
type: Game Resource Category
title: Card
description: "Cards as fuel, filtered by the zone that makes them usable."
tags: [mtg, deckbuilding, resources, category, card]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-08-08T04:00:05Z }
---

# Definition

A **card resource** is access to useful cards. Which zone a card sits in determines how you can spend it:

* [Hand](/resources/card/hand/) — immediate options
* [Library](/resources/card/library/) — future draws, tutors, and top-deck plays
* [Graveyard](/resources/card/graveyard/) — recursion, cast-from-GY, and fuel payments
* [Exile](/resources/card/exile/) — impulse windows, haven storage, cast-from-exile

This branch is **not**:

* **[Card Advantage](/foundations/card-advantage.md)** as a strategy essay — that lives in foundations; [Card Advantage](/resources/card/card-advantage.md) here frames it as a countable resource.
* **[Card Effects](/effects/resource/cards/)** / **[Zone Effects](/effects/zone/)** — oracle-tag inventories of effects that *move* or *create* card access (this tree links *to* those tags).
* **[Spell](/resources/spell/)** — cast events and storm counts once a card becomes a spell on the stack.

# Deckbuilding notes

* Separate **quantity** (how many cards) from **quality** (how selectable and on-plan they are). Filtering often beats raw draw.
* Zone strategy is a build choice: fair decks maximize hand; reanimator maximizes graveyard; red impulse and escapology maximize exile windows.
* Do not explode every `impulse-*` / `seek-*` / `tutor-*` subtype into resource leaves—link hubs and representative tags.

# Related

* [Game Resources](/resources/)
* [Card Advantage](/foundations/card-advantage.md)
* [Card Effects](/effects/resource/cards/)
* [Zone Effects](/effects/zone/)
* [Draw](/effects/zone/draw/)
* [Spell](/resources/spell/)
