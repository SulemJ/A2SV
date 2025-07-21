# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = Counter(a + b for a in nums1 for b in nums2)
        return sum(d[-(c + d2)] for c in nums3 for d2 in nums4)