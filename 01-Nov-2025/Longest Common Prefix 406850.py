# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sample = min(strs,key=len)
        i=0
        while i < len(sample):
            for j in strs:
                if j[i] != sample[i]:
                    return sample[:i] 
            i+=1
        return sample[:i]