# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [4,2,4,0,0,3,0,5,1,0]

        i,j=0,0
        while j<len(nums) and i<len(nums):
            if nums[j] != 0:
                # if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1
            