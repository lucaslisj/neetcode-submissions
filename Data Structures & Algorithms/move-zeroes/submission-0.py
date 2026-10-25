class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        for tail in range(len(nums)):
            if nums[tail] != 0:
                nums[head],nums[tail] = nums[tail], nums[head]
                head += 1
