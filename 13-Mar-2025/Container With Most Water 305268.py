# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        w=0
        c=0
        while l<r:
            # w=
            h=(min(height[r],height[l]))*(r-l)
            c=max(h,c)
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return c
        # for i in range(n):
        #     for j in range(i+1,n):
        #         l=(min(height[j],height[i]))*(j-i)
        #         # print(l, height[i],i,height[j],j)
        #         m=max(m,l)
        # return m