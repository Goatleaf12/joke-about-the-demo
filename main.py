"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt, as the competition requires. No network, no input:
the program simply emits the line.
"""

from pathlib import Path

JOKE = (
    "The demo worked in rehearsal because my agent had memorized it. "
    "Live, it tried to improvise."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
