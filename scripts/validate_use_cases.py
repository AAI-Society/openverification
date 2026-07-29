"""Validate the documented Markdown shape of use-case stories.

This is a structural check, not a judgment about tier reasoning, claim truth, or
conformance. Frontmatter support is intentionally limited to the scalar
``key: value`` form used by this repository's template.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
USE_CASES_DIR = REPO_ROOT / "Proof-of-Control" / "use_cases"
EXCLUDED_FILES = {"README.md", "_TEMPLATE.md"}
REQUIRED_FIELDS = ("industry", "use_case", "claimed_tier")
REQUIRED_HEADINGS = (
    "Scenario",
    "Why not one tier down?",
    "Tier by domain",
    "Notes / open questions",
)
DOMAINS = (
    "Provenance",
    "Authorization",
    "Security",
    "Identity",
    "Privacy",
    "Portability",
)
DISCLAIMER = (
    "Illustrative, hypothetical scenario for calibration. Not necessarily "
    "indicative of any specific organization's current state."
)

FIELD_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)$")
CLAIMED_RE = re.compile(r"^##\s+Claimed tier:\s+Tier\s+([1-4])\s*$")
H1_RE = re.compile(r"^#\s+(?!#)(.+?)\s*$")
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
TABLE_DELIMITER_RE = re.compile(r"^:?-+:?$")
COMMENT_RE = re.compile(r"<!--.*?(?:-->|$)", re.DOTALL)
PLACEHOLDER_RE = re.compile(
    r"<(?:sector(?:,[^>]*)?|one line(?::[^>]*)?|1-4|short title[^>]*|N(?:-1)?)>",
    re.IGNORECASE,
)

Error = tuple[int, str]


def is_indented_code(line: str) -> bool:
    """Return whether leading whitespace reaches Markdown's four-column indent."""

    column = 0
    for character in line:
        if character == " ":
            column += 1
        elif character == "\t":
            column += 4 - (column % 4)
        else:
            break
        if column >= 4:
            return True
    return False


def visible_lines(lines: Sequence[str]) -> list[tuple[int, str]]:
    """Return lines that Markdown renders as ordinary content."""

    text = "\n".join(lines)
    text = COMMENT_RE.sub(lambda match: "\n" * match.group().count("\n"), text)
    fence: tuple[str, int] | None = None
    visible: list[tuple[int, str]] = []

    for number, line in enumerate(text.split("\n"), start=1):
        if match := FENCE_RE.match(line):
            marker, trailing = match.groups()
            if fence is None:
                if marker[0] != "`" or "`" not in trailing:
                    fence = marker[0], len(marker)
                    continue
            elif (
                marker[0] == fence[0]
                and len(marker) >= fence[1]
                and not trailing.strip()
            ):
                fence = None
                continue
        if fence is None and not is_indented_code(line):
            visible.append((number, line))
    return visible


def normalize(text: str) -> str:
    return " ".join(text.replace("*", "").replace("_", "").replace("`", "").split())


def blockquote_content(line: str) -> str:
    """Remove one Markdown blockquote marker and its optional following space."""

    stripped = line.lstrip()
    if not stripped.startswith(">"):
        return ""
    content = stripped[1:]
    return content.removeprefix(" ")


def table_cells(line: str) -> tuple[str, str, str] | None:
    if not line.lstrip().startswith("|"):
        return None
    cells = line.strip().strip("|").split("|", 2)
    if len(cells) != 3:
        return None
    return normalize(cells[0]), normalize(cells[1]), normalize(cells[2])


def section(
    visible: Sequence[tuple[int, str]],
    start_line: int,
    *,
    keep_blank: bool = False,
) -> list[tuple[int, str]]:
    body: list[tuple[int, str]] = []
    for number, line in visible:
        if number <= start_line:
            continue
        if line.strip().startswith("## "):
            break
        if keep_blank or line.strip():
            body.append((number, line))
    return body


