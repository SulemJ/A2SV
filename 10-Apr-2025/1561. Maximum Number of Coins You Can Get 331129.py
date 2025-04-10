# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a=0
        k=len(piles)//3
        i=1
        while k >0:
            a+=piles[-(i*2)]
            i+=1
            k-=1
        return a