#!/usr/bin/env python
"""Solution to day 1 challenge."""

import os
from pathlib import Path
from typing import NamedTuple

from assertpy import assert_that, soft_assertions
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table


ELF_SEP = "\n\n"
SNACK_SEP = "\n"
RANK = ["🥇", "🥈", "🥉"]

# Change the cwd to be able to use the script from anywhere
os.chdir(Path(__file__).parent)


class ElfPackage(NamedTuple):
    """Calories carried by an Elf."""

    elf: int  # index
    cal: int  # calories


def most_calorie_elf(calorie_list: str) -> ElfPackage:
    """
    Answer the day 1 part 1 challenge question.

    Args:
        calorie_list: This list represents the Calories of the food carried by all Elves

    Returns:
        Elf package of the elf carrying the most calories
    """
    return most_calorie_elves(calorie_list)[0]


def most_calorie_elves(calorie_list: str) -> list[ElfPackage]:
    """
    Answer the day 1 part 2 challenge question.

    Args:
        calorie_list: This list represents the Calories of the food carried by all Elves

    Returns:
        list of Elf package of the elves carrying the most calories
    """
    all_snacks = list(calorie_list.split(ELF_SEP))
    total_cal = [
        ElfPackage(
            elf=idx, cal=sum(int(snack) for snack in snack_one_elf.split(SNACK_SEP))
        )
        for idx, snack_one_elf in enumerate(all_snacks, start=1)
    ]

    return sorted(total_cal, key=lambda x: x.cal, reverse=True)


def test_most_calorie_elf():  # noqa: D103
    with open("calories_list_sample.data") as cal_list:
        pkg = most_calorie_elf(cal_list.read())

    with soft_assertions():
        assert_that(pkg.elf).is_equal_to(4)
        assert_that(pkg.cal).is_equal_to(24000)


def test_most_calorie_three_elves():  # noqa: D103
    with open("calories_list_sample.data") as cal_list:
        result = most_calorie_elves(cal_list.read())

    assert_that(len(result)).is_greater_than_or_equal_to(3)
    with soft_assertions():
        assert_that(result[0].elf).is_equal_to(4)
        assert_that(result[0].cal).is_equal_to(24000)
        assert_that(result[1].elf).is_equal_to(3)
        assert_that(result[1].cal).is_equal_to(11000)
        assert_that(result[2].elf).is_equal_to(5)
        assert_that(result[2].cal).is_equal_to(10000)


def main():
    """Script to answer the question, with style."""
    console = Console()

    with open("day01_part1.md") as part_one, open("day01_part2.md") as part_two, open(
        "calories_list.data"
    ) as cal_f:
        cal_list = cal_f.read()
        console.print(Markdown(part_one.read()))

        console.print()

        top1 = most_calorie_elf(cal_list)

        console.print(
            f"The elf with the most calories is n°{top1.elf}", justify="center"
        )
        console.print(f"And it carries {top1.cal} calories", justify="center")

        console.print()

        console.print(Markdown(part_two.read()))

        console.print()

        top3 = most_calorie_elves(cal_list)

        console.print("The top three Elves carrying the most Calories are:")

        console.print()

        table = Table(title="Elves snack packages", show_lines=True)
        table.add_column("Elf", justify="left", style="bold green")
        table.add_column("Calories", justify="left", style="yellow")
        table.add_column("Rank", justify="center")
        for pkg, medal in zip(top3[:3], RANK):
            table.add_row(f"n°{pkg.elf}", f"{pkg.cal} cal", medal)
        console.print(table, justify="center")

        total = sum(pkg.cal for pkg in top3[:3])
        console.print(f"And altogether they carry {total} calories", justify="center")


if __name__ == "__main__":
    main()
