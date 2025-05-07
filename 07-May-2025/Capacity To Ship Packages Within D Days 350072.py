# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, w: List[int], d: int) -> int:
        l,r=max(w),sum(w)
        res=r
        def possible(x):
            space,summ=1,x
            for i in w:
                if summ-i < 0:
                    space+=1
                    summ=x
                summ -= i
            return space<=d

        while l<=r:
            m=(l+r) // 2
            if possible(m):
                res=min(res, m)
                r=m-1
            else:
                l=m+1
        return res
        
