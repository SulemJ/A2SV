# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        ans = []
        while l < len(word1) and r < len(word2):
         
            if word1[l:] > word2[r:]:
                ans.append(word1[l])
                l += 1
            else:
                ans.append(word2[r])
                r += 1

        ans.extend(word1[l:])
        ans.extend(word2[r:])
        return "".join(ans)
