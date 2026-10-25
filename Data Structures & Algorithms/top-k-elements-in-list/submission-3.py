class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        
        for key, val in counts.items():
            heapq.heappush(pq, (-val, key))
        
        ans = []
        for i in range(k):
            cur = heapq.heappop(pq)
            ans.append(cur[1])
        return ans

