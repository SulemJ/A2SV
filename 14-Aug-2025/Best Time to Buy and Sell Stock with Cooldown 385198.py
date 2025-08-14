# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, state):
            if i >= len(prices): return 0

            match state:
                case 'buy':
                    return max(
                        dp(i+1, 'sell') - prices[i],
                        dp(i+1, 'buy')
                    )
                case 'sell':
                    return max(
                        dp(i+1, 'sell'),
                        dp(i+1, 'cooldown') + prices[i]
                    )
                case _:
                    return dp(i+1, 'buy')
        return dp(0, 'buy')