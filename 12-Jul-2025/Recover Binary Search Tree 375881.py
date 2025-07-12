# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        value_list = []
        def traverse(root):
            if root is None:
                return
            
            traverse(root.left)
            value_list.append(root.val)
            traverse(root.right)
        traverse(root)
        
        value_list = sorted(value_list)


        index = [0]
        def fix(root):
            if root is None:
                return
            fix(root.left)
            root.val = value_list[index[0]]
            index[0] += 1
            fix(root.right)
        
        return fix(root)
