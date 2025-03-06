# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m=max(heights)
        mi=min(heights)
        f=[0]*(m-mi+1)
        p=[]
        # f= {i:heights[i] for i in range(len(heights))}
        for i in heights:
            f[i-mi]+=1
        for i in range(len(f)-1,-1,-1):
            for _ in range(f[i]):
                # p.append(i+mi)
                p.append(names[heights.index(i+mi)])
        # print(p)
        return p
        
        