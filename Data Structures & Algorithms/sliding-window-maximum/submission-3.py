import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = [] # -value, index
        p1 = 0
        ans = []
        for p2 in range(len(nums)):
            # add in new element
            heapq.heappush(pq,(-nums[p2],p2))

            # eject outdated terms based on index
            while(pq[0][1] < p2 - k + 1):
                heapq.heappop(pq)
            
            # get the max of the current window ending with p2 if its long enough
            if p2 >= k - 1:
                ans.append(-pq[0][0])

        return ans

        