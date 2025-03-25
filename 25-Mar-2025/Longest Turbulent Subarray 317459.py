# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1: return len(arr)
        prev = 0 if arr[1] == arr[0] else 1 if arr[1] > arr[0] else -1
        streak = maxLen = 1 if prev == 0 else 2
        for i in range(2, len(arr)):
	        cur = 0 if arr[i] == arr[i-1] else 1 if arr[i] > arr[i-1] else -1
	        streak = 1 if cur == 0 else 2 if cur == prev else streak + 1
	        maxLen = max(maxLen, streak)
	        prev = cur
        return maxLen