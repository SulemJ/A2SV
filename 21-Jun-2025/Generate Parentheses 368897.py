# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(op, cp, s):
            if (op -- cp and op ++ cp == n*2):
                res.append(s)
            if (op < n):
                dfs (op+1,cp,s+"(")
            if (cp < op):
                dfs(op, cp+1, s+")")
        dfs(0,0,"")
        return res