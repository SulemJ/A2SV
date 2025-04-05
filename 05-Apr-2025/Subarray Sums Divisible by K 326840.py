# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #[4, 5, 0, -2, -3, 1]
        #   1 1 1 4 6  10=2+1
        [7,4,-10]
        2 

        c=0
        s=0
        d={0:1}
        for i in nums:
            s+=i
            v=s%k
            if v%k in d:
                c+=d[v%k]
            if v not in d:
                d[v] = 1
            else:
                d[v]+=1
        return c 
