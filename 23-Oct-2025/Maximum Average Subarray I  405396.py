# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ= sum(nums[:k])
        maxx= summ
        for i in range(k, len(nums)):
            summ+=nums[i]
            summ-=nums[i-k]
            maxx=max(summ, maxx)
        return maxx/k