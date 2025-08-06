# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums= [[]]*numRows

        for i in range(numRows):
            nums[i]=[1]*(i+1)
            for j in range(1,i):
               nums[i][j] = nums[i][i-j] =nums[i-1][j-1]+nums[i-1][j]
        return nums