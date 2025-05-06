# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], t: int) -> int:
        r=len(nums)-1
        l=0
        while l<=r:
            n=(r+l)//2
            if nums[n]==t:
                return n
            if nums[n]<t:
                l=n+1
            else:
                r=n-1
        return -1
        # for i in n:
