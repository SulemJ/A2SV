# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        parent=self.kthGrammar(n-1, (k+1)//2)
        is_K_even=(k%2==0)

        if parent==1:
            return 0 if is_K_even else 1
        if parent == 0:
            return 1 if is_K_even else 0