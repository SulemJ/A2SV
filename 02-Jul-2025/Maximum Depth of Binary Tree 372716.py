# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxx(node):
            if not node:
                return 0
            right = 1 + maxx(node.right)
            left = 1 + maxx(node.left)
            return max(right, left)
        return maxx(root)
        # maxDepth = 1 + max(max_depth(root.left), max_depth(root.right))