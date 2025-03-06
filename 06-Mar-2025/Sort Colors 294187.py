# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        for i in range(n):
            m=i
            for j in range(i+1,n):
                if nums[m]>=nums[j]:
                    m=j
            nums[i],nums[m]=nums[m],nums[i]