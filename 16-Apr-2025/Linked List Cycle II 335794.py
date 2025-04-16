# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=r=head
        while r and r.next:
            t= t.next
            r= r.next.next
            if t == r:
                t=head
                while t != r:
                    t=t.next
                    r=r.next
                    # if t == r:
                return r

        return None
