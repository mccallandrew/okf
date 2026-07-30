---
type: Step
title: Combat Damage
description: Step where attacking and blocking creatures assign and deal combat damage.
tags: [mtg, combat, combat-damage]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-510
    resource: /references/comprehensive-rules.md
    title: "CR 510 Combat Damage Step"
---

# Definition

In the **combat damage step**, creatures assign combat damage, then that damage is dealt simultaneously.[^cr-510]

# Rules

* Unblocked attackers assign damage to the player, planeswalker, or battle they are attacking.
* Blocked attackers assign damage among blocking creatures (and excess with trample).
* Blockers assign damage to the attackers they block.
* First strike / double strike create an additional combat damage step before the normal one for creatures with those abilities.

# Interactions

* **First / double strike** — Only creatures with first strike or double strike assign and deal combat damage in the first combat damage step. Creatures that survive may deal damage again (double strike) or for the first time (no first strike) in the normal step.
* **Multi-block** — The attacker’s controller divides damage among blockers as they choose (no ordered blocking). See [Multi-Blocker Damage](/combat/multi-blocker-damage.md).
* **Trample** — Lethal damage must be assigned to each blocker before excess can be assigned to the player, planeswalker, or battle.
* **Deathtouch** — Any nonzero combat damage from a deathtouch source is lethal for toughness and for trample’s “lethal” check, so 1 damage per blocker can open a trampling path.
* Combined case: a first-strike deathtouch trampler can kill blockers in the first strike step and assign remaining damage (including trample excess) according to which creatures still block in each damage step.

# Related

* [Damage](/combat/damage.md)
* [Multi-Blocker Damage](/combat/multi-blocker-damage.md)
* [Trample](/keywords/trample.md)
* [First Strike](/keywords/first-strike.md)
* [Double Strike](/keywords/double-strike.md)
* [Deathtouch](/keywords/deathtouch.md)

[^cr]: Magic Comprehensive Rules
[^cr-510]: CR 510 Combat Damage Step
