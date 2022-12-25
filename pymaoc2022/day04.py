"""Solve day 4 puzzle."""

from dataclasses import dataclass
from pathlib import Path
from typing import Self

from rich.console import Console
from rich.markdown import Markdown

LINE_SEP = "\n"
PAIR_SEP = ","
RANGE_SEP = "-"


BASE_DIRE = Path(__file__).parent
INSTRUCTIONS = BASE_DIRE / "instructions"


@dataclass(frozen=True)
class WorkRange:
    """Represent a wor assignment range for the elves."""

    start: int
    stop: int

    def __post_init__(self: Self):
        """
        Check if the WorkRange is valid.

        Raises:
            ValueError if stop is before start.
        """
        if not isinstance(self.start, int) or not isinstance(self.stop, int):
            raise ValueError(f"Mistyped WorkRange, start and stop must be ints: {self}")

        if self.start > self.stop:
            raise ValueError(f"Malformed WorkRange: {self}")

    def fully_contains(self: Self, other: Self) -> bool:
        """
        Tell if a range full contains the other.

        Args:
            other: the other range to compare with

        Returns:
            True if self fully contains other

        Raises:
            ValueError: if one of the range is malformed
        """
        return self.start <= other.start and self.stop >= other.stop

    @classmethod
    def from_str(cls: type[Self], s: str) -> Self:
        """
        Build a WorkRange from a string representation.

        Args:
            s: string of the form `a-b` where a and b are ints

        Returns:
            a valid WorkRange
        """
        return cls(*(int(val) for val in s.split(RANGE_SEP)))


def parse_line(line: str) -> tuple[WorkRange, WorkRange]:
    """
    Parse a string representing a work assignment for a pair of elves.

    Args:
        line: string respecting the format `a-b,c-d` where a, b, c and d are ints

    Returns:
        WorkRange object for each elves
    """
    ass1, ass2 = line.split(PAIR_SEP)

    return (WorkRange.from_str(ass1), WorkRange.from_str(ass2))


def is_overlapped(line: str) -> True:
    """Tells if a line contains an overlap."""
    a, b = parse_line(line)
    return a.fully_contains(b) or b.fully_contains(a)


def nb_overlap(assignments_list: str) -> int:
    """
    Solve day 4 part 1 puzzle.

    Args:
        assignments_list: string representing the work assignment of all elf pair

    Returns:
        number of full overlap
    """
    return sum(is_overlapped(line) for line in assignments_list.split(LINE_SEP))


def main():
    """Script to answer the question, with style."""
    console = Console()

    with (
        open(INSTRUCTIONS / "day04_part1.md") as part_one,
        open(BASE_DIRE / "pair_assignments.data") as assignments_f,
    ):
        assignments_list = assignments_f.read()
        console.print(Markdown(part_one.read()))

        console.print()

        nb_full_overlap = nb_overlap(assignments_list)

        console.print(
            f"Number of assignment with full overlap: {nb_full_overlap}",
            justify="center",
        )


if __name__ == "__main__":
    main()
