# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a=[]
        for i in range(len(arr)-1,-1,-1):
            c=arr[len(arr)-1]
            if i ==len(arr)-1:
                a.append(-1)
            # if len(arr[i+1:]) >0:
            else:
                a.append(max(arr[i+1],c,a[-1]))
                # a.append(-1)
        # b=reversed(a)
        return list(reversed(a))