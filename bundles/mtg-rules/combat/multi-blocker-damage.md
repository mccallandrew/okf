---
type: Game Procedure
title: Multi-Blocker Damage
description: How combat damage is divided when multiple creatures block one attacker.
tags: [mtg, combat, combat-damage, blockers]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-510
    resource: /references/comprehensive-rules.md
    title: "CR 510 Combat Damage Step"
  - id: cr-702-2
    resource: /references/comprehensive-rules.md
    title: "CR 702.2 Deathtouch"
  - id: cr-702-19
    resource: /references/comprehensive-rules.md
    title: "CR 702.19 Trample"
---

# Definition

When two or more creatures block the same attacker, that attacker’s controller **assigns combat damage among those blockers**, divided as they choose, during the combat damage step. There is no damage-assignment order.[^cr-510]

# Rules

* Assignment happens as a turn-based action at the start of the combat damage step; damage is then dealt simultaneously — no player gets priority between assignment and dealing.
* An attacker blocked by multiple creatures may put any amounts of its power on any of those blockers (all on one, split evenly, or any other split of whole numbers).
* A blocker that blocks multiple attackers likewise divides its damage among those attackers as its controller chooses.
* Without trample, a blocked attacker assigns damage only to its blockers — none to the player, planeswalker, or battle being attacked.
* With [trample](/keywords/trample.md), lethal damage must be assigned to every blocker before any excess can go through to the attack destination.[^cr-702-19]
* With [deathtouch](/keywords/deathtouch.md), any nonzero combat damage assigned to a creature counts as lethal for that excess check — so 1 per blocker can be enough before trampling over.[^cr-702-2]
* First strike and double strike still use this division in each combat damage step that includes the attacker; blockers removed before the normal step are no longer assigned damage in that later step.

# Related

* [Combat Damage](/combat/combat-damage.md)
* [Declare Blockers](/combat/declare-blockers.md)
* [Trample](/keywords/trample.md)
* [Deathtouch](/keywords/deathtouch.md)
* [First Strike](/keywords/first-strike.md)
* [Double Strike](/keywords/double-strike.md)
* [Damage](/combat/damage.md)

[^cr]: Magic Comprehensive Rules
[^cr-510]: CR 510 Combat Damage Step
[^cr-702-2]: CR 702.2 Deathtouch
[^cr-702-19]: CR 702.19 Trample
