# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        output = 0
        mask = 0
        for i in range(31, -1, -1):  # from MSB to LSB
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            candidate = output | (1 << i)
            if any((candidate ^ p) in prefixes for p in prefixes):
                output = candidate
        return output