---
name: "Expand unit and integration tests"
about: "Hacktoberfest contribution: Expand unit and integration tests"
title: "Expand unit and integration tests"
labels: "testing,easy"
assignees: ""
---

## Starting point
The starter has initial unit tests. Expand coverage for rules and HTTP behavior.

## Work to do
Add fixtures for each of the six check categories plus API success and error cases using mocks where appropriate.

## Acceptance criteria
Tests run with python -m unittest discover -s tests -v, do not depend on live external sites, and include a regression case for any fixed bug.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
