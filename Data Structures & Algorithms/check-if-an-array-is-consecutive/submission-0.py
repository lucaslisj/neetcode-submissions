class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        seen = set()
        for index, num in enumerate(nums):
            if index > 0 and num != nums[index - 1] + 1:
                return False
        return True
