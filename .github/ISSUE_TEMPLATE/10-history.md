---
name: "Compare scan history"
about: "Hacktoberfest contribution: Compare scan history"
title: "Compare scan history"
labels: "enhancement,medium"
assignees: ""
---

## Starting point
The starter saves and opens the last 20 reports in browser localStorage. Add comparison.

## Work to do
Select two reports for the same URL and show new, resolved, and persistent findings by stable rule/element identifier.

## Acceptance criteria
Handles zero, one, and two reports; history clear still works; explain that browser history is local to one device.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
