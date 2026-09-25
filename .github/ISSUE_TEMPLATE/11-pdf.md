---
name: "Add PDF report download"
about: "Hacktoberfest contribution: Add PDF report download"
title: "Add PDF report download"
labels: "enhancement,medium"
assignees: ""
---

## Starting point
Export the current report to a readable, professionally formatted PDF.

## Work to do
Include URL, scan time, basic category score with its limitation, grouped findings, elements, fixes, and URL safety separately.

## Acceptance criteria
Multi-page long reports do not clip text; headings and reading order are sensible; print/download button works; tests cover empty and multi-page cases.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
