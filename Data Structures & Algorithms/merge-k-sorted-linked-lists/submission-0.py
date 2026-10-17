# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        pq = []
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(pq,(head.val,counter,head))
                counter += 1
        while pq:
            val, cntr, node = heapq.heappop(pq)
            tail.next = node
            if node.next:
                heapq.heappush(pq,(node.next.val, counter, node.next))
                counter += 1
            tail = tail.next

        return dummy.next

        