---
type: Rule Concept
title: Drawing a Card
description: Moving the top card of a library into its owner's hand, and what counts as a draw.
tags: [mtg, foundations, draw]
status: stable
generated: { by: okf-complete-agent/composer, at: 2026-07-29T05:00:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-121
    resource: /references/comprehensive-rules.md
    title: "CR 121 Drawing a Card"
---

# Definition

To **draw a card**, a player puts the top card of their [library](/zones/library.md) into their [hand](/zones/hand.md). Drawing is a defined game action; many abilities trigger on or replace draws.[^cr-121]

# Rules

* If an effect instructs a player to draw multiple cards, that is that many individual draw events in sequence (unless an effect says otherwise).
* Putting a card into a hand by another instruction (search, return, look-and-put) is **not** a draw unless the instruction uses the word "draw."
* Attempting to draw from an empty library is a [state-based action](/foundations/state-based-actions.md) that causes that player to lose the game (after the attempted draw fails).
* The active player draws one card during their [draw step](/turn/draw-step.md) as a turn-based action (skipped on the first player's first turn in a two-player game).
* Replacement effects can modify draws (for example "if you would draw a card, … instead").

# Related

* [Library](/zones/library.md)
* [Hand](/zones/hand.md)
* [Draw Step](/turn/draw-step.md)
* [State-Based Actions](/foundations/state-based-actions.md)
* [Winning and Losing](/foundations/winning-and-losing.md)
* [Replacement Effects](/effects/replacement-effects.md)

[^cr]: Magic Comprehensive Rules
[^cr-121]: CR 121 Drawing a Card
