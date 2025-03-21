# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        """
        """
        l=0
        a=[]
        for i in range(len(f)):
            j=0
            while j<len(s):
                if f[i][0] in range(s[j][0],s[j][1]+1) or f[i][1] in range(s[j][0],s[j][1]+1) or s[j][0] in range(f[i][0],f[i][1]+1) or s[j][1] in range(f[i][0],f[i][1]+1):
                    a.append([max(s[j][0],f[i][0]),min(s[j][1],f[i][1])])
        
                j+=1
        return a