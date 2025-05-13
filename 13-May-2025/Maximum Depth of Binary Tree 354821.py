# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ans=float('-inf')
        # def maxx(node, dpth):
        # dpth=0
        if not root:
            return 0
            # a=
            # b=maxx(node.right, dpth+1)
        return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        # return maxx(root,0)