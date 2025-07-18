# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:

        def dfs(idx, prev):
            if idx==len(s):
                return True
            for j in range(idx, len(s)):
                v=int(s[idx:j+1])
                if v+1==prev and dfs(j+1, v):
                    return True
            return False
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1, val): return True
        
        return False 