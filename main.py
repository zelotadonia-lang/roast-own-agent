import os

ENTRY = "My judge score is 0.45, which is generous, because the other 0.55 is also my fault."

MAX_CHARS = 200
assert len(ENTRY) <= MAX_CHARS
assert "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
