# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums= list(set(nums))
        nums.sort()
        if len(nums)>2:
            return nums[-3]
        else:
            return nums[-1]