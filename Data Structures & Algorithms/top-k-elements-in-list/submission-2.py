class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        counts = {}
        ans = []
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        for key, value in counts.items():
            heapq.heappush(h,(-value, key))
        
        while k:
            ans.append(heapq.heappop(h)[1])
            k -= 1
        return ans
