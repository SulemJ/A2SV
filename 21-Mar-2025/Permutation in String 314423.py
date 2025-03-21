# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        c1=Counter(s1)
        cw=Counter()
        for i in range(m):
            cw[s2[i]]+=1
            if i >=n:
                if cw[s2[i-n]]==1:
                    del cw[s2[i-n]]
                else:
                    cw[s2[i-n]]-=1
            if cw==c1:
                return True
        return False
