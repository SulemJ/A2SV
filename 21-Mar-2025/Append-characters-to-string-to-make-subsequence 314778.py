# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        loop through to the 1 
        """
        l,r=0,0

        for i in range(len(s)):
            if s[i]==t[r]:
                r+=1
            if r>=len(t):
                break
        return len(t)-r