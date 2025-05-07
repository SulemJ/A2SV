# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        # a=-1
        while l<=r:
            m=(l+r)//2
            if target<matrix[m][0]:
                r=m-1
            elif target>matrix[m][-1]:
                l=m+1
            else:
                break
        if not l<=r:
            return False
        c=(l+r)//2
        a,b=0,len(matrix[l])-1
        while a<=b:
            m=(a+b)//2
            if target<matrix[c][m]:
                b=m-1
            elif target>matrix[c][m]:
                a=m+1
            else:
                return True
        return False
