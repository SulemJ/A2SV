# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        a=[]
        s=[]
        num=(4-len(str(num)))*"0"+str(num)
        for i in range(4):
            if num[i]:
                a.append(int(num[i]))
            else:
                a.append(0)
        if a[0] != 0:
            s.append((a[0]*"M"))
        if a[1]!=0:
            if a[1] == 4:
                s.append("CD")
            elif a[1] == 9:
                s.append("CM")
            elif a[1]>=5:
                s.append(("D"+(a[1]-5)*"C"))
            else:
                s.append((a[1]*"C"))
        if a[2] != 0:
            if a[2] == 4:
                s.append("XL")
            elif a[2] == 9:
                s.append("XC")
            elif a[2]>=5:
                s.append(("L"+(a[2]-5)*"X"))
            else:
                s.append((a[2]*"X"))
        if a[3] != 0:
            if a[3] == 4:
                s.append("IV")
            elif a[3] == 9:
                s.append("IX")
            elif a[3]>=5:
                s.append(("V"+(a[3]-5)*"I"))
            else:
                s.append((a[3]*"I"))
        return "".join(s)

        """
        -mebeten num in decimal places
        -for 4 digits if take n[0]*"M" - append
        -for 3 digits   if starts with 4 append "CD"
                        elif starts with 9 append"CM"
                        elif >=500 append "D" then append (n[0]-5)*"C"
                        else n[0]*"C"
        -for 2 digits if starts with 4 append "XL"
                        elif starts with 9 append"XC"
                        elif >=50 append "L" then append (n[0]-5)*"X"
                        else n[0]*"X"
        -for 2 digits if starts with 4 append "IV"
                        elif starts with 9 append"IX"
                        elif >=5 append "V" then append (n[0]-5)*"I"
                        else n[0]*"I"
                    

        """