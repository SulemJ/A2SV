# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n,m= len(matrix),len(matrix[0])
        matrix.reverse()
        for i in range(n):
            for j in range(i+1,m):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
