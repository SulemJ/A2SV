# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy1=buy2=float('-inf')
        sell1 = sell2 = 0

        for stack in p:
            buy1=max(buy1, -stack)
            sell1=max(sell1, stack+buy1)
            buy2=max(buy2, sell1-stack)
            sell2=max(sell2, stack+buy2)

        return sell2        
        