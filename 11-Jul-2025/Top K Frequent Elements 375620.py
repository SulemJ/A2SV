# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        heap=[]
        for key,value in c.items():
            if len(heap)<k:
                heapq.heappush(heap,(value,key))
            else:
                heapq.heappushpop(heap,(value,key))


        return [h[1] for h in heap]