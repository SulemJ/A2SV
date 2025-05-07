# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l,r=1,max(nums)
        nums.sort()
        res=0
        while l<=r:
            m=(l+r)//2
            k=sum(ceil(i/m) for i in nums)
            if k<=threshold:
                res=m
                r=m-1
            else:
                l=m+1
        return res