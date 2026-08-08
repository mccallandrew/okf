# Effects

Deckbuilding-relevant Scryfall oracle tags, organized by an OKF effect taxonomy (resource, zone, permanent, spell, interaction, combat, synergy, game). Each leaf concept is an `Oracle Tag` with stable `scryfall_tag_id` and an `otag:` search hint. Scryfall Tagger parents appear under Related, not as filesystem paths.

See [Scryfall Oracle Tags](/references/scryfall-oracle-tags.md). Tags omitted from this tree are listed in the repo `tmp/excluded` dump.

* [Resource Effects](resource/) - Effects that change available resources—mana, cards, life, or board presence.
* [Zone Effects](zone/) - Effects defined by moving or manipulating cards across zones.
* [Permanent Effects](permanent/) - Effects that create, remove, or change permanents on the battlefield.
* [Spell Effects](spell/) - Effects about casting, copying, recasting, costing, or countering spells.
* [Interaction Effects](interaction/) - Answers, hate, taxes, and protective interaction.
* [Combat Effects](combat/) - Combat-relevant evasion, manipulation, and damage.
* [Synergy Effects](synergy/) - Ability shapes and matters-style payoffs.
* [Game Effects](game/) - Win conditions and turn-structure effects.
