# Problem:  Boats to Save People - https://leetcode.com/problems/boats-to-save-people/description/

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort()
        i,j=0,len(p)-1
        c=0
        while i<=j:
            if p[j]==l:
                c+=1
                j-=1
            elif p[j]+p[i]<=l:
                c+=1
                i+=1
                j-=1
            elif p[j]+p[i]>l:
                c+=1
                j-=1
        return c