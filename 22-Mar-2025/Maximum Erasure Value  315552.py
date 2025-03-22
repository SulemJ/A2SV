# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, n: List[int]) -> int:
        l,c=0,0
        w={}
        s=0
        for i in range(0,len(n)):
            s+=n[i]
            while n[i] in w:
                s-=n[l]
                if w[n[l]] ==1:
                    del w[n[l]] 
                else:
                    w[n[l]]-=1
                l+=1
            w[n[i]] =1
            c=max(c,s)
        return c