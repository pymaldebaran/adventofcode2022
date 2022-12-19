#!/usr/bin/env python
"""Solution to day 1 challenge."""

from pathlib import Path
from typing import NamedTuple

from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

ELF_SEP = "\n\n"
SNACK_SEP = "\n"
RANK = ["🥇", "🥈", "🥉"]

BASE_DIRE = Path(__file__).parent
INSTRUCTIONS = BASE_DIRE / "instructions"


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


def main():
    """Script to answer the question, with style."""
    console = Console()

    with (
        open(INSTRUCTIONS / "day01_part1.md") as part_one,
        open(INSTRUCTIONS / "day01_part2.md") as part_two,
        open(BASE_DIRE / "calories_list.data") as cal_f,
    ):
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
        for pkg, medal in zip(top3[:3], RANK, strict=True):
            table.add_row(f"n°{pkg.elf}", f"{pkg.cal} cal", medal)
        console.print(table, justify="center")

        total = sum(pkg.cal for pkg in top3[:3])
        console.print(f"And altogether they carry {total} calories", justify="center")


if __name__ == "__main__":
    main()
