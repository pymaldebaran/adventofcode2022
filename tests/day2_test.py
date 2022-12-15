"""Tests for the day 1."""

from pathlib import Path

import pytest
from assertpy import assert_that

from pymaoc2022.day02 import (
    ElfShape,
    MyShape,
    compute_all_scores,
    compute_global_score,
    outcome_score,
    shape_score,
)

TEST_DIR = Path(__file__).parent


@pytest.mark.parametrize(
    "shape, result", [(MyShape.ROCK, 1), (MyShape.PAPER, 2), (MyShape.SCISSORS, 3)]
)
def test_shape_score(shape: MyShape, result: int):  # noqa: D103
    assert_that(shape_score(shape)).is_equal_to(result)


@pytest.mark.parametrize(
    "elf, me",
    [
        (ElfShape.ROCK, MyShape.ROCK),
        (ElfShape.PAPER, MyShape.PAPER),
        (ElfShape.SCISSORS, MyShape.SCISSORS),
    ],
)
def test_outcome_score_tie(elf: ElfShape, me: MyShape):  # noqa: D103
    assert_that(outcome_score(elf, me)).is_equal_to(3)


@pytest.mark.parametrize(
    "strong, weak",
    [
        (ElfShape.ROCK, MyShape.SCISSORS),
        (ElfShape.PAPER, MyShape.ROCK),
        (ElfShape.SCISSORS, MyShape.PAPER),
    ],
)
def test_outcome_score_loose(strong: ElfShape, weak: MyShape):  # noqa: D103
    assert_that(outcome_score(elf=strong, me=weak)).is_equal_to(0)


@pytest.mark.parametrize(
    "weak, strong",
    [
        (ElfShape.SCISSORS, MyShape.ROCK),
        (ElfShape.ROCK, MyShape.PAPER),
        (ElfShape.PAPER, MyShape.SCISSORS),
    ],
)
def test_outcome_score_win(weak: ElfShape, strong: MyShape):  # noqa: D103
    assert_that(outcome_score(elf=weak, me=strong)).is_equal_to(6)


def test_compute_all_scores():  # noqa: D103
    with open(TEST_DIR / "strategy_guide_sample.data") as strat:
        score = compute_all_scores(strat.read())

        assert_that(score).is_length(3)
        assert_that(score).is_equal_to([8, 1, 6])


def test_compute_global_score():  # noqa: D103
    with open(TEST_DIR / "strategy_guide_sample.data") as strat:
        score = compute_global_score(strat.read())
        assert_that(score).is_equal_to(15)
