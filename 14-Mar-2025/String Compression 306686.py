# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, c: List[str]) -> int:
        n = len(c)
        if n == 0: return 0
        w = 0
        r = 0
        while r < n:
            x = c[r]
            f = 0
            while r < n and c[r] == x:
                r += 1
                f += 1
            c[w] = x
            w += 1
            if f > 1:
                for d in str(f):
                    c[w] = d
                    w += 1
        return w