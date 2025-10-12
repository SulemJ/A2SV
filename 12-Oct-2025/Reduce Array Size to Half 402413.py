# Problem: Reduce Array Size to Half - https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = sorted(Counter(arr).values(), reverse=True)
        removed = 0
        target = len(arr) // 2
        cnt = 0
        for c in counts:
            removed += c
            cnt += 1
            if removed >= target:
                return cnt
        return cnt