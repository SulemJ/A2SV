# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        n=len(nums)
        l,k=0,0
        s=0
        c=float('inf')
        for i in range(n):
            s+=nums[i]
            while s>=t:
                c=min(c, i-l+1)
                s-=nums[l]
                l+=1
                
        return 0 if c==float('inf') else c











