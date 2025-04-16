# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l,r=0,0
        d=ListNode(0,head)
        cur=head
        while cur:   
            r+=1
            if r-l==n:
                l+=1
            cur=cur.next
        i=0
        prev=d
        cur=head
        while cur:
            i+=1
            if i==l:
                prev.next=cur.next
                break
            prev=cur
            cur=cur.next
        return d.next