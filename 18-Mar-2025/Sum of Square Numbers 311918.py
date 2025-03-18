# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # a=[i for i in range(c+1)]
        i,j=0,int(math.sqrt(c))
        while i<=j:
            if i*i==c:
                return True
            elif j*j==c:
                return True
            elif i*i + j*j>c:
                j-=1
            elif i*i + j*j<c:
                i+=1
            else:
                return True
        return False