---
type: Rule Concept
title: Legend Rule
description: State-based action that limits legendary permanents with the same name under one player's control.
tags: [mtg, foundations, legend-rule, legendary]
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

The **legend rule** is a [state-based action](/foundations/state-based-actions.md): if a player controls two or more legendary permanents with the same name, that player chooses one of them and the rest are put into their owners' graveyards.[^cr-704]

# Rules

* It checks **name**, not legendary creature type or identity — two different legendary permanents with different names can coexist.
* It is per controller: each player may control their own copy of the same legendary permanent.
* The choice of which to keep is made by the controller as the SBA is applied; the others leave as a state-based action (not destruction, so [indestructible](/keywords/indestructible.md) does not save them).
* Tokens and nontoken legendaries are treated the same for this rule.
* Effects that say "the 'legend rule' doesn't apply" suppress this SBA for the relevant permanents.

# Related

* [State-Based Actions](/foundations/state-based-actions.md)
* [Characteristics](/foundations/characteristics.md)
* [Permanents](/foundations/permanents.md)
* [Planeswalker](/card-types/planeswalker.md)

[^cr]: Magic Comprehensive Rules
[^cr-704]: CR 704 State-Based Actions
