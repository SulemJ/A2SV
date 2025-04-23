# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=deque()
        for i in tokens:
            if i=="+":
                r=int(a[-2])+int(a[-1])
                a.pop()
                a.pop()
                a.append(r)
            elif i=="*":
                r=int(a[-2])*int(a[-1])
                a.pop()
                a.pop()
                a.append(r)
            elif i=="-":
                r=int(a[-2])-int(a[-1])
                a.pop()
                a.pop()
                a.append(r)
            elif i=="/":
                if (int(a[-1])>=0 and int(a[-2])>=0) or (int(a[-1])<0 and int(a[-2])<0):
                    r=int(a[-2])//int(a[-1])
                    a.pop()
                    a.pop()
                    a.append(r)
                else:
                    # if int(a[-1])<0: 
                    r=abs(int(a[-2]))//abs(int(a[-1]))
                    a.pop()
                    a.pop()
                    a.append(-1*r)
            else:
                a.append(i)
        return int(a[-1])