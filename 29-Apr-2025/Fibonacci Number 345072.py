# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        # if n==1:
        #     return 1
        # if n==0:
        #     return 0
        # a=self.fib(n-1)
        # b=self.fib(n-2)
        a=[0,1]
        for i in range(2,n+1):
            a.append(a[i-1] + a[i-2])
        return a[n]
