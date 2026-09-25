import unittest
from unittest.mock import patch
from pathlib import Path
from scanner import accessibility_findings, accessibility_score, safety_signals, validate_url, public_addresses, ScanError

class ScannerTests(unittest.TestCase):
    def test_demo_findings(self):
        html=(Path(__file__).resolve().parents[1]/'examples/inaccessible-demo.html').read_text()
        rules=[item['rule'] for item in accessibility_findings(html)]
        self.assertIn('Image alternative text',rules)
        self.assertIn('Form control label',rules)
        self.assertIn('Page language',rules)
        self.assertIn('Page title',rules)
        score = accessibility_score(html, accessibility_findings(html))
        self.assertLess(score['value'], 100)
        self.assertEqual(score['applicable'], 6)

    def test_clean_static_page(self):
        html='<html lang="en"><head><title>Home</title></head><body><h1>Home</h1><label for="q">Search</label><input id="q"><img alt="" src="x"><button>Go</button></body></html>'
        findings = accessibility_findings(html)
        self.assertEqual([], findings)
        self.assertEqual(100, accessibility_score(html, findings)['value'])

    def test_score_ignores_missing_element_categories(self):
        html = '<html lang="en"><head><title>Simple page</title></head><body>Hello</body></html>'
        score = accessibility_score(html, accessibility_findings(html))
        self.assertEqual(3, score['applicable'])
        self.assertEqual(67, score['value'])

    def test_url_validation(self):
        self.assertEqual(validate_url('example.com'),'https://example.com/')
        for bad in ('file:///etc/passwd','https://user:pass@example.com','http://localhost:9000','https://example.com:22/'):
            with self.assertRaises(ScanError):validate_url(bad)

    def test_private_addresses(self):
        with patch('scanner.socket.getaddrinfo',return_value=[(None,None,None,None,('127.0.0.1',0))]):
            with self.assertRaises(ScanError): public_addresses('example.com')
        with patch('scanner.socket.getaddrinfo',return_value=[(None,None,None,None,('1.1.1.1',0)),(None,None,None,None,('192.168.0.1',0))]):
            with self.assertRaises(ScanError): public_addresses('example.com')

    def test_safety_is_not_accessibility(self):
        self.assertIn('HTTP',safety_signals('http://example.com/')['signals'][0])
        self.assertEqual('No simple URL warnings',safety_signals('https://example.com/')['status'])
if __name__=='__main__':unittest.main()
