# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i] and stack[-1][1] + 1 == k:
                for _ in range(k-1):
                    stack.pop()
            elif stack and stack[-1][0] == s[i] and stack[-1][1] != k:
                stack.append((s[i], stack[-1][1] + 1))
            else:
                stack.append((s[i], 1))
        return "".join(s[0] for s in stack)