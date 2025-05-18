# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bits='0'
        for _ in range(n-1):
            new='1'
            size=len(bits)
            for i in range(size-1, -1,-1):
                new+=("0"if bits[i]=='1' else '1')
            bits+=new
        return bits[k-1]