"""Tests for the day 1."""

from pathlib import Path

import pytest
from assertpy import assert_that

from pymaoc2022.day03 import (
    all_badges_priorities,
    all_misplaced_priorities,
    badge_item,
    compute_total_priorities,
    misplaced_item,
    one_badge_priority,
    one_misplaced_priority,
    priority,
    split_in_half,
)

TEST_DIR = Path(__file__).parent


@pytest.mark.parametrize(
    "content, expect_left, expect_right",
    # cSpell:disable
    [("ab", "a", "b"), ("abcdef", "abc", "def"), ("abcdefghijkl", "abcdef", "ghijkl")],
    # cSpell:enable
)
def test_split_in_half(content: str, expect_left: str, expect_right: str):  # noqa: D103
    res = split_in_half(content)

    assert_that(res).is_length(2)

    left, right = res
    assert_that(left).is_equal_to(expect_left)
    assert_that(right).is_equal_to(expect_right)


@pytest.mark.parametrize(
    "content, misplaced",
    # cSpell:disable
    [
        ("abczdefz", "z"),
        ("ABCZDEFZ", "Z"),
        ("aaaybbby", "y"),
        ("AAAYBBBY", "Y"),
        ("XaaabbbXcccddd", "X"),
        ("abcXdefghijkXl", "X"),
    ],
    # cSpell:enable
)
def test_misplaced_item(content: str, misplaced: int):  # noqa: D103
    assert_that(misplaced_item(content)).is_equal_to(misplaced)


@pytest.mark.parametrize(
    "item, expected_priority", [("a", 1), ("z", 26), ("A", 27), ("Z", 52)]
)
def test_priority(item: str, expected_priority: int):  # noqa: D103
    assert_that(priority(item)).is_equal_to(expected_priority)


@pytest.mark.parametrize(
    "rucksack, priority",
    # cSpell:disable
    [
        ("abczdefz", 26),
        ("ABCZDEFZ", 52),
        ("aaaybbby", 25),
        ("AAAYBBBY", 51),
        ("XaaabbbXcccddd", 50),
        ("abcXdefghijkXl", 50),
    ],
    # cSpell:enable
)
def test_one_misplaced_priority(rucksack: str, priority: int):  # noqa: D103
    assert_that(one_misplaced_priority(rucksack)).is_equal_to(priority)


def test_all_misplaced_priorities():  # noqa: D103
    with open(TEST_DIR / "rucksack_contents_sample.data") as rucksack_list:
        rucksacks = rucksack_list.read()
        priorities = all_misplaced_priorities(rucksacks)

        assert_that(priorities).is_length(6)
        assert_that(priorities).is_equal_to([16, 38, 42, 22, 20, 19])


def test_compute_total_priorities_part1():  # noqa: D103
    with open(TEST_DIR / "rucksack_contents_sample.data") as rucksack_list:
        rucksacks = rucksack_list.read()
        total = compute_total_priorities(rucksacks)

        assert_that(total).is_equal_to(157)


@pytest.mark.parametrize(
    "group, badge",
    # cSpell:disable
    [
        (["Zabc", "deZfg", "hijklZ"], "Z"),
        (["aYbc", "Ydefg", "hijkYl"], "Y"),
        (["XZabc", "XYZdefg", "XYhijkl"], "X"),
    ],
    # cSpell:enable
)
def test_badge_item(group: list[str], badge: str):  # noqa: D103
    assert_that(badge_item(group)).is_equal_to(badge)


@pytest.mark.parametrize(
    "group, priority",
    # cSpell:disable
    [
        (["Zabc", "deZfg", "hijklZ"], 52),
        (["aYbc", "Ydefg", "hijkYl"], 51),
        (["XZabc", "XYZdefg", "XYhijkl"], 50),
    ],
    # cSpell:enable
)
def test_one_badge_priority(group: list[str], priority: int):  # noqa: D103
    assert_that(one_badge_priority(group)).is_equal_to(priority)


def test_all_badges_priorities():  # noqa: D103
    with open(TEST_DIR / "rucksack_contents_sample.data") as rucksack_list:
        rucksacks = rucksack_list.read()
        priorities = all_badges_priorities(rucksacks)

        assert_that(priorities).is_length(2)
        assert_that(priorities).is_equal_to([18, 52])


def test_compute_total_priorities_part2():  # noqa: D103
    with open(TEST_DIR / "rucksack_contents_sample.data") as rucksack_list:
        rucksacks = rucksack_list.read()
        total = compute_total_priorities(rucksacks, part=2)

        assert_that(total).is_equal_to(70)
