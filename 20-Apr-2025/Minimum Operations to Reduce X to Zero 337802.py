# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        t=sum(nums)-x
        cur_sum=0
        maxx=-1
        l=0
        for r in range(len(nums)):
            cur_sum+=nums[r]
            while l<=r and cur_sum>t:
                cur_sum-=nums[l]
                l+=1
            if cur_sum == t:
                maxx=max(maxx,r-l+1)
        return -1 if maxx ==-1 else len(nums)-maxx
        
