# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        # pr=[]
        while True:
            num, reduced =n,0
            for i in range(2, num+1):
                while num%i==0:
                    num//=i
                    reduced+=i
            if reduced == n:
                break
            n=reduced
        return n