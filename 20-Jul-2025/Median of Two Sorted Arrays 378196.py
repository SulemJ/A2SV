# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        j=0
        f = [0] *(len(nums1)+len(nums2))
        for i in nums1:
            f[j]= i 
            j+=1
        for i in nums2:
            f[j] = i 
            j+=1
        f.sort()
        if len(f) % 2 == 0:
            median = (f[len(f)//2 - 1] + f[len(f)//2]) / 2
        else:
            median = f[len(f)//2]
        return median