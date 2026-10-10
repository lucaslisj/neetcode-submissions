# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy

        n = 0
        tail = head
        while tail:
            n += 1
            tail = tail.next

        tail = head
        for i in range(n // 2):
            tail = tail.next
        prev = None
        while tail:
            true_next = tail.next
            tail.next = prev
            prev = tail
            if not true_next:
                break
            tail = true_next
        while head is not None and tail is not None:
            next_head = head.next
            head.next = tail
            head = next_head
            if head is tail:
                break
            next_tail = tail.next
            tail.next = head
            tail = next_tail

        
        