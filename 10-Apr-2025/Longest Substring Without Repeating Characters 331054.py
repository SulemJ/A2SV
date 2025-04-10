# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # bacabcbb
        d={}
        l,c=0,0
        for i in range(len(s)):
            if s[i] not in d: 
                d[s[i]]=0
            d[s[i]]+=1
            while d[s[i]]==2:
                if d[s[l]]==1:
                    del d[s[l]]
                else:
                    d[s[l]]-=1
                l+=1
            c=max(c,i-l+1)
        return c









        # d={}
        # l,c=0,0
        # for i in range(len(s)):
        #     if s[i] not in d:
        #         d[s[i]]=0
        #     d[s[i]]+=1
        #     while d[s[i]] ==2:
        #         if d[s[l]]==1:
        #             del d[s[l]]
        #         else:
        #             d[s[l]]-=1
        #         l+=1
        #     c=max(c,i-l+1)
        # return c
