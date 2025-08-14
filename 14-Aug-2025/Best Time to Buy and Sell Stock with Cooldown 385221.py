# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # @cache
        memo={}
        def dp(i, state):
            if i >= len(prices): return 0
            if (i,state) in memo: return memo[(i,state)]
            match state:
                case 'buy':
                    res= max(
                        dp(i+1, 'sell') - prices[i],
                        dp(i+1, 'buy')
                    )
                case 'sell':
                    res= max(
                        dp(i+1, 'sell'),
                        dp(i+1, 'cooldown') + prices[i]
                    )
                case _:
                    res= dp(i+1, 'buy')
                
            memo[(i,state)] = res
            return res
        return dp(0, 'buy')