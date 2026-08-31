#!/usr/bin/env python3
"""Regenerate COVERAGE.md from the threats: frontmatter across this folder.

Usage:  python3 make_coverage.py
Reads:  THREATS.md for the vocabulary, *.md for submissions
Writes: COVERAGE.md
"""
import re, pathlib, collections

here = pathlib.Path(__file__).parent
vocab, family = [], {}
current = None
for line in (here / "THREATS.md").read_text().splitlines():
    if line.startswith("## "):
        current = line[3:].strip()
    m = re.match(r"\|\s*`([a-z0-9-]+)`\s*\|\s*([^|]+?)\s*\|", line)
    if m:
        vocab.append(m.group(1))
        family[m.group(1)] = (current, m.group(2))

used = collections.defaultdict(list)
for f in sorted(here.glob("*.md")):
    if f.name in {"THREATS.md", "README.md", "COVERAGE.md", "_TEMPLATE.md"}:
        continue
    text = f.read_text()
    fm = text.split("---")[1] if text.startswith("---") else ""
    block = re.search(r"threats:\s*\n((?:\s*-\s*\S+\n)+)", fm)
    if block:
        for slug in re.findall(r"-\s*([a-z0-9-]+)", block.group(1)):
            used[slug].append(f.stem)

rows, gaps = [], []
for slug in vocab:
    fam, name = family[slug]
    cases = used.get(slug, [])
    rows.append((fam, slug, name, cases))
    if not cases:
        gaps.append((fam, slug, name))

out = ["# Coverage index", "",
       "Generated from the `threats:` frontmatter across this folder. Run",
       "`python3 make_coverage.py` after merging a submission.", "",
       f"**{len(vocab) - len(gaps)} of {len(vocab)} threats have a worked use case.**", ""]

if gaps:
    out += ["## Threats with no use case yet", "",
            "These are where a submission helps most.", "",
            "| Family | Threat | |", "|---|---|---|"]
    out += [f"| {fam} | `{slug}` | {name} |" for fam, slug, name in gaps]
    out += [""]

out += ["## Full index", "", "| Family | Threat | Use cases |", "|---|---|---|"]
for fam, slug, name, cases in rows:
    out.append(f"| {fam} | `{slug}` | {', '.join(cases) if cases else '—'} |")

(here / "COVERAGE.md").write_text("\n".join(out) + "\n")
print(f"{len(vocab) - len(gaps)}/{len(vocab)} threats covered")
