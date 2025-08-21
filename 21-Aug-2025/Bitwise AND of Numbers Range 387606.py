# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count=0
        while left != right:
            count+=1
            left >>=1
            right >>=1
        return right << count
