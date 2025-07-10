# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a=0 
        h=[-s for s in stones]
        heapq.heapify(h)
        while len(h) >1:
            l=-heapq.heappop(h)
            k=-heapq.heappop(h)
            if (l-k)>0:
                heapq.heappush(h,-(l-k))
        return -h[0] if len(h) >=1 else 0