# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        for i in t:
            if i in s:
                s.remove(i)
            elif i not in s:
                return i