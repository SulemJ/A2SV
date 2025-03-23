# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, f: List[int]) -> int:
        l,r,c=0,0,0
        d={}
        for i in range(len(f)):
            if f[i] not in d:
                d[f[i]]=0
            d[f[i]]+=1
            while len(d) ==3:
                if d[f[l]] ==1:
                    del d[f[l]]
                else:
                    d[f[l]]-=1
                l+=1
            c=max(c,i-l+1)
        return c