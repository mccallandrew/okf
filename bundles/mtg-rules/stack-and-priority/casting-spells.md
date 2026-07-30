---
type: Game Procedure
title: Casting Spells
description: The process of proposing a spell, choosing modes and targets, and paying costs.
tags: [mtg, stack, casting]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-601
    resource: /references/comprehensive-rules.md
    title: "CR 601 Casting Spells"
---

# Definition

**Casting a spell** moves a card (or copy) onto the stack as a spell, chooses required options, and pays its costs.[^cr-601]

# Outline

Casting follows CR 601 checkpoints (summarized):

1. **Propose / announce** — announce the spell and move the card (or copy) onto the [stack](/zones/stack.md). Verify it can legally be cast (timing, zone, restrictions).
2. **Choices** — choose [modes](/stack-and-priority/modal-spells.md), value of X, [targets](/stack-and-priority/targets.md), and other required choices; check that chosen targets are legal.
3. **Determine cost** — compute the total cost from mana cost plus additional costs, alternate costs, cost increases/reductions, and similar modifiers.
4. **Pay** — activate [mana abilities](/foundations/mana-abilities.md) if needed, then pay the total cost. If you can’t, the cast is illegal and is rewound.
5. **Become cast** — the spell is now cast; relevant abilities may trigger. The casting player receives [priority](/turn/priority.md).

# Illegal casts and backup

* If a player proposes an illegal cast (wrong timing, illegal target choice that can’t be fixed, unpaid costs, and so on), the game rewinds the cast: the card returns to the zone it came from, and mana spent is refunded as nearly as possible.[^cr-601]
* See also [Handling Illegal Actions](/foundations/handling-illegal-actions.md) for the general illegal-action framework.
* Once a spell has successfully become cast, later changes (illegal targets on resolution, and so on) are handled by fizzling/targeting rules on the [stack](/zones/stack.md), not by undoing the cast.

# Related

* [Spells](/foundations/spells.md)
* [Modal Spells and Abilities](/stack-and-priority/modal-spells.md)
* [Targets](/stack-and-priority/targets.md)
* [Costs](/foundations/costs.md)
* [Mana](/foundations/mana.md)
* [Resolving](/stack-and-priority/resolving.md)
* [Handling Illegal Actions](/foundations/handling-illegal-actions.md)

[^cr]: Magic Comprehensive Rules
[^cr-601]: CR 601 Casting Spells
