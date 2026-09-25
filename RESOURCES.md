# Resources for contributors

## 1. What is this project?
A learning project that flags selected accessibility problems in one public page's HTML. URL safety hints appear separately.

## 2. Concepts you need to know
HTML elements and attributes, accessible names, keyboard navigation, HTTP requests, Git branches and pull requests.

## 3. Prerequisites
Python 3.10+, Git, a code editor, and a browser. No Gmail or AI account.

## 4. Setup
Clone the repository, run `python server.py`, open `http://127.0.0.1:8000`, and run `python -m unittest discover -s tests -v`. For the intentionally flawed example, see `examples/inaccessible-demo.html` and its test.

## 5. Recommended reading
- [W3C Web Accessibility Initiative introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/)
- [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [MDN HTML accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML)
- [Playwright accessibility testing](https://playwright.dev/docs/accessibility-testing)

## 6. Recommended videos
Use the video and presentation links on the [W3C WAI introduction](https://www.w3.org/WAI/fundamentals/accessibility-intro/). Follow along by testing the example HTML.

## 7. Glossary
- **Accessibility:** Making a product usable by people with different abilities.
- **Alt text:** Text alternative to an image.
- **Accessible name:** Label announced for a control or link.
- **WCAG:** Web Content Accessibility Guidelines.
- **Static HTML:** Markup received before scripts modify the page.
- **False positive:** A reported issue that is not actually a problem.

## 8. Useful tools
Browser developer tools; keyboard-only navigation; an assistive technology or screen reader; axe DevTools for manual comparison.

## 9. Before you pick an issue
Run the tests, read the acceptance criteria, comment on the issue, and check if someone else is assigned. Reproduce the current behavior before editing.

## 10. How to submit your PR
Fork, branch from main, make a focused change, add or update a relevant test, run `python -m unittest discover -s tests -v`, and open a PR explaining the change and showing a screenshot for UI work.
