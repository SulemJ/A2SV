# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=Counter(nums1)
        m=Counter(nums2)
        a=max(len(nums1), len(nums2))
        ans=[]
        # m=min()
        for i,x in n.items():
            if i in m:
                for j in range(min(x,m[i])):
                    ans.append(i)
        return ans