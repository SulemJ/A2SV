# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        c=2
        co=0
        while c<n:
            if n%c==0:
                co+=1
            c+=1
        return True if co ==1 else False