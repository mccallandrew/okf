---
type: Format Guide
title: Packages
description: Build and evaluate Commander decks as themed packages (~8×8) instead of 99 isolated cards.
tags: [mtg, deckbuilding, commander, packages, budgets]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-08-03T19:55:00Z }
sources:
  - id: 341-build
    resource: /references/threeforone-commander-build-guide.md
    title: How to Build a Commander Deck (Three for One Trading)
  - id: eight-by-eight
    resource: /references/eight-by-eight-edh.md
    title: 8-by-8 EDH
  - id: cz-template
    resource: /references/command-zone-deckbuilding-template.md
    title: Command Zone Deckbuilding Template
---

# Definition

A **package** is a themed cluster of cards that advances one idea in the deck—ramp, interaction, “whenever you cast…,” storm payoffs, finishers, and so on. Package building treats the 99 as a small set of packages rather than ninety-nine independent choices.[^341-build]

Starting skeleton: **~8 packages × ~8 cards ≈ 64 nonlands + 1 commander + ~35 lands**.[^341-build] Exact sizes grow and shrink in testing.

# Why packages

* Any single Commander card is a needle in a haystack; package-level questions (“Is my removal package good enough?”) are easier to answer than “Is Damnation good here?”[^341-build]
* Packages reveal over- and under-representation of roles and themes.
* Swapping or retiring a **whole package** (e.g. Big Spells → Underworld Breach combo when pivoting toward cEDH) is cleaner than scattered one-card edits.[^341-build]

# Universal vs deck-specific

* **Universal**: ramp, card advantage/selection, interaction—every functional list needs some density (see also [Category Budgets](/commander/category-budgets.md)).[^cz-template]
* **Deck-specific**: Big Spells, Copy, Storm, “whenever you cast…,” Steam Rollers (finishers)—named for *your* vision, not a fixed template.[^341-build]
* **Overlap is good**: a card can sit in more than one package or do double duty (modal interaction that also draws).

Related recipe methodology: [8-by-8 EDH](/references/eight-by-eight-edh.md) emphasizes primary mandatory strategies versus secondary spice before shopping for pets.[^eight-by-eight] Guilfoyle’s framing stresses creative package names and package swaps as the unit of iteration.

# Filling packages

Treat each package like a mini-deck:[^341-build]

* Prefer **interplay between packages** and with the commander over “best card in vacuum.”
* Bucket by *function for this deck*: Galvanic Relay may count as “draw” for Kess even though it does not say “draw a card”; for Niv-Mizzet, Parun you would maximize true draw instead.
* Synergy examples: self-mill as pseudo-draw when the graveyard is a resource; modal and X spells that cast twice under Kess; slow permanent copy effects for battlecruiser pods versus one-shot copy for combo.
* Natural combos that slide into existing packages (Dualcaster Mage + Twinflame) can raise power without a separate “combo” package—or become one when you pivot.

# Tuning packages

After sample games:[^341-build]

1. Diagnose the **failing package** (lots of mana, never find payoffs → grow Big Spells / selection).
2. Allow sizes to drift away from eight; keep the skeleton memorable, not rigid.
3. Replace generic members with flexible multi-role cards that serve several packages.
4. **Retire** packages when goals change; swap in denser win packages rather than nibbling at random slots.

Package tuning turns “a 99-card deck” into roughly “an 8-card deck” for decision-making.[^341-build]

# Related

* [Category Budgets](/commander/category-budgets.md)
* [Deck Vision](/commander/deck-vision.md)
* [Synergy and Goodstuff](/commander/synergy-and-goodstuff.md)
* [Testing and Iteration](/process/testing-and-iteration.md)
* [Cutting Cards](/process/cutting-cards.md)
* [Local Meta](/commander/local-meta.md)
* [8-by-8 EDH](/references/eight-by-eight-edh.md)
* [How to Build a Commander Deck (Three for One Trading)](/references/threeforone-commander-build-guide.md)

[^341-build]: How to Build a Commander Deck (Three for One Trading)
[^eight-by-eight]: 8-by-8 EDH
[^cz-template]: Command Zone Deckbuilding Template
