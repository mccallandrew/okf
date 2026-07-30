---
type: Rule Concept
title: Layers
description: Ordered system for applying continuous effects to characteristics.
tags: [mtg, effects, layers]
status: stable
generated: { by: okf-seed-agent/composer, at: 2026-07-29T03:58:00Z }
sources:
  - id: cr
    resource: /references/comprehensive-rules.md
    title: Magic Comprehensive Rules
  - id: cr-613
    resource: /references/comprehensive-rules.md
    title: "CR 613 Interaction of Continuous Effects"
---

# Definition

**Layers** define the order in which continuous effects apply when determining an object's characteristics.[^cr-613]

# Layer order (summary)

1. Copy effects
2. Control-changing effects
3. Text-changing effects
4. Type-changing effects
5. Color-changing effects
6. Ability-adding/removing effects
7. Power/toughness effects (sublayers: CDA, setting, modifying, counters, effects that switch P/T)

# Within a layer

* **Timestamp order** — among effects in the same layer (or P/T sublayer) that do not depend on each other, apply earlier timestamps first, then later ones.
* **Dependency** — if applying effect A would change what effect B applies to or how B applies, and not vice versa (or other CR dependency cases), apply the independent effect first even if its timestamp is later.
* Effects that generate continuous effects still “exist” from their timestamps; layers only order *application* when determining current characteristics.

# Power/toughness sublayers (layer 7)

Apply in this order inside layer 7:

1. Characteristic-defining abilities (CDA) that set P/T
2. Effects that set power and/or toughness to a specific value
3. Effects that modify power and/or toughness (including +N/+N from Auras/Equipment that aren’t counters)
4. Power and toughness changes from counters
5. Effects that switch power and toughness

# Dependency example

If effect A says “all Goblins get +1/+1” and effect B says “this creature becomes a Goblin,” B is applied first when determining whether A applies to that creature — even if A has an earlier timestamp — because A depends on B.

# Related

* [Continuous Effects](/effects/continuous-effects.md)
* [Text-Changing Effects](/effects/text-changing-effects.md)
* [Objects](/foundations/objects.md)
* [Permanents](/foundations/permanents.md)
* [Characteristics](/foundations/characteristics.md)

[^cr]: Magic Comprehensive Rules
[^cr-613]: CR 613 Interaction of Continuous Effects
