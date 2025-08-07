# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t=[]
        for i in range(rowIndex+1):
            row = [1] * (i+1)

            for j in range(1, i):
                row[j] = t[i-1][j] + t[i-1][j-1]
            t.append(row)
        return t[-1]