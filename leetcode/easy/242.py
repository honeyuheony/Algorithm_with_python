# leetcode easy Valid-Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for c1, c2 in zip(s, t):
            if c1 in char_dict.keys():
                char_dict[c1] += 1
            else:
                char_dict[c1] = 1
            if c2 in char_dict.keys():
                char_dict[c2] -= 1
            else:
                char_dict[c2] = -1
 
        for c in char_dict.values():
            if c != 0:
                return False
        return True
                