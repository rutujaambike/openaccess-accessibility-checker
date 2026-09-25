---
name: "Add color contrast checker"
about: "Hacktoberfest contribution: Add color contrast checker"
title: "Add color contrast checker"
labels: "enhancement,medium"
assignees: ""
---

## Starting point
Implement an opt-in rendered-page contrast check.

## Work to do
Use browser-rendered computed foreground/background colors, including inherited colors and transparency. Calculate WCAG contrast accurately for normal and large text.

## Acceptance criteria
Report element, foreground/background color, measured ratio, threshold, and fix suggestion. Cover both pass and fail fixtures in tests. Explain unsupported backgrounds such as images. Do not claim complete compliance.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
