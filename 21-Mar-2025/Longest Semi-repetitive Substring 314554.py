# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        m=0
        c=0
        i=0
        if len(s) ==1:
            return 1
        for j in range(1,len(s)):
            if s[j]==s[j-1]:
                c+=1
            while c==2:
                if s[i+1] == s[i]:
                    c-=1
                i+=1
            m=max(m,j-i+1) 
        return m