# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c= defaultdict(int)
        for i,x in zip(names, heights):
            c[x]=i 
        n=len(heights)
        for i in range(n):
            min_idx= i
            for j in range(i+1, n):
                if heights[j] < heights[min_idx]:
                    min_idx = j
            heights[min_idx], heights[i] = heights[i], heights[min_idx]
        ans=[c[i] for i in heights]
        ans.reverse()
        return ans