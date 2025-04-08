# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # c=[0,0,0,0,0]
        return sum(set(word[i:j+1]) == set('aeiou') for i in range(len(word)) for j in range(i+1, len(word)))