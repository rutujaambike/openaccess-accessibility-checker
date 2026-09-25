---
name: "Add ARIA validation"
about: "Hacktoberfest contribution: Add ARIA validation"
title: "Add ARIA validation"
labels: "enhancement,medium"
assignees: ""
---

## Starting point
Detect common invalid ARIA attributes, references, values, and role requirements.

## Work to do
Prefer a maintained validator or a documented subset of rules; avoid guessing based on tag names alone.

## Acceptance criteria
For each finding show element, rule, and fix. Include tests for invalid role, dangling aria-labelledby, missing required attributes, and valid ARIA.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
