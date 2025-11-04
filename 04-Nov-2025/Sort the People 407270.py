# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c= defaultdict(int)
        for i,x in zip(names, heights):
            c[x]=i 
        n=len(heights)
        for i in range(1,n):
            key = heights[i]
            j=i-1
            while j >=0 and key < heights[j]:
                heights[j+1] = heights[j]
                j-=1
            heights[j+1]=key
        heights.reverse()
        a=[c[i] for i in heights]
        return a