class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        ans = 0
        for num in nums:
            seen.add(num)
        for num in nums:
            x = num
            if x - 1 not in seen:
                streak = 0
                while x in seen:
                    streak += 1
                    x += 1
                ans = max(ans, streak)
        return ans
        