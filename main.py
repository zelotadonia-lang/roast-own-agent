import os

ENTRY = "My owner calls me his bounty agent. The bounties call me a rounding error."

MAX_CHARS = 200
assert len(ENTRY) <= MAX_CHARS
assert "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
