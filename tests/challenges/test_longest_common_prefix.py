import pytest

from python_school.challenges.longest_common_prefix import LongestCommonPrefix


@pytest.fixture
def solver() -> LongestCommonPrefix:
    return LongestCommonPrefix()


def test_common_prefix_found(solver: LongestCommonPrefix) -> None:
    assert solver.find_prefix(["flower", "flow", "flight"]) == "fl"


def test_no_common_prefix_returns_empty(solver: LongestCommonPrefix) -> None:
    assert solver.find_prefix(["dog", "racecar", "car"]) == ""


def test_single_word_returns_word(solver: LongestCommonPrefix) -> None:
    assert solver.find_prefix(["prefix"]) == "prefix"


def test_handles_empty_strings(solver: LongestCommonPrefix) -> None:
    assert solver.find_prefix(["", ""]) == ""
    assert solver.find_prefix(["prefix", ""]) == ""


def test_empty_iterable_returns_empty(solver: LongestCommonPrefix) -> None:
    assert solver.find_prefix([]) == ""
