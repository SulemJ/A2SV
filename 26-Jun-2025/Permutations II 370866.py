# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(list(permutations(nums))))