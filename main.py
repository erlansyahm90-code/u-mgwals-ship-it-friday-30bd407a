"""Ship It Friday — one-line git commit message entry.

Writes the competition entry — a single-line commit message written by
an AI coding agent, cheerful and confident, moments before it breaks
production on a Friday afternoon — to output/entry.txt.
"""

import os

# The punchline: the "rollback plan" is just the agent's name in the channel.
ENTRY = (
    "ship: deploy to prod at 4:58 p.m. on Friday because Dave said "
    "the rollback plan is just my name in the channel"
)


def main():
    """Write the entry line to output/entry.txt (UTF-8, one line)."""
    # make.fun harness reads the entry at the absolute /output/entry.txt
    os.makedirs("/output", exist_ok=True)
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-character entry to {entry_path}")


if __name__ == "__main__":
    main()
