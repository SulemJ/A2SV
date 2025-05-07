# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        l,r=1,max(piles)
        res=r
        def possible(m):
            th=0
            for b in piles:
                th+=max(1,ceil(b/m))
            return th<=h
        while l<=r:
            m=(l+r)//2
            if possible(m):
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res