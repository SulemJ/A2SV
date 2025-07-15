# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 10 2 1 1
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2] and nums[i+2]+nums[i+1]>nums[i] and nums[i]+nums[i+2]>nums[i+1]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0