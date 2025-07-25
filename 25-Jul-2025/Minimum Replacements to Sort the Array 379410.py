# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # return 0 if nums==sorted(nums)
        n=len(nums)
        ans=0
        last=nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]>last:
                t= nums[i]//last
                if nums[i]%last:
                    t+=1
                last= nums[i] // t
                ans+=(t-1)
            else:
                last= nums[i]
        return ans
