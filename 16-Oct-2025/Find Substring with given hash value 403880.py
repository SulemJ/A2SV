# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n=len(s)
        res_idx=0
        hash_val=0
        powerK=pow(power,k,modulo)

        for i in range(n-1,-1,-1):
            val = ord(s[i])-ord('a')+1
            hash_val= (hash_val * power + val) % modulo

            if i+k <n:
                remov =( ord(s[i+k])-ord('a')+1) * powerK %modulo
                hash_val = (hash_val - remov +modulo) %modulo
            
            if hash_val == hashValue:
                res_idx = i
        return s[res_idx:res_idx+k]
