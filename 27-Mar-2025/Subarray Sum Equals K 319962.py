# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, n: List[int], k: int) -> int:
        c=0
        s=0
        d={0:1}
        for i in n:
            s+=i
            if s-k in d:
                c+=d[s-k]
            if s not in d:
                d[s] = 1
            else:
                d[s]+=1
        return c
            
