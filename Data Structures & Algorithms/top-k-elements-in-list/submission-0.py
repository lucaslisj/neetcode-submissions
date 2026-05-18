import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        pq = []
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        for num, count in num_count.items():
            if len(pq) < k:
                heapq.heappush(pq,(count,num))
            else:
                if count > pq[0][0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq,(count,num))
        ans = []
        while(len(pq) > 0):
            cur = heapq.heappop(pq)
            ans.append(cur[1])
        return ans

        