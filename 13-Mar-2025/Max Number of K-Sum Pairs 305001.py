# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c=0
        nums.sort()
        l,r=0,len(nums)-1
        while l<r:
            su=nums[l]+nums[r]
            if su<k:
                l+=1
            elif su>k:
                r-=1
            else:
                c+=1
                l+=1
                r-=1
        return c