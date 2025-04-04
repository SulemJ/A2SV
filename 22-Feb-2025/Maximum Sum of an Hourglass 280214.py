# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        a=0
        for i in range(n-2):
            for j in range(m-2):
                x =  [grid[x][y] for x in (i,i+1,i+2) for y in (j,j+1,j+2) if 0 <= x < n and 0 <= y < m]
                s = sum(x)- grid[i+1][j]-grid[i+1][j+2]
                a=max(a,s)
        return a