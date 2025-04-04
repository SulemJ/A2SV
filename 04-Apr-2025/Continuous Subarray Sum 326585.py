# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        l=0
        for i,x in enumerate(nums):
            l+=x
        # l=(c%k)
            c=(l%k)
            if c not in d:
                d[c]=i
            elif c in d and i-d[c]>1:
                return True
        return False        
















        # l=0
        # while l<len(nums):
        #     r=l+1
        #     c=nums[l]
        #     while r<len(nums):
        #         c+=nums[r]
        #         if (c % k)==0:
        #             return True
        #         r+=1
        #     l+=1
        # return False

