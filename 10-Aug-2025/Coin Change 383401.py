# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        dp = [float('inf')] * (amt + 1)
        dp[0] = 0  
        
        for i in range(1, amt + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[amt] if dp[amt] != float('inf') else -1