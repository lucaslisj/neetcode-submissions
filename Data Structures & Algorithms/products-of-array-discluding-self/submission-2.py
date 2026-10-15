class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = [0] * len(nums) #inclusive of current
        rightproduct = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                leftproduct[i] = nums[0]
                rightproduct[-1] = nums[-1]
            else:
                leftproduct[i] = leftproduct[i - 1] * nums[i]
                rightproduct[len(nums) - i - 1] = rightproduct[len(nums) - i] * nums[len(nums) - i - 1]
        
        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(rightproduct[1])
            elif i == len(nums) - 1:
                ans.append(leftproduct[len(nums) - 2])
            else:
                ans.append(rightproduct[i + 1] * leftproduct[i - 1])
        return ans