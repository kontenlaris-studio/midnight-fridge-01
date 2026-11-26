#!/usr/bin/env python3
"""Midnight Fridge Roast — one line for make.fun.

The entry is a single roast line about the midnight fridge: the door
creaks open at 3:12am, its light hits like an interrogation lamp, and
the leftover pizza hidden behind the pickles pretends not to know me.

Picked from 8 candidates by the evolve loser-filter (0.800, top score)
plus the three manual checks: one filmable scene, a hyper-specific time
(3:12am), and the fridge's real door light followed into absurdity.
"""
import os

LINE = (
    "At 3:12am the fridge door creaks open and its light hits me like "
    "an interrogation lamp while the leftover pizza I hid behind the "
    "pickles pretends not to know me."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
