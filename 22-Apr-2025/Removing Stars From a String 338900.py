# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in range(len(s)):
            if s[i]=='*':
                a.pop()
            else:
                a.append(s[i])
        return "".join(a)    