from __future__ import annotations

import io
import re
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

from scripts.validate_use_cases import (
    DISCLAIMER,
    DOMAINS,
    REQUIRED_FIELDS,
    USE_CASES_DIR,
    collect_story_files,
    main,
    normalize,
    table_cells,
    validate_file,
    visible_lines,
)

DISCLAIMER_BLOCK = (
    "> *Illustrative, hypothetical scenario for calibration. Not necessarily\n"
    "> indicative of any specific organization's current state.*"
)


def valid_story() -> str:
    return f"""---
industry: testing
use_case: AI agent exercising a documented action
claimed_tier: 3
review_note: extra scalar fields are allowed
---

# Structural validation fixture

{DISCLAIMER_BLOCK}

## Scenario

One actor takes one action with a concrete consequence.

## Claimed tier: Tier 3

The fixture explains its target tier.

## Why not one tier down?

The fixture names the remaining Tier 2 failure.

## Extra context

Additional sections are allowed.

## Tier by domain

| Domain | Tier | Why |
| :--- | :---: | ---: |
| Privacy | 2 | A nonblank rationale. |
| Provenance | 3 | A nonblank rationale. |
| Identity | 2 | A nonblank rationale. |
| Authorization | 3 | A nonblank rationale. |
| Portability | 1 | A nonblank rationale. |
| Security | 3 | A nonblank rationale. |

## Notes / open questions

None.
"""


