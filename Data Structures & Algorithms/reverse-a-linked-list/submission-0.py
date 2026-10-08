# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        if cur == None:
            return cur
        while cur.next != None:
            true_next = cur.next
            cur.next = prev
            prev = cur
            cur = true_next
        cur.next = prev
        return cur
