# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n= len(matrix)
        dp=[[0]* n for _ in range(n)]

        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(n):
                down= dp[i+1][j]
                left=dp[i+1][j-1] if j>0 else float('inf')
                right=dp[i+1][j+1] if j<n-1 else float('inf')
                dp[i][j]= matrix[i][j] + min(down, left, right)
        return min(dp[0])

        # def dfs(r,c):
        #     if r == n:
        #         return 0
        #     if c < 0 or c ==n:
        #         return float('inf')
        #     if (r,c) in cache:
        #         return cache[(r,c)]
            
        #     res = matrix[r][c] + min(
        #         dfs(r+1, c-1),
        #         dfs(r+1, c),
        #         dfs(r+1, c+1)
        #     )
        #     cache[(r,c)] = res
        #     return res

        # res = float('inf')
        # for c in range(n):
        #     res = min(res, dfs(0,c))

        # return res
        