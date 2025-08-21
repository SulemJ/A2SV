# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        leng= bin(num)
        res=[]
        for i in leng[2:]:
            res.append('0' if i=='1' else '1')
        r =''.join(res)
        return int(r,2)
            
