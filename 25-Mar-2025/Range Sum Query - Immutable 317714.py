# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.a=nums

    def sumRange(self, l: int, r: int) -> int:
        # s=0
        # for i in range(l,r+1):
        #     s+=self.a[i]
        return sum(self.a[l:r+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)