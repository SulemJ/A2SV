# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix),len(matrix[0])
        ar=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ar.add((i,j))
        for i,j in ar: 
            for v in range(n):
                matrix[i][v]=0
                for v in range(m):
                    matrix[v][j]=0