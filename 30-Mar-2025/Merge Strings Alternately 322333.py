# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=[]
        n=len(word1) if len(word1) <len(word2) else len(word2)
        f=len(word2) if len(word1) <len(word2) else len(word1)
        for i in range(n):
            a.append(word1[i])
            a.append(word2[i])
        for i in range(n,f):
            a.append(word1[i]) if f==len(word1) else a.append(word2[i])
        return "".join(a)