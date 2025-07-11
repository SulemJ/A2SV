# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(path, j):
            if len(path)==k:
                res.append(path[:])
                return
            for i in range(j, n+1):
                path.append(i)
                backtrack(path, i+1)
                path.pop()

        res=[]
        backtrack([],1)
        return res