# Problem: Minimum Number of Valid Strings to Form Target I - https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-i/description/

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root={}
        for w in words:
            node = root
            for ch in w:
                if ch not in node:
                    node[ch] = {}

                node = node[ch]
        n = len(target)
        dp= [float('inf')] * (n+1)
        dp[n]=0
        for i in range(n-1, -1,-1):
            node =root
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1+dp[j+1])
        return dp[0] if dp[0] != float('inf') else -1    