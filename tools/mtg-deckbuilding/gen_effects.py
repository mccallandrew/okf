#!/usr/bin/env python3
"""Generate bundles/mtg-deckbuilding/effects/ from Scryfall oracle_tags_gen.go + taxonomy YAML."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

# tools/mtg-deckbuilding/gen_effects.py → repo root is parents[1]
TOOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOL_DIR.parents[1]
BUNDLE_ROOT = REPO_ROOT / "bundles" / "mtg-deckbuilding"
EFFECTS_DIR = BUNDLE_ROOT / "effects"
TAXONOMY_PATH = TOOL_DIR / "effects_taxonomy.yaml"
EXCLUDED_PATH = REPO_ROOT / "tmp" / "excluded"
GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
GENERATOR = "okf-deckbuilding-agent/composer"

SEEDS = [
    "removal",
    "ramp",
    "tutor",
    "draw",
    "hate",
    "recursion",
    "reanimate",
    "counterspell",
    "protection",
    "copy",
    "theft",
    "sacrifice outlet",
    "cost reducer",
    "impulse",
    "evasion",
    "bounce",
    "discard",
    "mill",
    "lifegain",
    "burn",
    "anthem",
    "landfall",
    "wheel",
    "wish",
    "regrowth",
    "fog",
    "pillowfort",
    "mana rock",
    "mana dork",
    "cantrip",
    "loot",
    "rummage",
    "scry",
    "surveil",
    "ward",
    "card advantage",
    "pure draw",
    "burst draw",
    "draw engine",
    "extra turn",
    "alternate win condition",
    "alternate loss condition",
    "counters matter",
    "keyword counter",
    "artifact matters",
    "flicker",
    "hand disruption",
    "graveyard fuel",
    "cards in graveyard matter",
    "gives pp counters",
    "modal",
    "lockdown",
    "freeze",
    "tapper",
    "untapper",
    "saboteur",
    "poison mechanics",
    "thingfall",
    "lands matter",
    "power matters",
    "toughness matters",
    "discard outlet",
    "gives evasion",
    "gives haste",
    "damage prevention",
    "life payment",
    "cast on resolution",
    "combat manipulation",
    "attacking matters",
    "attack trigger",
    "activated ability",
    "triggered ability",
    "affinity",
    "convoke",
    "your sacrifice matters",
    "opponent sacrifice matters",
    "tax",
    "mana sink",
    "library manipulation",
    "peek",
    "control changing effects",
    "animate",
    "sweeper",
    "spot removal",
    "multi removal",
    "addendum",
    "adds multiple mana",
    "age matters",
    "aikido",
    "alternate-cost-gain-life",
    "alternate-equip-cost",
    "amount spent matters",
    "animate dead-like",
    "any player ability",
    "any zone color change",
    "any zone type change",
    "armament ability",
    "armoring",
    "artifactify",
    "attacking matters-any",
    "attacking matters-self",
    "auraify",
    "auto buyback",
    "auto equip",
    "balance",
    "battalion",
    "battle cry",
    "becomes changeling",
    "behold",
    "birthing pod",
    "block additional",
    "block unlimited",
    "block when tapped",
    "block without creature",
    "blood moon effect",
    # P0 structural seeds: cost-bypass, cast-from-nonhand, cheat-into-play, tuck
    "cost ignorer",
    "sneak",
    "sneak from library",
    "sneak from command zone",
    "show and tell",
    "castable from nonhand",
    "gives castable from nonhand",
    "tuck",
    "tuck-outlet",
    "haven",
    "imprint",
]

NOISE_EXACT = {
    "cycle",
    "draft signpost",
    "card names",
    "un-set mechanics",
    "un-design",
    "you matter",
    "type errata",
    "deprecated mechanics",
    "staple with set's mechanic",
    "face-commander",
    "alt-commander",
    "typal-creature",
    "hate-typal",
    "synergy-planeswalker",
    "tapland",
    "conditional tapland",
    "anagram",
    "alliteration",
    "art matters",
    "artist matters",
    "watermark matters",
    "vanity card",
    "you make the card",
    "ante matters",
    "name matters",
    "typal coupling",
    "black effect",
    "blue effect",
    "red effect",
    "green effect",
    "white effect",
    "aesthetic counter",
    "french vanilla",
    "vanilla",
    "virtual vanilla",
    "virtual french vanilla",
    # Naming / trivia (not effect roles)
    "punny name",
    "portmanteau",
    "onomatopoeia",
    "misnomer",
    "mob name",
    "three-letter name",
    "tongue twister",
    "single english word name",
    "rhyming name",
    "roman numeral",
    "mathy name",
    "quote name",
    "school name",
    "sports name",
    "real life animal name",
    "game name",
    "magic term name",
    "doctor who episode name",
    "doctor who episode saga",
    "fallout perk name",
    "fallout vault saga",
    "marvel storyline name",
    "creature type name",
    "eponymous",
    "eponymous planeswalker",
    "inscryption achievement",
    "notorious templating",
    "mechanical foreshadow",
    "playtest forecast",
    "fun",
    "fun ruling",
    "meme",
    "flavors of vanilla",
    "noncreature french vanilla",
    "noncreature virtual vanilla",
    "french vanilla aura",
    "french vanilla equipment",
    "vanilla aura",
    "vanilla equipment",
    # Product / packaging helpers
    "cover card",
    "substitute card",
    "front-card",
    "helper card",
    "reminder card",
    "pile card",
    "cross-game card",
    "scene",
    "punchcard",
    "commander set booster cards",
    "planeswalker deck face card",
    "planeswalker deck staples",
    "pwdeck-sidekick",
    "sneaky-self-trigger",
    # Format / construction evaluation (not in-game effects)
    "relentless",
    "stronger in singleton formats",
    "weaker in singleton formats",
    "useless in singleton formats",
    "worse in multiplayer",
    "deck requirement",
    "match points matter",
    "format matters",
    "shares name with a format",
    "shares name with a set",
    "shares name with a mechanic",
    # Provenance / digital-only catalog
    "day zero errata",
    "fulfilled futureshift",
    "digital replacement",
    "digital to paper",
    "digital-only mechanics",
    "legacy",
    # Cross-cutting shape facet (parent of show and tell, etc.)—not an effect role
    "symmetrical",
}

# Catalog uniqueness tags are noise except this functional payoff.
NOISE_UNIQUE_KEEP = {"unique counters matter"}

ROLE_HINTS = {
    "removal": "Primary answers that get permanents off the board.",
    "ramp": "Accelerates mana; core to curves and Commander category budgets.",
    "tutor": "Consistency pieces that find specific cards from the library.",
    "draw": "Card flow; pairs with card-advantage plans.",
    "card advantage": "Net access to more usable cards over time.",
    "hate": "Hate pieces that punish strategies, types, or zones.",
    "recursion": "Reuses graveyard resources; see also reanimate.",
    "reanimate": "Cheats permanents back from the graveyard.",
    "counterspell": "Stack interaction / permission.",
    "protection": "Keeps key permanents alive through interaction.",
    "mill": "Library-as-resource or alternate win plans.",
    "lifegain": "Life as a resource or win-condition enabler.",
    "burn": "Damage-based answers or direct damage plans.",
    "landfall": "Payoff for land drops and ramp.",
    "wheel": "Mass hand replacement; multiplayer politics matter.",
    "wish": "Sideboard / outside-the-game tutors.",
    "mana rock": "Nonland mana acceleration.",
    "mana dork": "Creature-based mana acceleration.",
    "cantrip": "Low-cost card selection that replaces itself.",
    "flicker": "Blink value and ETB reuse.",
    "tax": "Stax-adjacent cost increases.",
    "pillowfort": "Makes attacking you expensive or difficult.",
    "sacrifice outlet": "Enables aristocrats and death-trigger engines.",
    "sweeper": "Mass answers for wide boards.",
    "spot removal": "Efficient single-target answers.",
    "addendum": "Main-phase bonus on instant-speed spells; timing matters for value.",
    "adds multiple mana": "Burst mana production; relevant for big turns and sinks.",
    "aikido": "Redirects or reflects opposing force; pairs with pillowfort and politics.",
    "animate dead-like": "Aura reanimation that sticks to the permanent; classic recursion package.",
    "armoring": "Repeatable toughness pumps; defensive combat math.",
    "auto buyback": "Spells that return themselves for reuse after a condition.",
    "auto equip": "Equipment that snaps on at ETB; lowers equip friction.",
    "balance": "Symmetrical equalization via sac/discard; stax and white-hate package.",
    "battalion": "Payoff for attacking with a critical mass of creatures.",
    "birthing pod": "Sac-to-tutor chain; finds the next permanent by mana value.",
    "blood moon effect": "Nonbasic land hate via type/ability replacement.",
}

MID_TITLES = {
    "resource": "Resource Effects",
    "zone": "Zone Effects",
    "permanent": "Permanent Effects",
    "spell": "Spell Effects",
    "interaction": "Interaction Effects",
    "combat": "Combat Effects",
    "synergy": "Synergy Effects",
    "game": "Game Effects",
    "uncategorized": "Uncategorized",
}


@dataclass
class Tag:
    tid: str
    label: str
    parents: list[str] = field(default_factory=list)
    description: str = ""
    aliases: list[str] = field(default_factory=list)


@dataclass
class Taxonomy:
    taxonomy: dict[str, list[str]]
    descriptions: dict[str, str]
    seed_map: dict[str, str]
    overrides: dict[str, str]


def slugify(label: str) -> str:
    s = label.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def title_from_label(label: str) -> str:
    parts = re.split(r"([\s\-/]+)", label)
    out = []
    for p in parts:
        if re.fullmatch(r"[\s\-/]+", p or ""):
            out.append(p)
        elif p:
            out.append(p[:1].upper() + p[1:])
    return "".join(out) if out else label


def unescape_go_string(s: str) -> str:
    """Decode Go string escapes without corrupting literal UTF-8."""
    out: list[str] = []
    i = 0
    while i < len(s):
        if s[i] != "\\" or i + 1 >= len(s):
            out.append(s[i])
            i += 1
            continue
        nxt = s[i + 1]
        if nxt == "\\":
            out.append("\\")
            i += 2
        elif nxt == '"':
            out.append('"')
            i += 2
        elif nxt == "n":
            out.append("\n")
            i += 2
        elif nxt == "t":
            out.append("\t")
            i += 2
        elif nxt == "u" and i + 5 < len(s):
            hexpart = s[i + 2 : i + 6]
            if re.fullmatch(r"[0-9a-fA-F]{4}", hexpart):
                out.append(chr(int(hexpart, 16)))
                i += 6
            else:
                out.append(s[i])
                i += 1
        elif nxt == "x" and i + 3 < len(s):
            hexpart = s[i + 2 : i + 4]
            if re.fullmatch(r"[0-9a-fA-F]{2}", hexpart):
                out.append(chr(int(hexpart, 16)))
                i += 4
            else:
                out.append(s[i])
                i += 1
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def load_simple_yaml(path: Path) -> dict:
    """Minimal YAML loader for our taxonomy file (maps/lists/scalars)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    root: dict = {}
    stack: list[tuple[int, object]] = [(-1, root)]

    def parse_scalar(raw: str):
        raw = raw.strip()
        if raw == "[]":
            return []
        if (raw.startswith('"') and raw.endswith('"')) or (
            raw.startswith("'") and raw.endswith("'")
        ):
            return raw[1:-1]
        return raw

    for lineno, line in enumerate(lines, 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise ValueError(f"YAML indent error at line {lineno}")
        parent = stack[-1][1]

        if content.startswith("- "):
            if not isinstance(parent, list):
                raise ValueError(f"list item under non-list at line {lineno}")
            parent.append(parse_scalar(content[2:]))
            continue

        if ":" not in content:
            raise ValueError(f"expected key at line {lineno}: {content}")
        key, _, rest = content.partition(":")
        key = key.strip()
        rest = rest.strip()
        if not isinstance(parent, dict):
            raise ValueError(f"mapping entry under non-dict at line {lineno}")

        if rest == "" or rest.startswith("#"):
            # Lookahead: list or dict?
            # Default to dict; if next non-empty is list item at greater indent, use list
            nxt_kind = "dict"
            for look in lines[lineno:]:
                if not look.strip() or look.lstrip().startswith("#"):
                    continue
                li = len(look) - len(look.lstrip(" "))
                if li <= indent:
                    break
                nxt_kind = "list" if look.lstrip().startswith("- ") else "dict"
                break
            child: object = [] if nxt_kind == "list" else {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = parse_scalar(rest)

    return root


def load_taxonomy(path: Path) -> Taxonomy:
    data = load_simple_yaml(path)
    taxonomy = data.get("taxonomy") or {}
    # Normalize leaf lists
    norm: dict[str, list[str]] = {}
    for mid, leaves in taxonomy.items():
        if leaves is None or leaves == []:
            norm[mid] = []
        elif isinstance(leaves, list):
            norm[mid] = list(leaves)
        else:
            raise ValueError(f"taxonomy.{mid} must be a list")
    return Taxonomy(
        taxonomy=norm,
        descriptions=dict(data.get("category_descriptions") or {}),
        seed_map=dict(data.get("seed_map") or {}),
        overrides=dict(data.get("overrides") or {}),
    )


def parse_oracle_tags(path: Path) -> dict[str, Tag]:
    text = path.read_text(encoding="utf-8")
    consts = dict(re.findall(r'TagName(\w+)\s+TagName\s+=\s+"([^"]+)"', text))
    start = text.index("var OracleTagsByLabel")
    map_text = text[start:]
    parts = re.split(r"\n\tTagName(\w+):\s*\{", map_text)
    entries: dict[str, Tag] = {}
    i = 1
    while i < len(parts) - 1:
        const = parts[i]
        body = parts[i + 1]
        end = body.find("\n\t},")
        if end == -1:
            end = body.find("\n}")
        body = body[:end]
        tid_m = re.search(r'ID:\s*"([^"]+)"', body)
        if not tid_m:
            i += 2
            continue
        tid = tid_m.group(1)
        parents: list[str] = []
        pm = re.search(r"ParentIDs:\s*\[\]string\{([^}]*)\}", body)
        if pm:
            parents = re.findall(r'"([^"]+)"', pm.group(1))
        desc = ""
        dm = re.search(r'Description:\s*"((?:\\.|[^"\\])*)"', body)
        if dm:
            desc = unescape_go_string(dm.group(1)).strip()
        aliases: list[str] = []
        am = re.search(r"Aliases:\s*\[\]string\{([^}]*)\}", body)
        if am:
            aliases = re.findall(r'"([^"]+)"', am.group(1))
        label = consts.get(const, const)
        entries[tid] = Tag(
            tid=tid,
            label=label,
            parents=parents,
            description=desc,
            aliases=aliases,
        )
        i += 2
    return entries


def noise_reason(label: str) -> str | None:
    if label in NOISE_EXACT:
        return f"noise-rule:exact:{label}"
    if label.startswith("cycle"):
        return "noise-rule:cycle"
    if "signpost" in label:
        return "noise-rule:draft-signpost"
    if label.startswith("hate-typal"):
        return "noise-rule:hate-typal"
    if label.startswith("typal-"):
        return "noise-rule:typal"
    if label.startswith("synergy-pw-"):
        return "noise-rule:synergy-pw"
    if label.startswith("creature type "):
        return "noise-rule:creature-type-cohort"
    if label.startswith("dnd"):
        return "noise-rule:ub-naming"
    if (
        label.startswith("unique ") or label.startswith("unique-")
    ) and label not in NOISE_UNIQUE_KEEP:
        return "noise-rule:unique-catalog"
    if label.startswith("deprecated "):
        return "noise-rule:deprecated"
    if label.startswith("old ") and (
        "templating" in label or label.startswith("old typeline")
    ):
        return "noise-rule:old-templating"
    if "storyline" in label:
        return "noise-rule:storyline"
    if label.endswith(" effect") and label.split()[0] in {
        "black",
        "blue",
        "red",
        "green",
        "white",
    }:
        return "noise-rule:color-effect"
    if "with set" in label and "mechanic" in label:
        return "noise-rule:set-mechanic"
    if label.startswith("face-commander") or label.startswith("alt-commander"):
        return "noise-rule:commander-face"
    return None


def build_children(entries: dict[str, Tag]) -> dict[str, list[str]]:
    children: dict[str, list[str]] = defaultdict(list)
    for tid, tag in entries.items():
        for p in tag.parents:
            if p in entries:
                children[p].append(tid)
    for kids in children.values():
        kids.sort(key=lambda t: entries[t].label)
    return children


def descendants(tid: str, children: dict[str, list[str]]) -> list[str]:
    out: list[str] = []
    stack = list(children.get(tid, []))
    seen: set[str] = set()
    while stack:
        c = stack.pop()
        if c in seen:
            continue
        seen.add(c)
        out.append(c)
        stack.extend(children.get(c, []))
    return out


def ancestors(tid: str, entries: dict[str, Tag]) -> list[str]:
    out: list[str] = []
    stack = list(entries[tid].parents)
    seen: set[str] = set()
    while stack:
        p = stack.pop()
        if p in seen or p not in entries:
            continue
        seen.add(p)
        out.append(p)
        stack.extend(entries[p].parents)
    return out


def compute_include(
    entries: dict[str, Tag], children: dict[str, list[str]]
) -> tuple[set[str], dict[str, str], list[str]]:
    label_to_id = {t.label: tid for tid, t in entries.items()}
    missing = [s for s in SEEDS if s not in label_to_id]
    include: set[str] = set()
    excluded_noise: dict[str, str] = {}

    for lab in SEEDS:
        if lab not in label_to_id:
            continue
        tid = label_to_id[lab]
        reason = noise_reason(lab)
        if reason:
            excluded_noise[tid] = reason
            continue
        include.add(tid)
        for d in descendants(tid, children):
            r = noise_reason(entries[d].label)
            if r:
                excluded_noise[d] = r
            else:
                include.add(d)
        for a in ancestors(tid, entries):
            r = noise_reason(entries[a].label)
            if r:
                excluded_noise[a] = r
            else:
                include.add(a)

    cleaned: set[str] = set()
    for tid in include:
        r = noise_reason(entries[tid].label)
        if r:
            excluded_noise[tid] = r
        else:
            cleaned.add(tid)
    return cleaned, excluded_noise, missing


def resolve_category(
    tid: str,
    entries: dict[str, Tag],
    tax: Taxonomy,
    memo: dict[str, str],
) -> str:
    if tid in memo:
        return memo[tid]
    label = entries[tid].label
    if label in tax.overrides:
        memo[tid] = tax.overrides[label]
        return memo[tid]
    if label in tax.seed_map:
        memo[tid] = tax.seed_map[label]
        return memo[tid]
    # Walk Scryfall ancestors; first with a mapping wins (prefer shorter / seed_map)
    for a in ancestors(tid, entries):
        alabel = entries[a].label
        if alabel in tax.overrides:
            memo[tid] = tax.overrides[alabel]
            return memo[tid]
        if alabel in tax.seed_map:
            memo[tid] = tax.seed_map[alabel]
            return memo[tid]
    memo[tid] = "uncategorized"
    return memo[tid]


def yaml_quote(s: str) -> str:
    if s == "":
        return '""'
    if re.search(r'[:#\[\]{},&*?|>!%@`"\']', s) or s.strip() != s or "\n" in s:
        esc = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{esc}"'
    return s


def short_description(tag: Tag) -> str:
    if tag.description:
        d = " ".join(tag.description.split())
        if len(d) > 200:
            d = d[:197].rstrip() + "..."
        return d
    return f"Scryfall oracle tag: {tag.label}."


def category_parts(cat: str) -> tuple[str, str | None]:
    if cat == "uncategorized":
        return "uncategorized", None
    mid, _, leaf = cat.partition("/")
    if not leaf:
        return mid, None
    return mid, leaf


def concept_rel_path(tid: str, entries: dict[str, Tag], categories: dict[str, str]) -> str:
    cat = categories[tid]
    mid, leaf = category_parts(cat)
    slug = slugify(entries[tid].label)
    if leaf:
        return f"/effects/{mid}/{leaf}/{slug}.md"
    return f"/effects/{mid}/{slug}.md"


def fs_path_for_concept(
    tid: str, entries: dict[str, Tag], categories: dict[str, str]
) -> Path:
    rel = concept_rel_path(tid, entries, categories)
    return EFFECTS_DIR / rel[len("/effects/") :]


def render_category_overview(path_key: str, title: str, tax: Taxonomy) -> str:
    desc = tax.descriptions.get(
        path_key, f"Deckbuilding effect category: {title}."
    )
    slug = path_key.replace("/", "-")
    return f"""---
type: Effect Category
title: {yaml_quote(title)}
description: {yaml_quote(desc)}
tags: [mtg, deckbuilding, effects, category, {slug}]
status: draft
generated: {{ by: {GENERATOR}, at: {GENERATED_AT} }}
sources:
  - id: scryfall-otags
    resource: /references/scryfall-oracle-tags.md
    title: Scryfall Oracle Tags
---

# Definition

{desc}

# Related

* [Effects](/effects/)
"""


def render_concept(
    tid: str,
    include: set[str],
    children: dict[str, list[str]],
    entries: dict[str, Tag],
    categories: dict[str, str],
) -> str:
    tag = entries[tid]
    title = title_from_label(tag.label)
    desc = short_description(tag)
    slug_tag = slugify(tag.label)
    aliases_yaml = ""
    if tag.aliases:
        aliases_yaml = (
            "\naliases: ["
            + ", ".join(yaml_quote(a) for a in tag.aliases)
            + "]"
        )

    body_def = (
        tag.description.strip()
        if tag.description
        else (
            f"**{title}** is a Scryfall oracle tag used to classify related card effects."
        )
    )

    notes = [
        f"* Search: `otag:{tag.label}` on [Scryfall](/resources/scryfall.md).",
        f"* Category: `{categories[tid]}`.",
    ]
    if tag.label in ROLE_HINTS:
        notes.append(f"* {ROLE_HINTS[tag.label]}")

    related: list[str] = []
    # Scryfall parents (not filesystem parents)
    for p in sorted(
        (x for x in tag.parents if x in include),
        key=lambda x: entries[x].label,
    ):
        ppath = concept_rel_path(p, entries, categories)
        related.append(
            f"* Scryfall parent: [{title_from_label(entries[p].label)}]({ppath})"
        )
    kids = sorted(
        (c for c in children.get(tid, []) if c in include),
        key=lambda c: entries[c].label,
    )
    for c in kids:
        cpath = concept_rel_path(c, entries, categories)
        related.append(f"* [{title_from_label(entries[c].label)}]({cpath})")

    # Category hub link
    mid, leaf = category_parts(categories[tid])
    if leaf:
        related.insert(
            0,
            f"* Category: [{title_from_label(leaf.replace('-', ' '))}](/effects/{mid}/{leaf}/)",
        )
    else:
        related.insert(
            0,
            f"* Category: [{MID_TITLES.get(mid, mid)}](/effects/{mid}/)",
        )

    related_block = "\n".join(related) if related else "* (none)"

    return f"""---
type: Oracle Tag
title: {yaml_quote(title)}
description: {yaml_quote(desc)}
tags: [mtg, deckbuilding, effects, {slug_tag}, oracle-tag]
status: draft
generated: {{ by: {GENERATOR}, at: {GENERATED_AT} }}
scryfall_tag_id: "{tag.tid}"
category: {categories[tid]}{aliases_yaml}
sources:
  - id: scryfall-otags
    resource: /references/scryfall-oracle-tags.md
    title: Scryfall Oracle Tags
  - id: scryfall
    resource: /resources/scryfall.md
    title: Scryfall
---

# Definition

{body_def}

# Deckbuilding notes

{chr(10).join(notes)}

# Related

{related_block}
"""


def render_index(
    title: str,
    intro: str,
    entries_list: list[tuple[str, str, str]],
) -> str:
    lines = [f"# {title}", "", intro.rstrip(), ""]
    for link, t, d in entries_list:
        lines.append(f"* [{t}]({link}) - {d}")
    lines.append("")
    return "\n".join(lines)


def write_tree(
    include: set[str],
    children: dict[str, list[str]],
    entries: dict[str, Tag],
    categories: dict[str, str],
    tax: Taxonomy,
) -> list[str]:
    """Returns list of uncategorized labels (warnings)."""
    if EFFECTS_DIR.exists():
        shutil.rmtree(EFFECTS_DIR)
    EFFECTS_DIR.mkdir(parents=True)

    uncategorized = sorted(
        entries[t].label for t in include if categories[t] == "uncategorized"
    )

    # Write oracle tag concepts (flat under category leaf)
    for tid in include:
        path = fs_path_for_concept(tid, entries, categories)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            render_concept(tid, include, children, entries, categories),
            encoding="utf-8",
        )

    # Group tags by category path
    by_cat: dict[str, list[str]] = defaultdict(list)
    for tid in include:
        by_cat[categories[tid]].append(tid)
    for tids in by_cat.values():
        tids.sort(key=lambda t: entries[t].label)

    # Mid-level hubs
    for mid, leaves in tax.taxonomy.items():
        mid_dir = EFFECTS_DIR / mid
        mid_dir.mkdir(parents=True, exist_ok=True)
        mid_title = MID_TITLES.get(mid, title_from_label(mid.replace("-", " ")))
        mid_desc = tax.descriptions.get(mid, f"{mid_title} category.")
        (mid_dir / "overview.md").write_text(
            render_category_overview(mid, mid_title, tax), encoding="utf-8"
        )

        leaf_listing: list[tuple[str, str, str]] = [
            ("overview.md", mid_title, mid_desc)
        ]
        for leaf in leaves:
            leaf_key = f"{mid}/{leaf}"
            leaf_title = title_from_label(leaf.replace("-", " "))
            leaf_desc = tax.descriptions.get(
                leaf_key, f"{leaf_title} effects."
            )
            leaf_listing.append((f"{leaf}/", leaf_title, leaf_desc))

            leaf_dir = mid_dir / leaf
            leaf_dir.mkdir(parents=True, exist_ok=True)
            (leaf_dir / "overview.md").write_text(
                render_category_overview(leaf_key, leaf_title, tax),
                encoding="utf-8",
            )

            tags_here = by_cat.get(leaf_key, [])
            tag_listing: list[tuple[str, str, str]] = [
                ("overview.md", leaf_title, leaf_desc)
            ]
            for tid in tags_here:
                tag = entries[tid]
                tag_listing.append(
                    (
                        f"{slugify(tag.label)}.md",
                        title_from_label(tag.label),
                        short_description(tag),
                    )
                )
            (leaf_dir / "index.md").write_text(
                render_index(
                    leaf_title,
                    f"Oracle tags under **{leaf_title}** (`{leaf_key}`).",
                    tag_listing,
                ),
                encoding="utf-8",
            )

        # Tags mapped only to mid (no leaf) — rare; list under mid
        mid_only = by_cat.get(mid, [])
        for tid in mid_only:
            tag = entries[tid]
            leaf_listing.append(
                (
                    f"{slugify(tag.label)}.md",
                    title_from_label(tag.label),
                    short_description(tag),
                )
            )

        (mid_dir / "index.md").write_text(
            render_index(
                mid_title,
                f"{mid_desc}\n\nChild categories and any mid-level tags:",
                leaf_listing,
            ),
            encoding="utf-8",
        )

    # Uncategorized bucket if needed
    if uncategorized or "uncategorized" in tax.taxonomy:
        u_dir = EFFECTS_DIR / "uncategorized"
        u_dir.mkdir(parents=True, exist_ok=True)
        u_desc = tax.descriptions.get(
            "uncategorized", "Tags that could not be mapped."
        )
        (u_dir / "overview.md").write_text(
            render_category_overview("uncategorized", "Uncategorized", tax),
            encoding="utf-8",
        )
        u_listing: list[tuple[str, str, str]] = [
            ("overview.md", "Uncategorized", u_desc)
        ]
        for tid in by_cat.get("uncategorized", []):
            tag = entries[tid]
            u_listing.append(
                (
                    f"{slugify(tag.label)}.md",
                    title_from_label(tag.label),
                    short_description(tag),
                )
            )
        (u_dir / "index.md").write_text(
            render_index(
                "Uncategorized",
                "Oracle tags with no taxonomy mapping (should be empty).",
                u_listing,
            ),
            encoding="utf-8",
        )

    # Root effects index — mid-level categories
    root_listing: list[tuple[str, str, str]] = []
    for mid in tax.taxonomy:
        if mid == "uncategorized" and not uncategorized:
            continue
        title = MID_TITLES.get(mid, title_from_label(mid.replace("-", " ")))
        desc = tax.descriptions.get(mid, f"{title}.")
        root_listing.append((f"{mid}/", title, desc))

    intro = (
        "Deckbuilding-relevant Scryfall oracle tags, organized by an OKF "
        "effect taxonomy (resource, zone, permanent, spell, interaction, "
        "combat, synergy, game). Each leaf concept is an `Oracle Tag` with "
        "stable `scryfall_tag_id` and an `otag:` search hint. Scryfall "
        "Tagger parents appear under Related, not as filesystem paths.\n\n"
        "See [Scryfall Oracle Tags](/references/scryfall-oracle-tags.md). "
        "Tags omitted from this tree are listed in the repo `tmp/excluded` dump."
    )
    (EFFECTS_DIR / "index.md").write_text(
        render_index("Effects", intro, root_listing), encoding="utf-8"
    )

    return uncategorized


def write_excluded(
    entries: dict[str, Tag],
    include: set[str],
    excluded_noise: dict[str, str],
) -> int:
    EXCLUDED_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows: list[tuple[str, str, str]] = []
    for tid, tag in entries.items():
        if tid in include:
            continue
        reason = (
            excluded_noise.get(tid)
            or noise_reason(tag.label)
            or "not-in-seed-closure"
        )
        rows.append((tag.label, tid, reason))
    rows.sort(key=lambda r: r[0].lower())
    lines = ["label\tid\treason"] + [f"{a}\t{b}\t{c}" for a, b, c in rows]
    EXCLUDED_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(rows)


def write_manifest(
    source: Path,
    include_count: int,
    excluded_count: int,
    missing_seeds: list[str],
    uncategorized: list[str],
) -> None:
    h = hashlib.sha256(source.read_bytes()).hexdigest()[:16]
    manifest = {
        "source": str(source),
        "source_sha256_16": h,
        "generated_at": GENERATED_AT,
        "included": include_count,
        "excluded": excluded_count,
        "missing_seeds": missing_seeds,
        "uncategorized": uncategorized,
        "taxonomy": str(TAXONOMY_PATH),
    }
    (EFFECTS_DIR / ".generated.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        required=True,
        help="Path to oracle_tags_gen.go",
    )
    parser.add_argument(
        "--taxonomy",
        type=Path,
        default=TAXONOMY_PATH,
        help="Path to effects_taxonomy.yaml",
    )
    args = parser.parse_args()
    source = args.source.resolve()
    if not source.is_file():
        raise SystemExit(f"source not found: {source}")

    tax = load_taxonomy(args.taxonomy.resolve())
    entries = parse_oracle_tags(source)
    children = build_children(entries)
    include, excluded_noise, missing = compute_include(entries, children)

    categories: dict[str, str] = {}
    for tid in include:
        resolve_category(tid, entries, tax, categories)

    uncategorized = write_tree(include, children, entries, categories, tax)
    excluded_count = write_excluded(entries, include, excluded_noise)
    write_manifest(source, len(include), excluded_count, missing, uncategorized)

    from collections import Counter

    cat_counts = Counter(categories[t] for t in include)
    print(f"catalog:   {len(entries)}")
    print(f"included:  {len(include)}")
    print(f"excluded:  {excluded_count} -> {EXCLUDED_PATH}")
    print(f"categories:{len(cat_counts)}")
    for cat, n in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))[:20]:
        print(f"  {n:4d}  {cat}")
    if uncategorized:
        print(f"UNCATEGORIZED ({len(uncategorized)}):")
        for lab in uncategorized[:50]:
            print(f"  - {lab}")
        if len(uncategorized) > 50:
            print(f"  ... and {len(uncategorized) - 50} more")
    else:
        print("uncategorized: 0")
    if missing:
        print(f"missing seeds ({len(missing)}): {', '.join(missing)}")
    print(f"wrote:     {EFFECTS_DIR}")


if __name__ == "__main__":
    main()
