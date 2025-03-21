# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, st: str, k: int) -> int:
        c={}
        j=0
        m=float('-inf')
        s=0
        for i in range(len(st)):
            if st[i] not in c:
                c[st[i]]=0
            c[st[i]]+=1
            s=i-j+1
            if s-max(c.values())<=k:
                m=max(m,s)
            else:
                c[st[j]]-=1
                if  not  c[st[j]]:
                    c.pop(st[j])
                j+=1
            
        return m
