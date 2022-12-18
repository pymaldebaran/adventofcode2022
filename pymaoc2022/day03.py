#!/usr/bin/env python
"""Solution to day 2 challenge."""

import string
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown

BAG_SEP = "\n"

BASE_DIR = Path(__file__).parent


def split_in_half(content: str) -> tuple[str, str]:
    """
    Split a string in two equal length substrings.

    Args:
        content: a string to split

    Returns:
        The left and right part of the string
    """
    length = len(content)

    # We won't handle the not even strings
    assert length % 2 == 0

    return (content[: length // 2], content[length // 2 :])


def misplaced_item(rucksack: str) -> str:
    """
    Get the misplaced item of a rucksack.

    Args:
        rucksack: string representing the content of one rucksack

    Returns:
        the misplaced item

    Raises:
        ValueError: if rucksack contains no or multiple misplaced items
    """
    left_compartment, right_compartment = split_in_half(rucksack)
    intersection = {*left_compartment} & {*right_compartment}

    # TODO test this exec path
    if len(intersection) > 1:
        raise ValueError(f"Rucksack contains multiple misplaced snacks: {intersection}")

    # TODO test this exec path
    if len(intersection) == 0:
        raise ValueError(f"Rucksack contains no misplaced snacks: {rucksack}")

    return intersection.pop()


def priority(item: str) -> int:
    """
    Return the priority of an item.

    - Lowercase item types `a` through `z` have priorities 1 through 26.
    - Uppercase item types `A` through `Z` have priorities 27 through 52.

    Args:
        item: one char string representing an item. Must be a letter.

    Returns:
        corresponding priority

    Raises:
        ValuesError: if the items is not an ascii character
    """
    if item in string.ascii_lowercase:
        return ord(item) - ord("a") + 1
    elif item in string.ascii_uppercase:
        return ord(item) - ord("A") + 27
    else:
        # TODO test this exec path
        raise ValueError(f"Item must be an ascii letter: {item}")


def one_misplaced_priority(rucksack: str) -> int:
    """
    Compute the priority of the misplaced item of one rucksack.

    Args:
        rucksack: string representing the content of one rucksack

    Returns:
        priority
    """
    return priority(misplaced_item(rucksack))


def all_misplaced_priorities(rucksack_list: str) -> int:
    """
    Compute the priority of each rucksac misplaced item.

    Args:
        rucksack_list: string representing the content of all rucksacks

    Returns:
        all list of all the priorities
    """
    return [one_misplaced_priority(bag) for bag in rucksack_list.split(BAG_SEP)]


def compute_total_priorities(rucksack_list: str) -> int:
    """
    Answer the day 3 part 1 challenge question.

    Args:
        rucksack_list: string representing the content of all rucksacks

    Returns:
        the sum of all the priorities of the misplaced items
    """
    return sum(all_misplaced_priorities(rucksack_list))


def main():
    """Script to answer the question, with style."""
    console = Console()

    with (
        open(BASE_DIR / "day03_part1.md") as part_one,
        # open(BASE_DIR / "day02_part2.md") as part_two,
        open(BASE_DIR / "rucksack_contents.data") as ruck_f,
    ):
        ruck_list = ruck_f.read()
        console.print(Markdown(part_one.read()))

        console.print()

        total_priority = compute_total_priorities(ruck_list)

        console.print(
            f"Sum of the misplaced item's priorities: {total_priority}",
            justify="center",
        )


if __name__ == "__main__":
    main()
