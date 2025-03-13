# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        g.sort()
        s.sort()
        for i in s:
            if c<len(g) and g[c] <= i:
               c+=1
        return c