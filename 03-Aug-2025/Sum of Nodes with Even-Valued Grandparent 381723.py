# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        stack = [(root, None)]
        res = 0
        while stack:
            node, even_parent = stack.pop()
            if node.left:
                stack.append((node.left, node.val%2==0))
                if even_parent:
                    res+=node.left.val
            if node.right:
                stack.append((node.right, node.val%2==0))
                if even_parent:
                    res+=node.right.val
        return res