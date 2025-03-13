# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[l]=nums[i]
                l+=1
        # if nums[-1]==val:
        #     l+=1
        # nums=nums[:l]
        return l