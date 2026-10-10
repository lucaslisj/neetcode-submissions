# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        # 1. get length of list
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        # 2. figure out which node index to delete and construct the linked list
        delete_index = length - n
        node = dummy
        for i in range(delete_index):
            node = node.next
        node.next = node.next.next
        
        return dummy.next



        