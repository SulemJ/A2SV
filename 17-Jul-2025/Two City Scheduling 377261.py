# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=0
        intfroma=[[i,x[0]-x[1]  ] for i,x in enumerate(costs)]
        intfroma=sorted(intfroma,key=lambda x:x[1])
        # a=[]
        for i,x in enumerate(intfroma):
            if i<len(costs)//2:
                ans+=costs[x[0]][0]
            else:
                ans+=costs[x[0]][1]
        return ans