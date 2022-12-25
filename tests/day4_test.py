"""Tests for day 4 puzzle."""

from pathlib import Path

import pytest
from assertpy import assert_that

from pymaoc2022.day04 import WorkRange, is_overlapped, nb_overlap, parse_line

TEST_DIR = Path(__file__).parent


@pytest.mark.parametrize(
    "big, small, expected",
    [
        (WorkRange(1, 9), WorkRange(3, 6), True),
        (WorkRange(1, 9), WorkRange(1, 3), True),
        (WorkRange(1, 9), WorkRange(6, 9), True),
        (WorkRange(4, 6), WorkRange(4, 6), True),
        (WorkRange(4, 6), WorkRange(1, 3), False),
        (WorkRange(1, 3), WorkRange(4, 6), False),
        (WorkRange(4, 6), WorkRange(3, 5), False),
        (WorkRange(4, 6), WorkRange(5, 7), False),
        (WorkRange(4, 6), WorkRange(3, 7), False),
    ],
)
def test_fully_contains(  # noqa: D103
    big: WorkRange, small: WorkRange, expected: bool  # noqa: FBT001
):
    assert_that(big.fully_contains(small)).is_equal_to(expected)


@pytest.mark.parametrize(
    "a, b, c, d",
    [(1, 2, 3, 4), (1, 6, 4, 9), (10, 20, 30, 40)],
)
def test_parse_line(a: int, b: int, c: int, d: int):  # noqa: D103
    line = f"{a}-{b},{c}-{d}"
    expected = (WorkRange(a, b), WorkRange(c, d))

    assert_that(parse_line(line)).is_equal_to(expected)


@pytest.mark.parametrize(
    "line, expected",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", False),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", False),
    ],
)
def test_is_overlapped(line: str, expected: bool):  # noqa: D103 FBT001
    assert_that(is_overlapped(line)).is_equal_to(expected)


def test_nb_overlap():  # noqa: D103
    with open(TEST_DIR / "pair_assignments_sample.data") as assignments_list:
        assignments = assignments_list.read()
        overlaps = nb_overlap(assignments)

        assert_that(overlaps).is_equal_to(2)
