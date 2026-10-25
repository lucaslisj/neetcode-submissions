class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = [0] * len(nums)
        rightproduct = [0] * len(nums)
        cur = 1
        for i in range(len(nums)):
            cur *= nums[i]
            leftproduct[i] = cur
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            cur *= nums[i]
            rightproduct[i] = cur
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(rightproduct[i + 1])
            elif i == len(nums) - 1:
                ans.append(leftproduct[i - 1])
            else:
                ans.append(leftproduct[i - 1] * rightproduct[i + 1])
        return ans