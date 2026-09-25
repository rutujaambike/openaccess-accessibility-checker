from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import json
from scanner import scan, ScanError, accessibility_findings, accessibility_score

ROOT = Path(__file__).resolve().parent
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            data = (ROOT / 'index.html').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
        elif self.path == '/demo':
            data = (ROOT / 'examples' / 'inaccessible-demo.html').read_bytes()
            self.send_response(200)
            self.send_header('Content-Type','text/html; charset=utf-8')
        else:
            self.send_error(404)
            return
        self.send_header('Content-Length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path not in ('/api/scan', '/api/demo'):
            self.send_error(404)
            return
        try:
            size = int(self.headers.get('Content-Length','0'))
            if size < 1 or size > 4096:
                raise ScanError('Invalid request size.')
            payload = json.loads(self.rfile.read(size))
            if self.path == '/api/demo':
                html = (ROOT / 'examples' / 'inaccessible-demo.html').read_text()
                findings = accessibility_findings(html)
                result = {'url':'Built-in example page', 'findings':findings,
                          'score':accessibility_score(html, findings),
                          'safety':{'status':'Not checked','signals':[],
                                    'note':'Built-in example: no external URL was opened.'},
                          'method':'Static HTML checks on bundled example.'}
            else:
                result = scan(payload.get('url',''))
            status = 200
        except (ScanError, ValueError, json.JSONDecodeError) as exc:
            result = {'error':str(exc)}
            status = 400
        except Exception:
            result = {'error':'Scan failed unexpectedly. Please try another URL.'}
            status = 500
        data = json.dumps(result).encode()
        self.send_response(status)
        self.send_header('Content-Type','application/json; charset=utf-8')
        self.send_header('Content-Length',str(len(data)))
        self.end_headers()
        self.wfile.write(data)

if __name__ == '__main__':
    print('Open http://127.0.0.1:8000')
    ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
