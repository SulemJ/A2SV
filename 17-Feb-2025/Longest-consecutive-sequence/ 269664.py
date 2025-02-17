# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxx=0
        c=1
        if nums==[0]:
            return 1
        elif nums== []:
            return 0
        for i in range(1, len(nums)):
            if nums[i]-(nums[i-1]) == 1:
                c+=1
            elif nums[i]-(nums[i-1]) == 0:
                continue
            else:
                c=1
            maxx=max(maxx,c)    
        return max(maxx,c)   