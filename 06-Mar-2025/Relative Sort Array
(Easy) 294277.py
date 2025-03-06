# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a=Counter(arr1)
        b=Counter(arr2)
        g=[]
        d=[]
        for i in b:
            for _ in range(a[i]):
                g.append(i)
        for i,x in a.items():
            if i not in arr2:
                for _ in range(x):
                    d.append(i)
        d.sort()
        return g+d