class ValidateUseCasesTests(unittest.TestCase):
    def findings_for(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "story.md"
            path.write_text(text, encoding="utf-8")
            return [message for _, message in validate_file(path)]

    def test_repository_stories_pass(self) -> None:
        stories = collect_story_files(())
        self.assertTrue(stories)
        for story in stories:
            with self.subTest(story=story):
                self.assertEqual(validate_file(story), [])

    def test_contract_matches_template(self) -> None:
        template = (USE_CASES_DIR / "_TEMPLATE.md").read_text(encoding="utf-8")
        lines = template.splitlines()
        end = lines[1:].index("---") + 2
        fields = tuple(
            match.group(1)
            for line in lines[1 : end - 1]
            if (match := re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):", line))
        )
        self.assertEqual(fields, REQUIRED_FIELDS)

        headings = tuple(
            line.strip()[3:].strip()
            for _, line in visible_lines(lines)
            if line.strip().startswith("## ")
        )
        expected = (
            "Scenario",
            "Claimed tier: Tier <N>",
            "Why not one tier down?",
            "Tier by domain",
            "Notes / open questions",
        )
        self.assertEqual(headings, expected)

        rows = [
            cells[0]
            for line in lines
            if (cells := table_cells(line))
            and cells[0] not in {"Domain", "---------------"}
        ]
        self.assertEqual(tuple(rows), DOMAINS)
        quote = " ".join(line.lstrip()[1:] for line in lines if line.startswith(">"))
        self.assertIn(DISCLAIMER, normalize(quote))

    def test_allows_documented_extensions_and_formatting(self) -> None:
        self.assertEqual(self.findings_for(valid_story()), [])

    def test_ignores_markdown_syntax_in_frontmatter_comments(self) -> None:
        story = valid_story().replace(
            "industry: testing",
            "industry: testing\n# metadata note\n## Scenario",
        )
        self.assertEqual(self.findings_for(story), [])

    def test_reports_frontmatter_errors_and_tier_mismatch(self) -> None:
        cases = {
            "unclosed": (
                valid_story().replace("---\n\n# Structural", "\n# Structural", 1),
                "frontmatter is missing its closing '---'",
            ),
            "syntax": (
                valid_story().replace(
                    "review_note: extra scalar fields are allowed",
                    "- unsupported list value",
                ),
                "unsupported frontmatter syntax",
            ),
            "missing": (
                valid_story().replace(
                    "use_case: AI agent exercising a documented action\n", ""
                ),
                "missing required frontmatter field 'use_case'",
            ),
            "duplicate": (
                valid_story().replace(
                    "industry: testing", "industry: testing\nindustry: duplicate"
                ),
                "duplicate frontmatter field 'industry'",
            ),
            "invalid": (
                valid_story().replace("claimed_tier: 3", "claimed_tier: 5"),
                "claimed_tier must be an integer from 1 to 4",
            ),
            "mismatch": (
                valid_story().replace("claimed_tier: 3", "claimed_tier: 2"),
                "heading Tier 3 does not match frontmatter claimed_tier 2",
            ),
        }
        for name, (story, expected) in cases.items():
            with self.subTest(name=name):
                self.assertTrue(
                    any(expected in message for message in self.findings_for(story))
                )

    def test_requires_visible_disclaimer(self) -> None:
        hidden_versions = (
            f"<!--\n{DISCLAIMER_BLOCK}\n-->",
            f"```\n{DISCLAIMER_BLOCK}\n```",
            f"> ```\n{DISCLAIMER_BLOCK}\n> ````",
            DISCLAIMER_BLOCK.replace("> ", ">     "),
        )
        for replacement in hidden_versions:
            with self.subTest(replacement=replacement):
                story = valid_story().replace(
                    DISCLAIMER_BLOCK,
                    replacement,
                )
                self.assertTrue(
                    any(
                        "missing the hypothetical-scenario disclaimer" in message
                        for message in self.findings_for(story)
                    )
                )

    def test_requires_one_filled_title(self) -> None:
        missing = valid_story().replace("# Structural validation fixture\n", "")
        placeholder = valid_story().replace(
            "# Structural validation fixture", "# <Short title for the use case>"
        )
        self.assertIn(
            "expected exactly one non-placeholder H1 title",
            self.findings_for(missing),
        )
        self.assertTrue(
            any("placeholder" in message for message in self.findings_for(placeholder))
        )

    def test_hidden_headings_do_not_count(self) -> None:
        replacements = (
            "<!-- ## Scenario -->",
            "```\n## Scenario\n```",
            "    ## Scenario",
            " \t## Scenario",
        )
        for replacement in replacements:
            with self.subTest(replacement=replacement):
                story = valid_story().replace("## Scenario", replacement)
                self.assertIn(
                    "missing required heading '## Scenario'",
                    self.findings_for(story),
                )

    def test_fence_with_trailing_text_does_not_close_code(self) -> None:
        replacement = (
            "```\n"
            "```not-a-close\n"
            "## Scenario\n\n"
            "One actor takes one action with a concrete consequence.\n"
            "````"
        )
        story = valid_story().replace(
            "## Scenario\n\nOne actor takes one action with a concrete consequence.",
            replacement,
        )
        self.assertIn(
            "missing required heading '## Scenario'",
            self.findings_for(story),
        )

    def test_requires_content_in_core_sections(self) -> None:
        cases = (
            (
                "One actor takes one action with a concrete consequence.\n",
                "section '## Scenario' must not be blank",
            ),
            (
                "The fixture explains its target tier.\n",
                "section '## Claimed tier' must not be blank",
            ),
            (
                "The fixture names the remaining Tier 2 failure.\n",
                "section '## Why not one tier down?' must not be blank",
            ),
        )
        for content, expected in cases:
            with self.subTest(expected=expected):
                self.assertIn(
                    expected,
                    self.findings_for(valid_story().replace(content, "")),
                )

    def test_reports_heading_errors(self) -> None:
        missing = valid_story().replace("## Scenario", "## Context")
        duplicate = valid_story().replace(
            "## Scenario\n", "## Scenario\n\nFirst.\n\n## Scenario\n", 1
        )
        malformed = valid_story().replace(
            "## Claimed tier: Tier 3", "## Claimed tier: Level 3"
        )
        self.assertIn(
            "missing required heading '## Scenario'", self.findings_for(missing)
        )
        self.assertIn(
            "duplicate required heading '## Scenario'", self.findings_for(duplicate)
        )
        self.assertTrue(
            any(
                "'## Claimed tier: Tier N' heading" in message
                for message in self.findings_for(malformed)
            )
        )

    def test_requires_a_real_domain_table(self) -> None:
        no_header = valid_story().replace(
            "| Domain | Tier | Why |", "Domain | Tier | Why"
        )
        hidden_row = valid_story().replace(
            "| Privacy | 2 | A nonblank rationale. |",
            "<!-- | Privacy | 2 | A nonblank rationale. | -->",
        )
        self.assertIn(
            "tier-by-domain Markdown table is missing",
            self.findings_for(no_header),
        )
        self.assertIn("missing domain row 'Privacy'", self.findings_for(hidden_row))

    def test_enforces_gfm_domain_table_boundaries(self) -> None:
        separator = "| :--- | :---: | ---: |"
        short_separator = valid_story().replace(separator, "| : | - | :: |")
        interior_colon = valid_story().replace(separator, "| -:- | --- | --- |")
        gap_after_header = valid_story().replace(
            "| Domain | Tier | Why |\n" + separator,
            "| Domain | Tier | Why |\n\n" + separator,
        )
        gap_after_separator = valid_story().replace(
            separator + "\n| Privacy",
            separator + "\n\n| Privacy",
        )

        one_hyphen = valid_story().replace(separator, "| :- | -: | :- |")
        self.assertEqual(self.findings_for(one_hyphen), [])
        self.assertIn(
            "domain table separator is invalid",
            self.findings_for(short_separator),
        )
        self.assertIn(
            "domain table separator is invalid",
            self.findings_for(interior_colon),
        )
        self.assertIn(
            "domain table separator is invalid",
            self.findings_for(gap_after_header),
        )
        self.assertIn(
            "missing domain row 'Privacy'",
            self.findings_for(gap_after_separator),
        )

    def test_reports_domain_row_errors(self) -> None:
        story = (
            valid_story()
            .replace("| Privacy | 2 |", "| Privacy | 5 |")
            .replace(
                "| Provenance | 3 | A nonblank rationale. |",
                "| Provenance | 3 | |",
            )
            .replace(
                "| Identity | 2 | A nonblank rationale. |",
                "| Identity | 2 | A nonblank rationale. |\n"
                "| Reliability | 2 | Unexpected. |\n"
                "| Identity | 2 | Duplicate. |",
            )
        )
        messages = self.findings_for(story)
        expected = (
            "Privacy tier must be an integer from 1 to 4",
            "Provenance rationale must not be blank",
            "unexpected domain row 'Reliability'",
            "duplicate domain row 'Identity'",
        )
        for message in expected:
            self.assertIn(message, messages)

    def test_collects_nested_stories_and_excludes_support_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            nested = root / "nested"
            nested.mkdir()
            story = nested / "story.md"
            story.write_text(valid_story(), encoding="utf-8")
            (root / "README.md").write_text("support", encoding="utf-8")
            (root / "_TEMPLATE.md").write_text("support", encoding="utf-8")
            self.assertEqual(collect_story_files((root,)), [story.resolve()])

    def test_cli_reports_file_line_and_nonzero_exit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.md"
            path.write_text("# Missing everything else\n", encoding="utf-8")
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                code = main((str(path),))
            self.assertEqual(code, 1)
            self.assertRegex(stderr.getvalue(), r"bad\.md:\d+: ")


if __name__ == "__main__":
    unittest.main()
