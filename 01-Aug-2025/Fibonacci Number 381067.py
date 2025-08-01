# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo={0:0, 1:1}

        def f(h):
            if h in memo:
                return memo[h]
            else:
                memo[h]= f(h-1) + f(h-2)
                return memo[h]
        return f(n)
        