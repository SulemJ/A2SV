# Problem: Maximum Binary Tree - https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # position= {nums[i]:i for i in range(len(nums))}
        # a=nums
        if not nums:
            return 
        element =max(nums)
        index=nums.index(element)
         
        node=TreeNode(element)
        node.left=self.constructMaximumBinaryTree(nums[0:index])
        node.right=self.constructMaximumBinaryTree(nums[index+1:])

        return node






