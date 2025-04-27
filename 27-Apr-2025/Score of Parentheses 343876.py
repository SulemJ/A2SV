# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        f=[0]
        for r in s:
            if r=="(":
                f.append(0)
            elif f:
                last=f.pop()
                f[-1] += max(1,last*2)
        return f[-1]
   