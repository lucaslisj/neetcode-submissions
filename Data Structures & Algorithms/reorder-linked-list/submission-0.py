# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy

        array = []

        while head:
            array.append(head)
            head = head.next

        p1 = 0
        p2 = len(array) - 1
        while (p1 <= p2):
            tail.next = array[p1]
            tail = tail.next
            if p1 != p2:
                tail.next = array[p2]
                tail = tail.next
            p1 += 1
            p2 -= 1
        tail.next = None




        