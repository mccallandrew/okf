---
type: Reference
title: How Many Sources Do You Need (2022 Update)
description: Frank Karsten's hypergeometric guidelines for colored mana sources by pip count and deck size.
resource: https://www.tcgplayer.com/content/article/How-Many-Sources-Do-You-Need-to-Consistently-Cast-Your-Spells-A-2022-Update/dc23a7d2-0a16-4c0b-ad36-586fcca03ad8/
tags: [mtg, deckbuilding, mana, math, source]
status: stable
generated: { by: okf-deckbuilding-agent/composer, at: 2026-07-29T13:00:00Z }
author: human:frank-karsten
---

# Overview

Frank Karsten’s updated tables for how many **colored mana sources** a deck needs to cast spells on curve with roughly **90%** consistency, across 40-, 60-, 80-, and 99-card decks. Method uses simulation / hypergeometric assumptions about land counts and mulligans.[^karsten-sources]

This bundle summarizes rules of thumb; consult the article for full tables and methodology.

# Key takeaways

* Earlier, more pips → more sources (e.g. turn-one `C` needs more sources than a late `5C`).
* Double and triple pips (e.g. `1CC`, `CC`) demand substantially more sources than single-pip costs at the same turn.
* Numbers assume typical land counts for the deck size; extreme land counts change the picture.
* Treat “sources” carefully: duals, fetches, dorks, and filter lands may or may not count depending on when they produce the color.

# Related

* [Colored Sources](/mana/colored-sources.md)
* [Land Counts](/mana/land-counts.md)
* [Commander Curve and Ramp (Karsten)](/references/karsten-commander-curve.md)

[^karsten-sources]: How Many Sources Do You Need to Consistently Cast Your Spells? A 2022 Update
