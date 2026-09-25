---
name: "Improve CSV report export"
about: "Hacktoberfest contribution: Improve CSV report export"
title: "Improve CSV report export"
labels: "enhancement,easy"
assignees: ""
---

## Starting point
The starter already exports one row per finding. Improve spreadsheet safety and completeness.

## Work to do
Include scan time, score, and category status; make spreadsheet formula injection impossible for attacker-controlled fields.

## Acceptance criteria
Unicode and comma/quote/newline cases are covered in tests; empty-result exports still contain scan metadata; CSV opens correctly in Excel and Sheets.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
