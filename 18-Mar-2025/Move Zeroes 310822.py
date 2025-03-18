# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l=0
        # i=0
        # while i<len(nums):
        #     if nums[i] !=0:
        #         nums[l]=nums[i]
        #         l+=1
        #     i+=1
        # for i in range(1,(len(nums)-l)+1):
        #     nums[-i]=0
           

        i,j=0,1
        while j<len(n):
            if n[i]!=0:
                i+=1
                j+=1
            else:
                if n[j]!=0:
                    n[i],n[j]=n[j],n[i]
                    i+=1
                    j+=1
                else:
                    j+=1
                    