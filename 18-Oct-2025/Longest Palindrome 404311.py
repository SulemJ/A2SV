# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d= Counter(s)
        odd=0
        ans=0
        for i,x in d.items():
            if x%2==0:
                ans+=x
            else:
                ans+=((x//2)*2)
                odd+=1
        return ans + 1 if odd !=0 else ans