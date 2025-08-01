# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 2  3 4 5 6 7 8 9
        # 1 2  3 5 
        if n==1:
            return 1
        if n==2:
            return 2
        prev=1
        cur=2
        for i in range(2,n):
            prev,cur=cur, prev+cur

        return cur