# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        c=Counter(p)
        res=[]
        for i in range(len(s)-len(p)+1):
            temp=Counter(s[i:i+len(p)])

            if temp==c:
                res.append(i)
        return res