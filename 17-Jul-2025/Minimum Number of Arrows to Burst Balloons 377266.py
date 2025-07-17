# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        a = 1
        temp = points[0][1]
        i = 1
        while i < len(points):
            if points[i][0] > temp:
                a += 1
                temp = points[i][1]
            i += 1
        return a
