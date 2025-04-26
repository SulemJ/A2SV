# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,c=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                l=(i+1)
            c=max(c,i-l+1)
        return c