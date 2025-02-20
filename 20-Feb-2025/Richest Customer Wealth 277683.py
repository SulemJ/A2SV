# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx= 0
        for i in accounts:
            maxx=max(maxx,sum(i))
        return maxx