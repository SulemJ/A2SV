# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        a=[0]*len(t)
        s=[]
        for i,x in enumerate(t):
            while s and x>t[s[-1]]:
                f=s.pop()
                a[f]=i-f
            s.append(i)
        return a        
