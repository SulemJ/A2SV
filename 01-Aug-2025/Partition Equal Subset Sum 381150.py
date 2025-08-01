# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        # dp.add(nums[-1])
        tar=sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            temp=set()
            for t in dp:
                if (t+nums[i]) == tar:
                    return True
                else:
                    temp.add(t+nums[i])
                    temp.add(t)
            dp=temp
        return True if tar in dp else False    
