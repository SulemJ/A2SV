# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        i=0
        while i<len(nums):
            if nums[i] !=0:
                nums[l]=nums[i]
                l+=1
            i+=1
        for i in range(1,(len(nums)-l)+1):
            nums[-i]=0
            # h=l+1
            # if nums[l] ==0:
            #     while h ==0 and h<len(nums)-1:
            #         h+=1
            #     nums[l],nums[h]=nums[h],nums[l]
            #     # r-=1
            # l+=1