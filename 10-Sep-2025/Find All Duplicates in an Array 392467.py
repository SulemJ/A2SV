# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count= Counter(nums)
        arr=[]
        for i,x in count.items():
            if x==2:
                arr.append(i)
        return arr