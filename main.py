"""Write one childhood-memory sentence to /output/entry.txt.

Saturday-morning cartoons: cereal going soggy, sitting too close
to the TV, the theme tune still in your head. Stdlib only, no
network, deterministic.
"""

import os

SENTENCE = (
    "Every Saturday I sat cross-legged on the carpet, too close to the TV, "
    "spooning cereal that had already gone soggy while the theme tune played, "
    "and I never wanted that morning to end."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
