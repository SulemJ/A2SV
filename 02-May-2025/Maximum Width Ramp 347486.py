# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n=len(nums)
        pre_max=[0]*n
        maxx=0
        for i in range(n-1,-1,-1):
            maxx=max(maxx,nums[i])
            pre_max[i]=maxx
        max_wdt=l=0
        for r in range(n):
            if nums[l]>pre_max[r]:
                l+=1
            max_wdt=max(max_wdt,r-l)
        return max_wdt