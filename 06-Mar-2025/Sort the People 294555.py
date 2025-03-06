# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)
        for i in range(1,n):
            p=heights[i]
            f=names[i]
            j=i-1
            while j>=0 and p>heights[j]:
                names[j+1]=names[j]
                heights[j+1]=heights[j]
                j-=1
                
            names[j+1] = f
            heights[j+1] = p
        return names
        
        