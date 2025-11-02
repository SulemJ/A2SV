# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        ans=[i for i in nums if i!=0]
        for i in range(len(nums)-len(ans)):
            ans.append(0)
        return ans