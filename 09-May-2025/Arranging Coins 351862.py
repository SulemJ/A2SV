# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        n * (n + 1) / 2
        """
        l,r=1,n
        a=0
        while l<=r:
            m=(r+l)//2
            if m*(m+1)//2>n:
                r=m-1
            elif m*(m+1)//2<n:
                a=m
                l=m+1
            else:
                return m
        return a