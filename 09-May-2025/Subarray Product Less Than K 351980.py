# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        product=1
        l=0
        ans=0
        for right in range(len(nums)):
            product*=nums[right]
            while product>=k:
                product//=nums[l]
                l+=1
            ans+=right-l+1
        return ans        