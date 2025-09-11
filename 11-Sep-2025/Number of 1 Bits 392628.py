# Problem: Number of 1 Bits - https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        ans=0
        for i in binary:
            ans+=int(i)

        return ans