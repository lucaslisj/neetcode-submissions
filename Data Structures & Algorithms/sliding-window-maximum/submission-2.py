import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = [] # we store negatives to ensure we can get positive numbers
        p1 = 0
        trash_can = {} # numbers we remove, number of times we remove
        ans = []
        for p2 in range(len(nums)):
            # add in the current number (negative version)
            num = -nums[p2]
            heapq.heappush(pq,num)

            # move left pointer up if window is too long
            while p2 - p1 + 1 > k:
                removing = -nums[p1]
                if removing == pq[0]:
                    heapq.heappop(pq)
                    new_max = pq[0]
                    while(trash_can.get(new_max,0) > 0):
                        trash_can[new_max] -= 1
                        heapq.heappop(pq)
                        new_max = pq[0]

                else:
                    trash_can[removing] = trash_can.get(removing,0) + 1
                p1 += 1

            # if window is perfect size then do a check
            if p2 - p1 + 1 == k:
                max_val = -pq[0]
                ans.append(max_val)
        return ans
        