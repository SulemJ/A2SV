# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        for i in s:
            if i =='[' or i =='(' or i =='{':
                a.append(i)
            else:
                if (i == "}" or i == "]" or i == ")") and len(a)==0:
                    return False
                elif i == "}" and a[-1]=='{':
                    a.pop()
                elif i == "]" and a[-1]=='[':
                    a.pop()
                elif i == ")" and a[-1]=='(':
                    a.pop()
                else:
                    return False
        if len(a)==0:
            return True
        else:
            return False