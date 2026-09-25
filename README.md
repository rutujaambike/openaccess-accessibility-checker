# OpenAccess — Campus Accessibility Checker

An accessibility-first adaptation of a phishing URL detector prototype. [Windows step-by-step instructions](RUN_ON_WINDOWS.md). Enter a public webpage URL to receive **static HTML findings** with affected elements and suggested fixes. A separate panel shows limited URL safety signals. Saved reports and JSON export are available in the browser.

## Quick start

Requires Python 3.10+; no packages or API keys.

```bash
python server.py
```

Open <http://127.0.0.1:8000>. Enter any public HTML webpage URL. Click **Try built-in example** for a predictable scan without network access. The page lives in `examples/inaccessible-demo.html`. Local network addresses are deliberately blocked for normal URL scans. You can test the sample locally without network access with `python -m unittest discover -s tests -v`.

## What works today

- One public HTTP/HTTPS webpage per scan, including redirects.
- Static checks: page title, language, image alt attributes, form field labels, button/link names, empty and missing main headings.
- Severity totals, element references, explanations, suggested fixes, a basic passed-category score, JSON and CSV exports, browser-only history with view and clear controls.
- Separate basic URL signals (HTTP, IP host, long URL, many subdomains, IDN encoding).
- URL and redirect validation, private address rejection, size and timeout limits.

## Basic score

The displayed score is the percentage of **applicable categories passed** among page title, language, heading structure, images, form labels, and links/buttons. A category with no relevant elements is marked not applicable and excluded. For example, passing 4 of 5 applicable categories gives 80%. This is a teaching indicator, not a WCAG compliance rating, and a 100% result does not mean a page is accessible.

## Hacktoberfest issues

The 12 issue templates in `.github/ISSUE_TEMPLATE/` cover every requested task. See [ISSUES_TO_CREATE.md](ISSUES_TO_CREATE.md) for what already works and what remains to implement. Issue templates are not automatically published as GitHub issues.

## Limits

This is a **learning starter**, not a WCAG compliance audit, browser-based axe scan, phishing classifier, or malware detector. HTML created after JavaScript runs is not scanned. The URL safety hints do not establish that a URL is safe or malicious. Textual labels are approximated; manual review is required. For public deployment, isolate outbound requests at the network layer to prevent DNS rebinding and similar server-side request forgery; add rate limits and resource controls. Run locally for the event starter.

The uploaded prototype included a dashboard and serialized model, but its `api.py` and `features.py` contained no implementation. This repo does not load the unverified pickle model or retain a nonworking Gmail password form. No real email messages or credentials are needed.

## Project layout

- `server.py`: local API and page server.
- `scanner.py`: URL validation, fetching, accessibility rules, and separate URL hints.
- `index.html`: accessible interface, report, export, and browser history.
- `examples/`: intentionally inaccessible sample for learning.
- `tests/`: checks for known findings and URL validation.
- `RESOURCES.md`: beginner learning path.
- `CONTRIBUTING.md`: contribution steps.

## For contributors

Pick a labeled issue, comment before beginning, create a branch, run the tests, and open a PR using the template. Keep changes small and explain how you verified them. See [RESOURCES.md](RESOURCES.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
