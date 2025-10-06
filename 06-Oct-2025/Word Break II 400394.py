# Problem: Word Break II - https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        cur=[]
        res=[]
        backtrack(0)
        return res