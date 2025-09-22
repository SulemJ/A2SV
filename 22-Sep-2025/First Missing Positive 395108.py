# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        ans=1
        for i in nums:
            if i >0 and i ==ans:
                ans+=1
            elif i<=0:
                pass
            else:
                return ans
        return ans