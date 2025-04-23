# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        s=[]
        # print(a)
        for i in range(len(a)):
            if a[i] == '' or a[i]=='.':
                continue
            elif a[i]=='..':
                if len(s)!=0:
                    s.pop()
                else:
                    continue
                # s.pop()
            else:
                s.append(a[i])
        d="/".join(s)
        return "/"+d