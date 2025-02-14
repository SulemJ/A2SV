# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums=set()
        for i, x in ranges:
            for y in range(i, x+1):
                nums.add(y)
        for i in range(left, right+1):
            if i not in nums:
                return False
        return True