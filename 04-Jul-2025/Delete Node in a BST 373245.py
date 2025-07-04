# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        # def helper(node):
        #     cur=node
        #     while node.left:
        #         cur=node.left
        #     return cur
        if key < root.val:
            root.left= self.deleteNode(root.left, key)
        elif key > root.val:
            root.right= self.deleteNode(root.right, key)
        else:
            if not root.right:
                return  root.left
            if not root.left:
                return root.right

            temp= root.right 
            while temp.left:
                temp=temp.left
            root.val=temp.val

            root.right=self.deleteNode(root.right, temp.val)
            
        return root
