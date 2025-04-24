# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=[]
        b=defaultdict(lambda:-1)
        for i,x in enumerate(nums2):
            while s and s[-1]<x:
                b[s[-1]]=x
                s.pop()
            s.append(x)
        return [b[i] for i in nums1]        