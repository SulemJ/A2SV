# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        buk = [0] * k
        self.res = float('inf')

        def backtrack(i, buk):
            if i >= len(cookies):
                self.res = min(self.res, max(buk))
                return
            if max(buk) > self.res:
                return
            for j in range(k):
                buk[j] += cookies[i]
                backtrack(i+1, buk)
                buk[j] -= cookies[i]

        backtrack(0, buk)
        return self.res