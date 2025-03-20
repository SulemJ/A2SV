# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >0 and len(nums)>1 and k!=len(nums):
            k=k%len(nums)
            nums[:]=nums[-k:]+nums[:len(nums)-k]
        # nums=nums
        # for i in range(len(n)-k):
        #     n.append(n[i])
        # n[:]=n[k-1:]