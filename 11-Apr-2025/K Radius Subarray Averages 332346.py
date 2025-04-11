# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        a=[-1]*len(nums)
        l,c=0,0
        for i in range(len(nums)):
            c+=nums[i]
            if i-l+1==2*k+1:
                a[l+k]=(c//(2*k+1))
                c-=nums[l]
                l+=1
        
        return a