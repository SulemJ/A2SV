# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a=[intervals[0]]
        for i in intervals[1:]:
            if i[0]<=a[-1][1]:
                a[-1][1]=max(a[-1][1],i[1])
            else:
                a.append(i)
        return a