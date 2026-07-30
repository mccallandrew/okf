---
type: Rule Concept
title: Copying
description: Creating a copy of an object or spell and which values the copy inherits.
tags: [mtg, foundations, copying]
status: stable
generated: { by: okf-expand-agent/composer, at: 2026-07-29T04:15:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-707
    resource: /references/comprehensive-rules.md
    title: "CR 707 Copying Objects"
---

# Definition

**Copying** creates a new object (or a copy of a spell on the [stack](/zones/stack.md)) whose **copiable values** match those of another object. Copies are distinct objects; they are not the same physical card.[^cr-707]

# Copiable values

A copy inherits the object's printed (or otherwise copiable) characteristics — typically name, mana cost, color, types, abilities, power/toughness, and similar — as modified by other copy effects. It does **not** copy:

* Counters on the original
* Damage marked on the original
* Non-copy continuous effects (Auras, Equipment, most +N/+N effects, control-changing effects, and so on), unless those effects are themselves copy effects
* Choices made for the original when it entered or resolved, except where the copy effect says otherwise

See [Characteristics](/foundations/characteristics.md).

# Rules

* Copying a permanent usually creates a token that's a copy of that permanent (unless the effect puts a card onto the battlefield as a copy).
* Copying a [spell](/foundations/spells.md) puts a copy of that spell on the stack; the copy can usually be targeted and responded to like any other spell.
* A copy of a spell copies choices made for it when cast (modes, targets, and so on) unless the copy effect says otherwise; you often still choose new targets if the effect allows.
* "Becomes a copy" continuous effects change an existing object's copiable values for as long as the effect lasts.

# Spells vs permanents

* A **copy of a spell** on the stack is itself a spell. It usually copies modes, targets, and other choices; many effects let you choose new targets.
* A **copy of a permanent** is usually a token (unless a card is put onto the battlefield as a copy). Status (tapped/untapped), counters, and noncopy continuous effects are not copied by default.

# Face-down and double-faced

* Copying a [face-down](/card-types/face-down.md) permanent copies the face-down characteristics (typically a 2/2 with no name), not the hidden face, unless the effect says otherwise.
* Copying a [double-faced](/card-types/double-faced-cards.md) permanent or spell copies both faces’ copiable values as appropriate; which face is up can matter for the resulting token or spell.

# Related

* [Objects](/foundations/objects.md)
* [Spells](/foundations/spells.md)
* [Characteristics](/foundations/characteristics.md)
* [Tokens](/card-types/token.md)
* [Face-Down Spells and Permanents](/card-types/face-down.md)
* [Double-Faced Cards](/card-types/double-faced-cards.md)
* [Continuous Effects](/effects/continuous-effects.md)
* [Layers](/effects/layers.md)

[^cr]: Magic Comprehensive Rules
[^cr-707]: CR 707 Copying Objects
