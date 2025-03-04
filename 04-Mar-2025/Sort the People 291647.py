# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(heights)
        for i in range(n):
            min=i
            for j in range(i+1, n):
                if heights[min]<=heights[j]:
                    min =j
            names[min], names[i] = names[i], names[min]
            heights[min], heights[i] = heights[i], heights[min]
        return names
        
        