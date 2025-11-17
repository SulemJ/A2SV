# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        ans=0
        for j in range(len(s)):
            while s[j] in s[i:j]:
                i+=1
            ans=max(ans, j-i+1)
        return ans