# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        k=[]
        for i in range(len(s)):
            k.append(abs(ord(s[i])-ord(t[i])))
        j=0
        le=0
        su=0
        for i in range(len(k)):
            su+=k[i]
            while su>maxCost:
                su-=k[j]
                j+=1
            le=max(le,i-j+1)      

        return le