# OKF — Magic: The Gathering Knowledge Bundles

This repository holds **Magic: The Gathering** knowledge as [Open Knowledge Format (OKF)](SPEC.md) bundles: directories of markdown concepts with YAML frontmatter, meant to be read by people and agents alike.

## What's here

| Path | Contents |
| --- | --- |
| [`SPEC.md`](SPEC.md) | OKF v0.2 specification |
| [`bundles/mtg-rules/`](bundles/mtg-rules/) | Comprehensive Rules–oriented concept graph (zones, turn structure, keywords, glossary, …) |
| [`bundles/mtg-deckbuilding/`](bundles/mtg-deckbuilding/) | Deck construction and strategy (foundations, mana, archetypes, Limited, Commander, …) |

Each bundle is self-contained: start at its `index.md`, follow linked concepts, and use `log.md` for change history.

## Format

OKF is intentionally minimal—no schema registry or required tooling. If you can `cat` a file and `git clone` a repo, you can consume these bundles. See [`SPEC.md`](SPEC.md) for the full format definition.