def parse_frontmatter(
    lines: Sequence[str],
) -> tuple[list[Error], int | None, dict[str, tuple[str, int]]]:
    if not lines or lines[0].lstrip("\ufeff").strip() != "---":
        return [(1, "missing opening frontmatter delimiter '---'")], None, {}
    end = next(
        (i for i, line in enumerate(lines[1:], start=2) if line.strip() == "---"),
        None,
    )
    if end is None:
        return [(1, "frontmatter is missing its closing '---'")], None, {}

    errors: list[Error] = []
    fields: dict[str, tuple[str, int]] = {}
    for number, line in enumerate(lines[1 : end - 1], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = FIELD_RE.match(line)
        if not match:
            errors.append(
                (number, "unsupported frontmatter syntax; expected 'key: scalar'")
            )
            continue
        key, value = match.group(1), match.group(2).strip().strip("'\"").strip()
        if key in fields:
            errors.append((number, f"duplicate frontmatter field '{key}'"))
        else:
            fields[key] = value, number

    for key in REQUIRED_FIELDS:
        if key not in fields:
            errors.append((1, f"missing required frontmatter field '{key}'"))
        elif not fields[key][0]:
            errors.append(
                (fields[key][1], f"frontmatter field '{key}' must not be blank")
            )
    return errors, end, fields


def validate_table(
    visible: Sequence[tuple[int, str]], heading_line: int
) -> list[Error]:
    body = section(visible, heading_line, keep_blank=True)
    header = next(
        (
            i
            for i, (_, line) in enumerate(body)
            if table_cells(line) == ("Domain", "Tier", "Why")
        ),
        None,
    )
    if header is None:
        return [(heading_line, "tier-by-domain Markdown table is missing")]
    header_line = body[header][0]
    if header + 1 >= len(body) or body[header + 1][0] != header_line + 1:
        return [(body[header][0], "domain table separator is missing")]

    separator_line, separator_text = body[header + 1]
    separator = separator_text.strip().strip("|").split("|", 2)
    valid_separator = (
        separator_text.lstrip().startswith("|")
        and len(separator) == 3
        and all(TABLE_DELIMITER_RE.fullmatch(value.strip()) for value in separator)
    )
    if not valid_separator:
        return [(separator_line, "domain table separator is invalid")]

    errors: list[Error] = []
    expected = {domain.casefold(): domain for domain in DOMAINS}
    seen: set[str] = set()
    next_line = separator_line + 1
    for number, line in body[header + 2 :]:
        if number != next_line:
            break
        cells = table_cells(line)
        if cells is None:
            break
        next_line += 1
        domain, tier, reason = cells
        key = domain.casefold()
        if key not in expected:
            errors.append((number, f"unexpected domain row '{domain}'"))
            continue
        name = expected[key]
        if key in seen:
            errors.append((number, f"duplicate domain row '{name}'"))
            continue
        seen.add(key)
        if not re.fullmatch(r"[1-4]", tier):
            errors.append((number, f"{name} tier must be an integer from 1 to 4"))
        if not reason:
            errors.append((number, f"{name} rationale must not be blank"))

    errors.extend(
        (heading_line, f"missing domain row '{domain}'")
        for key, domain in expected.items()
        if key not in seen
    )
    return errors


def validate_file(path: Path) -> list[Error]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        return [(1, f"cannot read UTF-8 Markdown: {error}")]

    errors, frontmatter_end, fields = parse_frontmatter(lines)
    visible = [
        (number, line)
        for number, line in visible_lines(lines)
        if frontmatter_end is None or number > frontmatter_end
    ]
    headings: dict[str, list[int]] = {}
    claimed: list[tuple[int, int | None]] = []
    titles: list[tuple[int, str]] = []

    for number, line in visible:
        stripped = line.strip()
        if match := H1_RE.fullmatch(stripped):
            titles.append((number, normalize(match.group(1))))
        if stripped.startswith("## "):
            heading = stripped[3:].strip()
            headings.setdefault(heading, []).append(number)
            if heading.startswith("Claimed tier:"):
                match = CLAIMED_RE.fullmatch(stripped)
                claimed.append((number, int(match.group(1)) if match else None))

    if len(titles) != 1:
        errors.append((1, "expected exactly one non-placeholder H1 title"))
    elif not titles[0][1] or PLACEHOLDER_RE.search(titles[0][1]):
        errors.append((titles[0][0], "H1 title still contains a placeholder"))

    first_section = min(
        (number for occurrences in headings.values() for number in occurrences),
        default=len(lines) + 1,
    )
    quote_source = [
        blockquote_content(line) if number < first_section else ""
        for number, line in visible
    ]
    quote = " ".join(
        line.strip() for _, line in visible_lines(quote_source) if line.strip()
    )
    if DISCLAIMER not in normalize(quote):
        errors.append(
            (
                (frontmatter_end or 0) + 1,
                "missing the hypothetical-scenario disclaimer before sections",
            )
        )

    heading_lines: dict[str, int] = {}
    for heading in REQUIRED_HEADINGS:
        occurrences = headings.get(heading, [])
        if not occurrences:
            errors.append((1, f"missing required heading '## {heading}'"))
            continue
        heading_lines[heading] = occurrences[0]
        errors.extend(
            (number, f"duplicate required heading '## {heading}'")
            for number in occurrences[1:]
        )

    frontmatter_tier: int | None = None
    if "claimed_tier" in fields:
        value, value_line = fields["claimed_tier"]
        if re.fullmatch(r"[1-4]", value):
            frontmatter_tier = int(value)
        else:
            errors.append((value_line, "claimed_tier must be an integer from 1 to 4"))

    if len(claimed) != 1 or claimed[0][1] is None:
        errors.append(
            (
                claimed[0][0] if claimed else 1,
                "expected one '## Claimed tier: Tier N' heading with N from 1 to 4",
            )
        )
    else:
        number, tier = claimed[0]
        heading_lines["Claimed tier"] = number
        if frontmatter_tier is not None and tier != frontmatter_tier:
            message = (
                f"heading Tier {tier} does not match frontmatter "
                f"claimed_tier {frontmatter_tier}"
            )
            errors.append((number, message))

    for heading in ("Scenario", "Claimed tier", "Why not one tier down?"):
        if heading in heading_lines and not section(visible, heading_lines[heading]):
            errors.append(
                (heading_lines[heading], f"section '## {heading}' must not be blank")
            )

    if "Tier by domain" in heading_lines:
        errors.extend(validate_table(visible, heading_lines["Tier by domain"]))
    for number, line in visible:
        if match := PLACEHOLDER_RE.search(line):
            errors.append(
                (number, f"unresolved template placeholder '{match.group(0)}'")
            )
    return sorted(set(errors))


def collect_story_files(paths: Sequence[Path]) -> list[Path]:
    candidates: list[Path] = []
    for path in paths or (USE_CASES_DIR,):
        candidates.extend(path.rglob("*.md") if path.is_dir() else [path])
    return sorted(
        {
            path.resolve()
            for path in candidates
            if path.suffix.lower() == ".md" and path.name not in EXCLUDED_FILES
        }
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths", nargs="*", type=Path, help="story files or directories"
    )
    stories = collect_story_files(parser.parse_args(argv).paths)
    if not stories:
        print("No use-case story Markdown files found.", file=sys.stderr)
        return 2

    findings = [
        (story, line, message)
        for story in stories
        for line, message in validate_file(story)
    ]
    if findings:
        for path, line, message in findings:
            try:
                path = path.relative_to(REPO_ROOT)
            except ValueError:
                pass
            print(f"{path}:{line}: {message}", file=sys.stderr)
        print(
            f"Found {len(findings)} structural error(s) in {len(stories)} file(s).",
            file=sys.stderr,
        )
        return 1

    noun = "story" if len(stories) == 1 else "stories"
    print(f"Validated the documented shape of {len(stories)} use-case {noun}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
