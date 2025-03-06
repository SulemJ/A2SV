# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums= list(set(nums))
        for i in range(len(nums)):
            m=i
            for j in range(i+1,len(nums)):
                if nums[m]>=nums[j]:
                    m=j
            nums[i],nums[m]= nums[m],nums[i]
        if len(nums)>2:
            return nums[-3]
        else:
            return nums[-1]