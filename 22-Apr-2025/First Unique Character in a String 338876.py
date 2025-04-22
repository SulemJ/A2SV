# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        for i,x in a.items():
            if x==1:
                return s.index(i)
        return -1