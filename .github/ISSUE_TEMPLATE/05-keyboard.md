---
name: "Add keyboard accessibility checks"
about: "Hacktoberfest contribution: Add keyboard accessibility checks"
title: "Add keyboard accessibility checks"
labels: "enhancement,medium"
assignees: ""
---

## Starting point
Static HTML cannot prove keyboard operability. Add browser-based checks with honest limitations.

## Work to do
Identify obvious inaccessible controls (e.g. clickable non-focusable elements), test tab reachability where feasible, and provide a manual checklist for keyboard operation.

## Acceptance criteria
At least one failing and one passing browser fixture; results distinguish automated findings from manual-review prompts. Document why tab order and interactions still need human testing.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
