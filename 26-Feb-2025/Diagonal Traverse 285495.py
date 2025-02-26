# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        0,0 - 0,1 1,0 - 2,0 1,1 0,2 - 1,2 2,1 - 2,2
        

        """
        a=[]
        n,m= len(mat), len(mat[0])
        d= defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i+j].append(mat[i][j])
                # print(i+j)
        for i,x in d.items():
            if i%2==0:
                v=list(reversed(x))
                for j in v:
                    a.append(j)
                # print(v)
            else:
                for j in x:
                    a.append(j)
        return a
