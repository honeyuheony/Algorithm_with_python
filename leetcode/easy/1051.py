# leetcode easy Height Checker
# https://leetcode.com/problems/height-checker/

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 for a, b in zip(heights, sorted(heights)) if a != b])
