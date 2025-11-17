# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        c= Counter(p) #{a:1, b:1, c:1}
        ch=Counter(s[:len(p)]) #{c:1,b:1,a:1}
        i=0
        ans=[]
        for j in range(len(p),len(s)):
            if ch==c:
                ans.append(i)
            ch[s[i]]-=1
            if ch[s[i]]==0:
                del ch[s[i]]
            ch[s[j]]+=1
            i+=1
        if ch==c:
                ans.append(i)       # j+=1
        return ans
