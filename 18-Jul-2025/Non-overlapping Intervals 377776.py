# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2],[1,3],[2,3],[3,4]]
        intervals.sort()
        ans=0
        ch=intervals[0][1]
        for start,end in intervals[1:]:
            if start < ch:
                # if intervals[i][1]<ch:
                ch= min(end, ch)
                ans+=1
            else:
                ch= end
        return ans
                