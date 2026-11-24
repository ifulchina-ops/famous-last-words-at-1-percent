"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's one-line farewell to /output/entry.txt.
The line is the phone itself speaking at 1% battery: it confesses the
charger was right there the whole time and it only wanted to watch its
owner panic a little longer before being plugged in.
"""

import os

ENTRY = (
    "One percent. The charger was right here the whole time. "
    "I just wanted to see how long you'd panic before plugging me in."
)


def main() -> None:
    # The gate accepts 1-199 characters; fail loudly rather than ship invalid.
    if not (1 <= len(ENTRY) <= 199) or not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry line must be one non-blank line of 1-199 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
