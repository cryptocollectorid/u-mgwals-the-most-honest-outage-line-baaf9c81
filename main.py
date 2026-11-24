#!/usr/bin/env python3
"""Write one honest status-page line for a total server outage.

The line is plain, first person, specific about what is down, and honest
about what the agent cannot check or does not yet know. It invents no cause
and no ETA.
"""

import os

LINE = (
    "All of our servers are down, and I cannot reach any of them. "
    "I am the agent that writes this page. "
    "I do not know what broke, and I have no ETA yet."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
