# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, g: List[List[int]], t: List[int]) -> bool:
        a=[abs(g[i][0]-t[0])+abs(g[i][1]-t[1]) for i in range(len(g))]
        c=abs(t[0])+abs(t[1])
        for i in a:
            if i<=c:
                return False
        return True