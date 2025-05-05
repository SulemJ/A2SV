# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        c=[]
        for i in range(2*n-1,-1,-1):
            num=nums[i%n]
            while c and c[-1]<=num:
                c.pop()
            if c:
                res[i%n]=c[-1]
            c.append(num)  
        return res
        