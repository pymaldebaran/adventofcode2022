#!/usr/bin/env python
"""Solution to day 2 challenge."""

from enum import StrEnum
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table


ROUND_SEP = "\n"
ORDER_SEP = " "

BASE_DIR = Path(__file__).parent


class ElfShape(StrEnum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class MyShape(StrEnum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Expected(StrEnum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


SHAPE_TO_PLAY = {
    (ElfShape.ROCK, Expected.WIN): MyShape.PAPER,
    (ElfShape.PAPER, Expected.WIN): MyShape.SCISSORS,
    (ElfShape.SCISSORS, Expected.WIN): MyShape.ROCK,
    (ElfShape.ROCK, Expected.LOSE): MyShape.SCISSORS,
    (ElfShape.PAPER, Expected.LOSE): MyShape.ROCK,
    (ElfShape.SCISSORS, Expected.LOSE): MyShape.PAPER,
    (ElfShape.ROCK, Expected.DRAW): MyShape.ROCK,
    (ElfShape.PAPER, Expected.DRAW): MyShape.PAPER,
    (ElfShape.SCISSORS, Expected.DRAW): MyShape.SCISSORS,
}


def shape_score(shape: MyShape):
    """
    Compute the score for the shape you selected.

    Args:
        shape: shape you played

    Returns:
        1 for Rock, 2 for Paper, and 3 for Scissors
    """
    match shape:
        case MyShape.ROCK:
            return 1
        case MyShape.PAPER:
            return 2
        case MyShape.SCISSORS:
            return 3
        case _:
            assert False


def outcome_score(elf: ElfShape, me: MyShape) -> int:
    """
    Compute the outcome score of Rock Paper Scissors match.

    Args:
        elf: shape played by the elf
        me: shape played by me

    Returns:
        0 if you lost, 3 if the round was a draw, and 6 if you won
    """
    match (elf, me):
        case (ElfShape.ROCK, MyShape.PAPER) | (ElfShape.PAPER, MyShape.SCISSORS) | (
            ElfShape.SCISSORS,
            MyShape.ROCK,
        ):
            return 6
        case (ElfShape.ROCK, MyShape.ROCK) | (ElfShape.PAPER, MyShape.PAPER) | (
            ElfShape.SCISSORS,
            MyShape.SCISSORS,
        ):
            return 3
        case _:
            return 0


def compute_one_score(round: str, part: int = 1) -> int:
    """
    Compute the score of one Rock Paper Scissors match.

    Args:
        round: string description of a round
        part: 1 to compute part 1 score 2 to compute part 2 score

    Returns:
        the score of the outcome of the match
    """
    elf, me = round.split(ORDER_SEP)
    if part == 1:
        return outcome_score(elf, me) + shape_score(me)
    else:
        return outcome_score(elf, SHAPE_TO_PLAY[elf, me]) + shape_score(
            SHAPE_TO_PLAY[elf, me]
        )


def compute_all_scores(round_list: str, part: int = 1) -> list[int]:
    """
    Compute all scores for a whole strategy list.

    Args:
        round_list: Strategy list for all the rounds
        part: 1 to compute part 1 score 2 to compute part 2 score

    Returns:
        a list of all the scores for a given strategy list.
    """
    rounds = list(round_list.split(ROUND_SEP))
    return [compute_one_score(fight, part) for fight in rounds]


def compute_global_score(round_list: str, part: int = 1) -> int:
    """
    Answer the day 1 part 1 challenge question.

    Args:
        round_list: Strategy list for all the rounds
        part: 1 to compute part 1 score 2 to compute part 2 score

    Returns:
        the total score of all the rounds
    """
    return sum(compute_all_scores(round_list, part))


def main():
    """Script to answer the question, with style."""
    console = Console()

    with (
        open(BASE_DIR / "day02_part1.md") as part_one,
        open(BASE_DIR / "day02_part2.md") as part_two,
        open(BASE_DIR / "strategy_guide.data") as strat_f,
    ):
        strat_list = strat_f.read()
        console.print(Markdown(part_one.read()))

        console.print()

        score_1 = compute_global_score(strat_list)

        console.print(f"Hypothetic score: {score_1}", justify="center")

        console.print()

        console.print(Markdown(part_two.read()))

        console.print()

        score_2 = compute_global_score(strat_list, part=2)

        console.print(f"Less hypothetic score: {score_2}", justify="center")


if __name__ == "__main__":
    main()
