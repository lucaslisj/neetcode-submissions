class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        dppos = [0] * len(nums)
        dpneg = [0] * len(nums)

        for index, value in enumerate(nums):
            if index == 0:
                if value > 0:
                    dppos[index] = value
                    dpneg[index] = 0
                elif value < 0:
                    dppos[index] = 0
                    dpneg[index] = value
                else:
                    dppos[index] = 0
                    dpneg[index] = 0
            elif value > 0:
                dppos[index] = max(dppos[index - 1] * value, value)
                dpneg[index] = min(dpneg[index - 1] * value, value)
            elif value < 0:
                dppos[index] = max(value, dpneg[index - 1] * value)
                dpneg[index] = min(value, dppos[index - 1] * value)
            else:
                dppos[index] = 0
                dpneg[index] = 0
            if dppos[index] > 0:
                ans = max(ans,dppos[index])
            ans = max(ans,dpneg[index])
        return ans