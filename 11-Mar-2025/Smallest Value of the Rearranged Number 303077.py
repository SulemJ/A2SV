# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

# from itertools import permutations
# class Solution:
#     def smallestNumber(self, num: int) -> int:
#         l=len(str(num))
from itertools import permutations
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num== 0:
            return num
        if num > 0:
            b= list(map(int, list(str(num))))
            b.sort()
            zeros= b.count(0)
            if b[0]==0:
                b[0] , b[zeros] = b[zeros] , b[0]
            num = int("".join((map(str,list(b)))))    
            
        else :
            num=num* -1
            b= list(map(int, list(str(num))))
            b.sort(reverse=True)
            num = int("".join((map(str,list(b)))))
            num = num * -1
        return num
        # if num>=0:
        #     b= list(map(int, list(str(num))))
        #     b.sort()
        #     z=b.count(0)
        #     a=[]
        #     for i in b:
        #         a.appe
        # l=len(str(num))
        # n=False
        # if num<0:
        #     n=True
        #     num=num*(-1)
        # b= list(map(int, list(str(num))))
        # v=list(permutations(b))
        # if n==False:
        #     a=[]
        #     for i in v:
        #         a.append(int("".join((map(str,list(i))))))
        #     a.sort()
        #     for i in a:
        #         if len(str(i)) == l:
        #             return i
        #             # break
        # else:
        #     return -1*int("".join((map(str,list(sorted(v)[-1])))))
