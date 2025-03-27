# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a=[0]*(len(s)+1)
        c=[]
        b=0
        for i in shifts:
            a[i[0]]+=i[2] if i[2]==1 else -1
            a[i[1]+1]-=i[2] if i[2]==1 else -1
        for i in a:
            c.append(b+i)
            b+=i
        # print(c)
        for i in range(len(s)):
            n= (c[i] % 26 + 26) % 26
            c[i]=chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            # print(c[i])
        return "".join(c[:-1])