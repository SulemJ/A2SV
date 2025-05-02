# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss=[]
        st=[]
        for i in s:
            if i =="#":
                if ss:
                    ss.pop()
                else:
                    continue
            else:
                ss.append(i)
        for i in t:
            if i =="#":
                if st:
                    st.pop()
                else:
                    continue
            else:
                st.append(i)
        return ss==st