# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        def dp(i):
            if i not in memo:
                memo[i]=max(dp(i-1), dp(i-2)+nums[i])
            return memo[i]
        memo={0:nums[0], 1:max(nums[0],nums[1])}
        return dp(n-1)