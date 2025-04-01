# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[1]*(n+2)
        r=[1]*(n+2)
        lp=1
        rp=1
        a=[1]*(n+2)
        for i,j in zip(range(n-1,-1,-1),range(n)):
            lp=nums[j]*lp
            r[j+1]=lp
            # print(i)
            rp=nums[i]*rp
            l[i+1]=rp
        for i in range(1,n+1):
            # print(i)
            a[i]=l[i+1]*r[i-1]
        # print(a[1:-1])
        


        return a[1:-1]