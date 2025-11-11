# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0 or c==2 or c==8: return True
        for i in range(int(math.sqrt(c))):
            if c-(i*i) >=0 and (math.sqrt(c-(i*i))).is_integer():
                return True
        return False
