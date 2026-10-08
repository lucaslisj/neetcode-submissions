# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        visited = set()
        visited.add(cur)
        if cur == None:
            return False
        while cur.next is not None:
            if cur.next in visited:
                return True
            visited.add(cur.next)
            cur = cur.next
        return False

        