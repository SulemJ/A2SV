# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        use counter
        for i in counter fill nums[i] with co[i] leave the rest as it is
        """
        c=Counter(nums)
        for i,x in enumerate(c):
            nums[i]=x
        return len(c)