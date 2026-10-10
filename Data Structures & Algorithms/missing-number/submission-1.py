class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minn = nums[0]
        maxx = nums[0]
        for num in nums:
            minn = min(minn, num)
            maxx = max(maxx, num)
        if minn != 0:
            return 0
        if maxx != len(nums):
            return len(nums)
        # now the edge cases are handled and the numbers should be from 0 to n inclusive
        n = len(nums)
        math_sum = n * (n + 1) // 2
        real_sum = 0
        for num in nums:
            real_sum += num
        return math_sum - real_sum