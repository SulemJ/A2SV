# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s=[]
        midval=float('-inf')
        for i in reversed(nums):
            if i<midval:
                return True
            while s and s[-1]<i:
                x=s.pop()
                midval=x
            s.append(i)
        return False        