# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i,j=0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] > mid:
                j = mid-1
            else:
                i= mid+1
        return i 