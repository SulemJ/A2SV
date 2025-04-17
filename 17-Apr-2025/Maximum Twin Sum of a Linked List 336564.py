# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            new=curr.next
            curr.next=prev
            prev=curr
            curr=new
        a=[]
        chk=head
        while prev:
            a.append(chk.val+prev.val)
            chk=chk.next
            prev=prev.next
        return max(a)
