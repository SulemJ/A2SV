# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums.sort()
        #  [-1,4,5,7,8]
        l,r=0,0
        m=nums[0]
        c=nums[0]
        for i in range(1,len(nums)):
            m=max(nums[i], nums[i]+m)
            c=max(m,c)
        return c     