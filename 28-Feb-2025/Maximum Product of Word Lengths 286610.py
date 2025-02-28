# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits=[]
        for word in words:
            bit=0
            for char in word:
                bit |= 1 << (ord(char) - ord('a'))
            bits.append(bit)
        # print(bits)
        maxp=0
        for i in range(len(bits)):
            for j in range(len(bits)):
                if bits[i] & bits[j] ==0:
                    maxp=max(maxp,len(str(words[i]))*len(str(words[j])))
        return maxp
