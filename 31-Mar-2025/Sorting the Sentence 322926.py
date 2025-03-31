# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        a=[i[-1] for i in s]
        
        r=[0]*len(s)
        for i in range(len(s)):
            r[int(a[i])-1]=s[i][:-1]
        return " ".join(r)