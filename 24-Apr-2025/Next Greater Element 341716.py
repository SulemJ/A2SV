# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums1)):
            c=0
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums2[j]>nums1[i]:
                    a.append(nums2[j])
                    c+=1
                    break
            if c==0:
                a.append(-1) 
        return a  