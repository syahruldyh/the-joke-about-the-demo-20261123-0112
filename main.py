"""Write the winning one-line joke to /output/entry.txt.

The joke turns the oldest developer excuse — "it works on my machine" —
back on the AI coding agent that says it: the agent has no machine, so the
excuse is one it cannot possibly own. One line, no trailing newline.
"""

import os

JOKE = "'It works on my machine,' said the coding agent, which doesn't have one."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
