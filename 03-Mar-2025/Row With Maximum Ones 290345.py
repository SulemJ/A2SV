# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        f= defaultdict(int)
        for i in range(len(mat)):
            f[i]=mat[i].count(1)

        v=max(x for i,x in f.items())
        # c=0
        for i,x in f.items():
            if x == v:
                return [i,x]
