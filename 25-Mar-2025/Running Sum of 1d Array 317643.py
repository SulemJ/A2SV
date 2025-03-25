# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        som=[0]
        for i in range(len(nums)):
            som.append(som[-1]+nums[i])
        return som[1:]