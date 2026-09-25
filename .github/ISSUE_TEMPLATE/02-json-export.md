---
name: "Improve JSON report export"
about: "Hacktoberfest contribution: Improve JSON report export"
title: "Improve JSON report export"
labels: "enhancement,easy"
assignees: ""
---

## Starting point
The starter already downloads a JSON report. Extend its structured data and documentation.

## Work to do
Define a versioned JSON schema including scan timestamp, URL, engine, basic score breakdown, issue counts, rules, elements, fixes, safety signals, and limitations.

## Acceptance criteria
Export parses as valid JSON; file schema is documented and has a test. Older saved reports remain viewable.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
