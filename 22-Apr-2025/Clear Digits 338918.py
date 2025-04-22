# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution:
    def clearDigits(self, s: str) -> str:
        a=[]
        # for i in range(len(s)-1,-1,-1):
        #     if type(s[i]) is str :
        #         if len(a)!=0 and type(a[-1]) is not str:
        #             a.pop()
        #     # else:
        #     a.append(s[i])
        # return "".join(reversed(a))  

        for i in range(len(s)-1,-1,-1):
            if not s[i].isdigit() :
                if len(a)!=0 and a[-1].isdigit():
                    a.pop()
                else:
                    a.append(s[i])
            else:
                a.append(s[i])
        return "".join(reversed(a))