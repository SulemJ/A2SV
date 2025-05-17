# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        is_even=True
        d=deque([root])
        while d:
            prev=float('-inf') if is_even else float('inf')
            for _ in range(len(d)):
                node=d.popleft()
                if is_even and (node.val%2==0 or node.val<=prev):
                    return False
                elif not is_even and (node.val%2==1 or node.val>=prev):
                    return False
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                prev=node.val
            is_even= not is_even
        return True












