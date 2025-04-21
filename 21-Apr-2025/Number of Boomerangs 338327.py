# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, p: List[List[int]]) -> int:
        boomerangs = 0
        for p1 in p:
            distances = defaultdict(int)
            for p2 in p:
                if p1 == p2:
                    continue
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                distances[dist] += 1
            for dist in distances.values():
                boomerangs += dist * (dist - 1)
        return boomerangs

        # for i in range(len(p)):
        #     f={}
        #     for j in range(len(p)-1):
        #         if (abs(p[i+1][0] - p[i][0]) + abs(p[i+1][1] - p[i][1])) not in f:
        #             f[abs(p[i+1][0] - p[i][0]) + abs(p[i+1][1] - p[i][1])]=0
        #         f[abs(p[i+1][0] - p[i][0]) + abs(p[i+1][1] - p[i][1])]+=1
        #     for i,x in f.items():

                    
                    
                     















        # p.sort()
        # c=0
        # for i in range(1,len(p)-1):
        #     if abs(p[i-1][0] - p[i][0]) ==abs(p[i+1][0] - p[i][0]) and abs(p[i-1][1] - p[i][1]) ==abs(p[i+1][1] - p[i][1]):
        #         c+=2
        # return c
