# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort()
        l,r=0,len(s)-1
        t=s[r]+s[l]
        a=[]
        while l<r:
            if s[l]+s[r]!=t:
                return -1
            else:
                a.append(s[l]*s[r])
            l+=1
            r-=1
        return sum(a)
