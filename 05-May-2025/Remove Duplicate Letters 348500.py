# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        f=Counter(s)
        a=[]
        visited=set()
        for i in range(len(s)):
            f[s[i]]-=1
            if s[i] in visited:
                continue
            while a and a[-1]> s[i] and f[a[-1]]>0:
                visited.remove(a.pop())
            a.append(s[i])
            visited.add(s[i])
        return "".join(a)