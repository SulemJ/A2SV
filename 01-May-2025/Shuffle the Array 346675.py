# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        for i,j in zip(range(n),range(n,2*n)):
            a.append(nums[i])
            a.append(nums[j])
        return a