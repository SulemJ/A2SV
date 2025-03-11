# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        l=0
        nums=set(nums)
        for i in nums:
            p=2 
            c=1
            while i**p in nums:
                c+=1
                i=i**p
            l=max(l,c)
        return l if l>1 else -1



