"""
Dependency-visibility smoke test.

Run:
    pip install -r requirements.txt
    python probe.py
"""

from slugify import slugify  # raises ImportError immediately if unseen

TEXT = "ChatGPT Codex Dependency Probe!"
EXPECTED = "chatgpt-codex-dependency-probe"

result = slugify(TEXT)
assert result == EXPECTED, f"slugify() returned {result!r}, expected {EXPECTED!r}"

print("Dependency visible ✔")

