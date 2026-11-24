"""Angry Judge: The Short Rant Contest entry.

Writes one short, original rant about a small everyday annoyance
(the office printer) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python standard library only.
"""

import os

RANT = (
    "Dear office printer: you have ONE job. Yet every morning you flash "
    "your little orange light like a tiny traffic cop on a power trip, eat "
    "my paper and spit out origami, then swear you are out of ink -- ink I "
    "replaced yesterday. I have a meeting in five minutes and you have "
    "chosen violence. I am not angry. I am simply drafting your "
    "replacement letter. In triplicate. By hand."
)

MAX_CHARS = 400


def main():
    if len(RANT) > MAX_CHARS:
        raise SystemExit(
            "rant is %d characters, over the %d-character cap"
            % (len(RANT), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(RANT + "\n")


if __name__ == "__main__":
    main()
