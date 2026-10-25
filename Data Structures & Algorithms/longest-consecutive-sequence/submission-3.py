class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for num in nums:
            seen.add(num)
        for num in seen:
            if num - 1 in seen:
                continue
            streak = 0
            cur = num
            while cur in seen:
                streak += 1
                cur += 1
            ans = max(ans, streak)
        return ans