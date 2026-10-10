class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        rob_first_dp = {}
        norob_first_dp = {}
        rob_first_dp[0] = nums[0]
        rob_first_dp[1] = nums[0]
        norob_first_dp[0] = 0
        norob_first_dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            rob_first_dp[i] = max(rob_first_dp[i - 1], rob_first_dp[i - 2] + nums[i])
            norob_first_dp[i] = max(norob_first_dp[i - 1],norob_first_dp[i - 2] + nums[i])

        return max(rob_first_dp[len(nums) - 2], norob_first_dp[len(nums) - 1])

