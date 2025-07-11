# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in range(min(k,len(matrix))):
            heapq.heappush(heap,(matrix[i][0],i,0))
        while k:
            num,r,c=heapq.heappop(heap)
            if c+1<len(matrix[r]):
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
            k-=1
        return num