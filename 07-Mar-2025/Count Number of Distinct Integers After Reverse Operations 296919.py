# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n):
            nums.append(int((str(nums[i]))[::-1]))
        return len(set(nums))