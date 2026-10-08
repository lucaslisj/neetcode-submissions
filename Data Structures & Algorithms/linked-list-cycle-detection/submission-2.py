# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        pointer1 = head
        pointer2 = head.next
        while pointer2 != None:
            if pointer1 == pointer2:
                return True
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer2 is None:
                return False
            pointer2 = pointer2.next
        return False