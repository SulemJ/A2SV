# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=head
        # prev=dummy
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                # prev=curr
                curr=curr.next
        return dummy.next









        