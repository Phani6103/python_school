"""
Implementation of the "Longest Common Prefix" problem from LeetCode.
"""

from __future__ import annotations

from typing import Iterable, List


class LongestCommonPrefix:
    """Utility for computing the longest shared prefix across a collection of strings."""

    def find_prefix(self, words: Iterable[str]) -> str:
        """Return the longest prefix common to every string in ``words``."""
        word_list: List[str] = list(words)
        if not word_list:
            return ""

        prefix = word_list[0]
        for word in word_list[1:]:
            while not word.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix


if __name__ == "__main__":
    examples = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["", ""],
    ]
    solver = LongestCommonPrefix()
    for case in examples:
        print(case, "->", solver.find_prefix(case))
