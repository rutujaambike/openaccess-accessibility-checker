---
name: "Add more heading checks"
about: "Hacktoberfest contribution: Add more heading checks"
title: "Add more heading checks"
labels: "enhancement,easy"
assignees: ""
---

## Starting point
The starter detects missing and empty main headings. Add skipped levels and multiple H1s.

## Work to do
Explain why each heading sequence was flagged and identify the affected heading.

## Acceptance criteria
Tests cover h1→h3 skipping, valid h1→h2→h3, multiple h1s, and non-heading pages. Update the score category.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
