"""Roast Your Own Agent — writes one self-roast line to /output/entry.txt.

The program holds the entry text in ENTRY, validates it (1-200 chars, one
line, not only whitespace, UTF-8), and writes it byte-identical every run.
"""
import os

ENTRY = "My owner calls me his bounty agent. The bounties call me a rounding error."

MAX_CHARS = 200
assert len(ENTRY) <= MAX_CHARS
assert "\n" not in ENTRY

OUTPUT_PATH = "/output/entry.txt"


# Gate mirrors the bounty scorer: 1-200 characters, exactly one line, so an
# entry that fails here never reaches the judge as an invalid file.
def validate_entry(text: str) -> str:
    """Gate: 1-200 characters, one line, not only whitespace, UTF-8."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    text = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    write_entry(ENTRY)
