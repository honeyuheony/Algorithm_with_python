# leetcode medium Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        str_temp = ''
        start = 0
        for end, char in enumerate(s):
            str_temp += char
            if Counter(str_temp).most_common(1)[0][1] == 1:
                max_length = max(max_length, end-start+1)
            else:
                while Counter(str_temp).most_common(1)[0][1] != 1:
                    start += 1
                    str_temp = str_temp[1:]
        return max_length