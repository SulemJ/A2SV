# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[-n for n in nums]
        heapq.heapify(h)
        for _ in range(k-1):
            heapq.heappop(h)
        return -heapq.heappop(h)