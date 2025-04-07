# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # a=[0]*(len(s)+1)
        # c=[]
        # b=0
        # for i in shifts:
        #     a[i[0]]+=i[2] if i[2]==1 else -1
        #     a[i[1]+1]-=i[2] if i[2]==1 else -1
        # for i in a:
        #     c.append(b+i)
        #     b+=i
        # # print(c)
        # for i in range(len(s)):
        #     n= (c[i] % 26 + 26) % 26
        #     c[i]=chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        #     # print(c[i])
        # return "".join(c[:-1])







        a=[0]*len(s)
        for i in shifts:
            if i[2]==0:
                a[i[0]]-=1
                if i[1]+1<len(a):
                    a[i[1]+1]+=1
            else:
                a[i[0]]+=1
                if i[1]+1<len(a):
                    a[i[1]+1]-=1
        
        k=0
        c=[0]*len(s)
        for i in range(len(a)): 
            k+=a[i]
            c[i]=k
        # d=[]
        for i in range(len(a)):
            n= (c[i] % 26 + 26) % 26
            c[i]=chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            # if c[i]+ord(s[i])<97:
            #     d.append(chr(c[i]+ord(s[i])+26))
            # elif c[i]+ord(s[i])>122:
            #     d.append(chr(c[i]+ord(s[i])-26))
            # else:
            #     d.append(chr(c[i]+ord(s[i])))

        return "".join(c)












