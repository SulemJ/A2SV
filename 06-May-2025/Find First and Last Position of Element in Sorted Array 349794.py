# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l,r=0,len(nums)-1
        a=[]
        f=False
        while l<=r:
            m=(l+r)//2
            if nums[m]<t:
                l=m+1
            else:
                if nums[m]==t:
                    f=True
                r=m-1
            
        a.append(l)
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>t:
                r=m-1
            else:
                if nums[m]==t:
                    f=True
                l=m+1
        a.append(r)
        return a if f else [-1,-1]