# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        ans=[]
        n=len(nums)
        for i,x in c.items():
            if x > n/3:
                ans.append(i)

        return ans