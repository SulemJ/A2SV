# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # sCount= Counter(s)
        # tCount= Counter(t)
        # arr1= [x for i, x in sCount.items()]
        # arr2= [x for i, x in tCount.items()]
        pair1 ={}
        pair2 ={}
        for i, x in zip(s,t):
            if i not in pair1:
                pair1[i]=x
            else:
                if pair1[i] != x:
                    return False
            if x not in pair2:
                pair2[x]=i
            else:
                if pair2[x] != i:
                    return False
        return True
        # if arr2 == arr1:
        #     return True
        # else:
        #     return False