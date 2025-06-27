# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        self.min_unfairness = float('inf')

        def backtrack(index):
            if index == len(cookies):
                self.min_unfairness = min(self.min_unfairness, max(distribution))
                return

            for i in range(k):
                distribution[i] += cookies[index]
                
                if max(distribution) < self.min_unfairness:
                    backtrack(index + 1)
                
                distribution[i] -= cookies[index]

            
                if distribution[i] == 0:
                    break

        backtrack(0)
        return self.min_unfairness
