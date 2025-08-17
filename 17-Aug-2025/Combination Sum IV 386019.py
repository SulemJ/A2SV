# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(n=0):
            if n >= target:
                return n==target
            
            res=0
            for num in nums:
                res+=dp(n+num)
            return res
        return dp()