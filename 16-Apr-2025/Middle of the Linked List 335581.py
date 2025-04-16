# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0,head)
        cur=head
        l,r=0,0
        while cur:
            cur=cur.next
            l+=1
            r+=2

        # if l %2==0:
        t=l//2+1
        # if l %2!=0:
        #     t=l//2+1     
        i=0
        cur=head
        while i<t-1:
            cur=cur.next
            i+=1
        return cur