# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n,m=len(matrix),len(matrix[0])
        a=[[0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
                a[i][j]=matrix[j][i]
        return a