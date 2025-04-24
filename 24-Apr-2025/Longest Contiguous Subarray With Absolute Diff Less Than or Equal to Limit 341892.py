# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec=deque()
        inc=deque()
        a=0
        l=0
        for r,x in enumerate(nums):
            while dec and x>dec[-1]:
                dec.pop() 
            dec.append(x)
            while inc and x<inc[-1]:
                inc.pop() 
            inc.append(x)
            while dec[0]-inc[0] > limit:
                if dec[0]==nums[l]:
                    dec.popleft()
                if inc[0]==nums[l]:
                    inc.popleft()
                l+=1
            a=max(a,r-l+1)
        return a
