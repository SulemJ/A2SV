# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch=''
        for i in s:
            if i.isalnum():
                ch+=i.lower()
        return ch ==ch[::-1]
