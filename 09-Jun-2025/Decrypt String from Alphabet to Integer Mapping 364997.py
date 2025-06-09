# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                num = int(s[i:i+2])
                res += chr(ord('a') + num - 1)
                i += 3
            else:
                num = int(s[i])
                res += chr(ord('a') + num - 1)
                i += 1

        return res