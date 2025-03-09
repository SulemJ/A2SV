# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S= Counter(s)
        T= Counter(t)
        if T == S:
            return True
        else:
            return False