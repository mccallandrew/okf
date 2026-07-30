---
type: Rule Concept
title: State-Based Actions
description: Automatic checks that clean illegal or losing game states without using the stack.
tags: [mtg, foundations, state-based-actions, sba]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-704
    resource: /references/comprehensive-rules.md
    title: "CR 704 State-Based Actions"
---

# Definition

**State-based actions** (SBAs) are game-enforced checks that happen automatically whenever a player would receive [priority](/turn/priority.md). They are not spells or abilities and do not use the [stack](/zones/stack.md).[^cr-704]

# When checked

* SBAs are checked whenever a player would get priority (after turn-based actions and before putting triggered abilities on the stack, as part of the priority sequence).
* If any apply, they all happen simultaneously, then the check repeats until none apply.
* Triggered abilities waiting to go on the stack wait until SBAs have finished cleaning the game state.

# Common SBAs

| Condition | Result |
|-----------|--------|
| A player has 0 or less [life](/combat/life.md) | That player loses the game |
| A player attempted to draw from an empty [library](/zones/library.md) | That player loses the game |
| A creature has toughness 0 or less | It is put into its owner's [graveyard](/zones/graveyard.md) |
| A creature has lethal damage marked on it (and is not [indestructible](/keywords/indestructible.md)) | It is destroyed |
| A [planeswalker](/card-types/planeswalker.md) has 0 loyalty | It is put into its owner's graveyard |
| Two or more legendary permanents with the same name controlled by the same player | See [Legend Rule](/foundations/legend-rule.md) |
| An Aura attached to an illegal object or player | It is put into its owner's graveyard |
| A token in a zone other than the [battlefield](/zones/battlefield.md) | It ceases to exist |
| A copy of a spell in a zone other than the stack | It ceases to exist |

# Grouped families (non-exhaustive)

* **Player loss** — 0 life; drew from empty library; 10 or more poison counters (and similar format-specific loss SBAs).
* **Creature death** — toughness 0 or less; lethal damage (destroyed); deathtouch damage marked as lethal for toughness > 0 cases as defined.
* **Other permanents** — planeswalker with 0 loyalty; battle with 0 defense; illegal Aura/Equipment/Fortification attachments.
* **Uniqueness** — legend rule; world rule; more than one of certain unique designations as listed in CR 704.
* **Tokens and copies** — token not on the battlefield ceases to exist; spell copy not on the stack ceases to exist.
* **Commander** — optional command-zone replacement when a commander would go to the graveyard or exile (variant SBA).

The full CR 704.5 list is authoritative; this table is a playable summary.

# Related

* [Legend Rule](/foundations/legend-rule.md)
* [Priority](/turn/priority.md)
* [Turn-Based Actions](/foundations/turn-based-actions.md)
* [Winning and Losing](/foundations/winning-and-losing.md)
* [Damage](/combat/damage.md)
* [Counters](/foundations/counters.md)
* [Attachments](/foundations/attachments.md)
* [Commander Overview](/multiplayer/commander-overview.md)

[^cr]: Magic Comprehensive Rules
[^cr-704]: CR 704 State-Based Actions
