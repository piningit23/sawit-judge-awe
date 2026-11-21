"""Write one short relaxing text to /output/entry.txt.

The text is a single fixed string, written verbatim. No input is
read, no network is used, and the output is the same on every run.
"""

from pathlib import Path

TEXT = (
    "The snow falls on the frozen lake and does not hurry. "
    "Under the ice, the water moves on, dark and unhurried, "
    "carrying the whole long winter toward a spring still months away "
    "\u2014 and somewhere above it all, the sky keeps turning, "
    "patient as stone."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
