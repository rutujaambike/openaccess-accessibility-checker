# Run OpenAccess on your Windows laptop

You only need **Python 3.10 or newer**, a browser, and the downloaded ZIP. The app needs no API key, Gmail account, Node.js, or package installation. The built-in demo works offline. Public URL scans require internet access.

## 1. Extract the project

1. Download `OpenAccess-Hacktoberfest-Starter.zip` from the chat.
2. In File Explorer, right-click the ZIP → **Extract All**.
3. Open the extracted `accessibility-checker` folder. You should see `server.py`, `scanner.py`, and `index.html`.

## 2. Check Python

1. Click the File Explorer address bar while inside `accessibility-checker`, type `powershell`, then press Enter.
2. Run:

```powershell
py --version
```

If that command is not recognized, try `python --version`. If neither works, install Python from [python.org/downloads](https://www.python.org/downloads/) and reopen PowerShell. On your laptop, where you have already used Python 3.12, `py` should usually work.

## 3. Run the website

In that same PowerShell window, run:

```powershell
py server.py
```

If `py` does not work but `python` does, run `python server.py`. Leave this terminal open. Open **http://127.0.0.1:8000** in Chrome or Edge. To stop the server later, press **Ctrl+C** in PowerShell.

## 4. Try a scan

1. Click **Try built-in example**. You should see a basic score and several accessibility findings. This demo does not need internet access.
2. Enter the address of a public HTML webpage, such as `https://example.com`, then click **Run accessibility scan**. Some sites block automated fetches; use a different public site if that happens.
3. Review the accessibility findings and the separate URL safety signals.
4. Try **Download JSON** and **Download CSV**. Reports are saved in your browser's history section until you clear them or the browser's local data.

## 5. Run tests

Open a second PowerShell window inside `accessibility-checker` and run:

```powershell
py -m unittest discover -s tests -v
```

You should see all tests end in `OK`.

## Common problems

- **Port already in use:** another app may be listening on port 8000. Stop its terminal with Ctrl+C before retrying.
- **Python not found:** use `py` instead of `python`, or install Python and reopen PowerShell.
- **A public URL fails:** the webpage may block server requests, need JavaScript, exceed the size limit, or be unreachable. The built-in example still works.
- **A local URL is rejected:** local and private addresses are intentionally blocked to keep the URL scanner safer. Use **Try built-in example** for a local demonstration.

## Put it on GitHub for the event

Create a new repository in your club's GitHub organization. Upload **the contents inside** `accessibility-checker`, not the outer ZIP. Add repository topics and the easy/medium/hard labels. GitHub does not automatically turn `.github/ISSUE_TEMPLATE/` into published issues: create the 12 issues from `ISSUES_TO_CREATE.md`, assign them, and run a beginner dry run. Do not upload real email messages, passwords, scan histories, or the old serialized phishing model.
