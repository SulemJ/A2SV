# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

ssum=[]
        for _ in range(k):
            f=max(nums)
            ssum.append(f)
            nums[nums.index(f)]+=1
        return sum(ssum)