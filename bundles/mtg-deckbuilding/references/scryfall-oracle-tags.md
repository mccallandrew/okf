---
type: Reference
title: Scryfall Oracle Tags
description: Community Tagger oracle-tag catalog on Scryfall—labels, stable IDs, parent hierarchy, and otag search.
resource: https://scryfall.com/docs/tagger-tags
tags: [mtg, deckbuilding, effects, oracle-tag, source]
status: draft
generated: { by: okf-deckbuilding-agent/composer, at: 2026-08-08T02:00:00Z }
---

# Overview

Scryfall exposes **oracle tags** from the community [Tagger](https://tagger.scryfall.com/) project: functional labels on cards (removal, ramp, tutor, and thousands more) with a parent/child hierarchy. Labels can change; **tag UUIDs are the stable identifiers**. Search with `otag:<label>` on Scryfall.[^scryfall-otags]

This bundle’s [Effects](/effects/) section indexes a **deckbuilding-relevant subset** of that catalog as `Oracle Tag` concepts. OKF **filesystem paths follow a deckbuilding taxonomy** (resource, zone, permanent, spell, interaction, combat, synergy, game); Tagger parent/child links appear under Related. Stable identity remains `scryfall_tag_id`.

# Key takeaways

* Prefer `scryfall_tag_id` in frontmatter when syncing; treat labels as display/search strings.
* Tagger hierarchy is a DAG (multi-parent); OKF paths are taxonomic categories, with Scryfall parents linked under Related.
* Not every Tagger tag is ingested—cycles, draft signposts, typal hate lists, and similar noise are omitted (see repo `tmp/excluded` when regenerating).

# Related

* [Effects](/effects/)
* [Scryfall](/resources/scryfall.md)

[^scryfall-otags]: Scryfall Card Tags / API documentation
