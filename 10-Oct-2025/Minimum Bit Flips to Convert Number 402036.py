# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=0
        while start > 0 or goal > 0:
            if(start & 1) != (goal & 1):
                ans+=1
            start >>= 1
            goal >>= 1
        return ans