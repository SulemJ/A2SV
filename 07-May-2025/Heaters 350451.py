# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        min_dist=0
        heaters.sort()
        for b in houses:
            l,r=0,len(heaters)-1
            close=float('inf')
            while l<=r:
                m=(l+r)//2
                close=min(close,abs(heaters[m]-b))
                if heaters[m] < b:
                    l=m+1
                else:
                    r=m-1
            min_dist=max(min_dist,close)
        return min_dist 