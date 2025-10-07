# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ans=1
        ch=a
        while len(ch) < 5*(max(len(b), len(a))):
            if b in ch:
                return ans
            ch+=a
            ans+=1
        return -1