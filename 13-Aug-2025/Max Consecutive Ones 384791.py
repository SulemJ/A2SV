# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # if not nums:
        #     return ''
        f=nums[0]
        for i in range(1,len(nums)):
            if nums[i] ==0:
                f=0
            f+=nums[i]
            nums[i]=f
        return max(nums)
