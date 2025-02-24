# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1 and n not in s:
            s.add(n)
            n= sum(int(i)*int(i) for i in str(n))
        return n==1
