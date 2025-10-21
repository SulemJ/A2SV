# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        c=Counter(nums)
        for i,x in c.items():
            if x==2:
                ans.append(i)
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans