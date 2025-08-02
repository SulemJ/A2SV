# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sma=[]
        gr=[]
        eq=[]
        for i in nums:
            if i == pivot:
                eq.append(i)
            elif i > pivot:
                gr.append(i)
            else:
                sma.append(i)
        return sma+eq+gr