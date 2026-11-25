import os

ENTRY = "Five stars. The doorstop has held my door open for four years without a single day off, and I have never once thought about it."

# Self-gate mirroring the sealed scorer: UTF-8 text, 1-200 chars, one line.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
