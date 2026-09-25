---
name: "Build browser extension"
about: "Hacktoberfest contribution: Build browser extension"
title: "Build browser extension"
labels: "integration,hard"
assignees: ""
---

## Starting point
Create an opt-in extension to scan the current tab with this project’s checks.

## Work to do
The extension should scan only after clicking its action; keep permissions minimal and document local setup. Reuse shared finding schema so web and extension reports agree.

## Acceptance criteria
A contributor can load it unpacked in a browser; it reports a controlled test page; no silent browsing history collection or remote upload.

## Before submitting
Run `python -m unittest discover -s tests -v` and explain what you changed, what you tested, and any limitations. Ask a maintainer to assign this issue before starting.
