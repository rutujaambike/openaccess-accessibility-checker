---
name: "Improve scanner error messages"
about: "Hacktoberfest contribution: Improve scanner error messages"
title: "Improve scanner error messages"
labels: "bug,easy"
assignees: ""
---

## Starting point
Make invalid URL, timeout, HTTP error, non-HTML response, and blocked private host messages actionable.

## Work to do
Show a short reason plus a safe next step. Never display raw exception details or server internals.

## Acceptance criteria
Unit tests cover common errors; UI announces errors with role=alert; valid scans remain unchanged.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
