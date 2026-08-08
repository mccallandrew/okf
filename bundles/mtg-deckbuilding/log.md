# Directory Update Log

## 2026-08-07
* **Update**: Relocated external tools catalog from `resources/` to `builder-resources/` (freeing `resources/` for a future game-resources taxonomy); retargeted absolute links and `gen_effects.py` Scryfall provenance.
* **Update**: Moved effects generator and taxonomy to repo-root `tools/mtg-deckbuilding/` (`gen_effects.py`, `effects_taxonomy.yaml`); bundle still owns generated `effects/`.
* **Update**: Effects taxonomy P0 — added leaves `spell/cost-bypass`, `spell/cast-from-nonhand`, `zone/cheat-into-play`, `zone/battlefield-to-library`; documented exile triad and gains/gives routing; expanded noise rules (unique-*, synergy-pw-*, creature-type cohorts, UB naming, product helpers, format-eval); regenerated Effects tree (~1.3k tags).
* **Update**: Restructured [Effects](/effects/) onto an OKF taxonomy (`resource/`, `zone/`, `permanent/`, `spell/`, `interaction/`, `combat/`, `synergy/`, `game/`) via taxonomy YAML; filesystem paths are categorical; Scryfall parents remain Related links. Regenerated ~1.2k `Oracle Tag` concepts with `type: Effect Category` hubs.
* **Creation**: Added [Effects](/effects/) — deckbuilding-relevant Scryfall oracle-tag concept tree (`type: Oracle Tag`, ~1.2k tags) generated via `tools/mtg-deckbuilding/gen_effects.py`; added [Scryfall Oracle Tags](/references/scryfall-oracle-tags.md); wired root index, Scryfall resource, and hub cross-links. Tags omitted from the tree are dumped to repo `tmp/excluded` on regenerate.

## 2026-08-03
* **Update**: Ingested Ben Guilfoyle’s Three for One Trading Commander build guide (`references/threeforone-commander-build-guide.md`). Added concepts for [top-down vs bottom-up](/process/top-down-vs-bottom-up.md), [deck vision](/commander/deck-vision.md), [packages](/commander/packages.md), [pip distribution](/mana/pip-distribution.md), and [local meta](/commander/local-meta.md); split package methodology out of category budgets; wired commander selection, synergy, process, mana, formats, Scryfall, and 8-by-8 cross-links.
* **Update**: Ingested Draftsim’s 27 EDH archetypes under `archetypes/commander/` (folder per archetype, `type: Example Deck` lists, graveyard sub-archetypes), added `references/draftsim-edh-archetypes.md`, and wired macros, commander/format hubs, and root scope for attributed illustrative decks.

## 2026-07-29
* **Update**: Ingested six additional Commander sources under references/ (MTGGoldfish checklist, Draftsim tips, EDHREC threat assessment / misrepresenting power, MTG EDH skeleton build, 8-by-8 recipe) and wired them into commander/, formats/commander-overview, foundations/threats-and-answers, and process concepts.
* **Update**: Ingested six Commander-focused sources under references/ (WotC brackets, Command Zone template, EDHREC how-to-build / synergy-vs-exploiting / anatomy-of-upgrade, MTG Salvation first-deck walkthrough) and wired them into commander/, formats/commander-overview, and process cutting/iteration concepts.
* **Initialization**: Seeded the Magic: The Gathering deckbuilding concept graph (foundations, process, mana, archetypes, formats, limited, commander) with cited guides under references/ and external tools under resources/.
