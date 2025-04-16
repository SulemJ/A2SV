# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        t=r=head
        # c=0
        while r and r.next:
            # c+=1
            t=t.next
            r=r.next.next
        prev,cur=None,t
        while cur:
            nextNode = cur.next
            cur.next=prev
            prev = cur
            cur =nextNode

        r=head
        t=prev
        while t:
            if r.val !=t.val:
                return False
            t=t.next
            r=r.next
        return True
        # t=c//2+1
        # while t:

