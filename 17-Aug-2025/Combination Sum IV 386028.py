# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1
        for i in range(target+1):
            for n in nums:
                dp[i]+=dp[i-n]
        return dp[target]