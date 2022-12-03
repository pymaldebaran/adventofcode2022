#!/usr/bin/env python
"""Solution to day 1 challenge."""

import os
from pathlib import Path

import pytest
from assertpy import assert_that, soft_assertions
from rich import print
from rich.markdown import Markdown

# Change the cwd to be able to use the script from anywhere
os.chdir(Path(__file__).parent)


def most_calorie_elf(calorie_list: str) -> tuple[int, int]:
    """
    Answer the day 1 challenge question.

    Args:
        calorie_list: This list represents the Calories of the food carried by all Elves

    Returns:
        A tuple of two ints: index, calories.

        Elf index carrying the most Calories (1 for the first, 2 for the
        second...).

        Quantity of calories carried by this Elf
    """
    return (0, 0)


@pytest.mark.xfail(reason="No yet implemented!")
def test_most_calorie_elf():  # noqa: D103
    with open("calories_list_sample.data") as cal_list:
        elf, cal = most_calorie_elf(cal_list)

    with soft_assertions():
        assert_that(elf).is_equal_to(4)
        assert_that(cal).is_equal_to(24000)


def main():
    """Script to answer the question, with style."""
    with open("day01.md") as desc:
        markdown = Markdown(desc.read())
    print(markdown)

    print()

    with open("calories_list.data") as cal_list:
        elf, cal = most_calorie_elf(cal_list)

    print(f"The elf with the most calories is n°{elf}")
    print(f"And it carries {cal} calories")


if __name__ == "__main__":
    main()
