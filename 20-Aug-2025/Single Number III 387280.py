# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c= Counter(nums) 
        res=[]
        for i,x in c.items():
            if x == 1:
                res.append(i)
        return res