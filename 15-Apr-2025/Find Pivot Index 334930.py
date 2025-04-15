# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=[]
        b=[0]*(len(nums))
        d=0
        c=0
        for i in nums:
            c+=i
            a.append(c)
        for i in range(len(nums)-1,-1,-1):
            d+=nums[i]
            b[i]=d
        for i in range(len(nums)):
            if a[i]==b[i]:
                return i
        return -1