#!/usr/bin/env python
"""Solution to day 2 challenge."""

import string
from pathlib import Path

from more_itertools import chunked
from rich.console import Console
from rich.markdown import Markdown

BAG_SEP = "\n"

BASE_DIRE = Path(__file__).parent
INSTRUCTIONS = BASE_DIRE / "instructions"


def split_in_half(content: str) -> tuple[str, str]:
    """
    Split a string in two equal length substrings.

    Args:
        content: a string to split

    Returns:
        The left and right part of the string
    """
    length = len(content)

    assert length % 2 == 0, f"We won't handle the not even strings: {content}"

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


def badge_item(group: list[str]) -> str:
    """
    Get the identification badge item of a group of rucksack.

    Args:
        group: group of 3 rucksack belonging to a group of elves

    Returns:
        the identification badge

    Raises:
        ValueError: if the group of rucksack contains no or multiple badges
    """
    if len(group) != 3:
        # TODO test this execution path
        raise ValueError(f"A group must be constituted of 3 rucksack: {group}")

    bag1, bag2, bag3 = group
    intersection = {*bag1} & {*bag2} & {*bag3}

    # TODO test this exec path
    if len(intersection) > 1:
        raise ValueError(f"Group contains multiple badges: {intersection}")

    # TODO test this exec path
    if len(intersection) == 0:
        raise ValueError(f"Group contains no badge: {group}")

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


def one_badge_priority(group: list[str]) -> int:
    """
    Compute the priority of the badge of one group of rucksack.

    Args:
        group: group of 3 rucksack belonging to a group of elves

    Returns:
        priority
    """
    return priority(badge_item(group))


def all_misplaced_priorities(rucksack_list: str) -> int:
    """
    Compute the priority of each rucksac misplaced item.

    Args:
        rucksack_list: string representing the content of all rucksacks

    Returns:
        all list of all the priorities
    """
    return [one_misplaced_priority(bag) for bag in rucksack_list.split(BAG_SEP)]


def all_badges_priorities(rucksack_list: str) -> int:
    """
    Compute the priority of each identification badges.

    Args:
        rucksack_list: string representing the content of all rucksacks

    Returns:
        all list of all the priorities
    """
    return [
        one_badge_priority(group) for group in chunked(rucksack_list.split(BAG_SEP), 3)
    ]


def compute_total_priorities(rucksack_list: str, part: int = 1) -> int:
    """
    Answer the day 3 part 1 challenge question.

    Args:
        rucksack_list: string representing the content of all rucksacks
        part: 1 to compute part 1 score 2 to compute part 2 score

    Returns:
        the sum of all the priorities of the misplaced items
    """
    if part == 1:
        return sum(all_misplaced_priorities(rucksack_list))
    else:
        return sum(all_badges_priorities(rucksack_list))


def main():
    """Script to answer the question, with style."""
    console = Console()

    with (
        open(INSTRUCTIONS / "day03_part1.md") as part_one,
        open(INSTRUCTIONS / "day02_part2.md") as part_two,
        open(BASE_DIRE / "rucksack_contents.data") as ruck_f,
    ):
        ruck_list = ruck_f.read()
        console.print(Markdown(part_one.read()))

        console.print()

        total_misplaced_priority = compute_total_priorities(ruck_list)

        console.print(
            f"Sum of the misplaced item's priorities: {total_misplaced_priority}",
            justify="center",
        )

        console.print()

        console.print(Markdown(part_two.read()))

        console.print()

        total_badges_priority = compute_total_priorities(ruck_list, part=2)

        console.print(
            f"Sum of the identification badges priorities: {total_badges_priority}",
            justify="center",
        )


if __name__ == "__main__":
    main()
