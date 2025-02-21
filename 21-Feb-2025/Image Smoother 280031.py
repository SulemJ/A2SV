# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        0,0 - 1,1
        0,2 - 0,1 0,3 -1,1- 1,2 1,3  -1,2 -1,1, -1,3
        




        """
        m,n = len(img), len(img[0])
        r=[[0]*n for _ in range(m) ]
        for i in range(m):
            for j in range(n):
              s = [img[x][y] for x in (i-1, i, i+1) for y in (j-1, j, j+1) if 0 <= x < m and 0 <= y < n]
              r[i][j]=sum(s) // len(s)
        return r
                