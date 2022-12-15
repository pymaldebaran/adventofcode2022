"""Tests for the day 1."""

from pathlib import Path

from assertpy import assert_that, soft_assertions

from pymaoc2022.day01 import most_calorie_elf, most_calorie_elves

TEST_DIR = Path(__file__).parent


def test_most_calorie_elf():  # noqa: D103
    with open(TEST_DIR / "calories_list_sample.data") as cal_list:
        pkg = most_calorie_elf(cal_list.read())

    with soft_assertions():
        assert_that(pkg.elf).is_equal_to(4)
        assert_that(pkg.cal).is_equal_to(24000)


def test_most_calorie_three_elves():  # noqa: D103
    with open(TEST_DIR / "calories_list_sample.data") as cal_list:
        result = most_calorie_elves(cal_list.read())

    assert_that(len(result)).is_greater_than_or_equal_to(3)
    with soft_assertions():
        assert_that(result[0].elf).is_equal_to(4)
        assert_that(result[0].cal).is_equal_to(24000)
        assert_that(result[1].elf).is_equal_to(3)
        assert_that(result[1].cal).is_equal_to(11000)
        assert_that(result[2].elf).is_equal_to(5)
        assert_that(result[2].cal).is_equal_to(10000)
