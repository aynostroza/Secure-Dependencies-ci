# Secure Dependencies CI Lab

A calculator with ten unit tests, GitHub Actions, Safety, pip-audit, and Bandit.
The initial requirements intentionally contain vulnerable versions for an isolated
class demonstration. The calculator does not make network requests.

The workflow tests code and scans dependencies on pushes and pull requests.
Set the `SAFETY_API_KEY` Actions repository secret before running it.
Scanners use separate virtual environments so they cannot upgrade the tested app.
The scanners inspect the app's resolved dependencies, including transitives.

Use the accompanying LAB_GUIDE.md for setup, the two required commits, additional
remediation if needed, and the screen recording checklist.

A green job does not establish clean scan results: inspect the step outcomes and
logs. Never treat an authentication or network error as successful scanning.

Local tests without third-party dependencies:

```powershell
py -m unittest discover -s tests -v
```

GitHub runs these same tests through pytest.
