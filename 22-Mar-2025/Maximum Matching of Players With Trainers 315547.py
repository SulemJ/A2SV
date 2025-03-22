# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        l,r=0,0
        c=0
        while l<len(p) and r<len(t):
            if p[l]<=t[r]:
                c+=1
                l+=1
            r+=1

        return c

