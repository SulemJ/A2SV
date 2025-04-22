# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        curr=l1
        while curr:
            a.append(curr.val)
            curr=curr.next
        cur=l2
        while cur:
            b.append(cur.val)
            cur=cur.next
        c=int("".join(map(str,a)))+int("".join(map(str,b)))
        c=str(c)
        dummy=ListNode(0)
        cu=dummy
        for i in c:
            cu.next=ListNode(int(i))
            cu=cu.next
        return dummy.next