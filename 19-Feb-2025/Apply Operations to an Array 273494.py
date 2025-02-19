# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n= len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        s = list(filter(lambda a: a != 0, nums))
        for i in range(n-len(s)):
            s.append(0)
        return s