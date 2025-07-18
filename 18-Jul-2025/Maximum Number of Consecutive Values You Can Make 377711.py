# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # 1,4,10,3,1
        # 1 2 5 9 19
        # 1 1 3 4 10
        coins.sort()
        goal =1
        for i in coins:
            if goal - i<0:
                break
            goal+=i
        return goal 