# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        a=SortedList()
        l,c=0,0
        for i,x in enumerate(nums):
            a.add(x)
            while a and (a[-1]-a[0])>2:
                a.remove(nums[l])
                l+=1
            c+=(i-l+1)
        return c