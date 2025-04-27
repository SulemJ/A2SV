# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        f=[0]
        for r in s:
            if r=="(":
                f.append(0)
            elif f:
                last=f.pop()
                if last == 0:
                    f[-1] += 1 
                else:
                    f[-1] += 2 * last
        return f[0]
   