# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        a=s[0]
        c=1
        # if len(s)==2 and s[0]!=s[1]:
        #     return s[0]
        # if len(s)==2 and s[0]==s[1]:
        #     return s
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1>c and s[i:j+1] ==s[i:j+1][::-1]:
                    c=j-i+1
                    a=s[i:j+1]
        return a
                # l,r=0,len(d)-1
                # c=0
                # while l<r:
                #     if d[l]!=d[r]:
                #         c=-1
                #     l+=1
                #     r-=1
                # if c!=-1 and len(d)>len(a):
                #     a=d if len(a)>0 else s[0]

                # if len(d)==2:
                #     if d[l]!=d[r]:
                #         break
                #     else:
                #         if len(d)>len(a):
                #             a=d
                # else: