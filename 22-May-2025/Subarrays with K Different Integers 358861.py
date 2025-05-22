# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def uptok(k):
            l,ans=0,0
            f=defaultdict(int)
            for r in range(len(nums)):
                if f[nums[r]] ==0:
                    k-=1
                f[nums[r]]+=1
                
                while k<0:
                    f[nums[l]]-=1
                    if f[nums[l]] ==0:
                        k+=1
                    l+=1
                ans+=r-l+1
            return ans

        return uptok(k)-uptok(k-1)