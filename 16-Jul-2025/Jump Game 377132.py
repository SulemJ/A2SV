# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tar = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= tar:
                tar = i
        return tar == 0