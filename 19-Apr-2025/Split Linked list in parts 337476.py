# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length,cur=0,head
        while cur:
            cur=cur.next
            length+=1
        remainder,parts=length%k,length//k
        curr=head
        a=[]
        for i in range(k):
            a.append(curr)
            for j in range(parts - 1 + (1 if remainder else 0)):
                if not curr: break
                curr = curr.next
            remainder -= (1 if remainder else 0)
            if curr:
                curr.next,curr =None,curr.next

        return a      
