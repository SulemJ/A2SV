# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        
        """
        k=1
        i,j=0,1
        while j<len(nums):
            if nums[i] <nums[j]:
                if j-i==1:
                    k+=1
                    i+=1
                    j+=1
                else:
                    nums[i+1],nums[j]=nums[j],nums[i+1]
                    k+=1
                    i+=1
                    j+=1
            else:
                j+=1
        return k