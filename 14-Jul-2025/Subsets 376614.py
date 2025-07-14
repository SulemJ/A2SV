# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
                return

            backtrack(i+1)

            path.append(nums[i])
            backtrack(i+1)
            path.pop()

        backtrack(0)
        return res    
