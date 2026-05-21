class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        p1 = 0
        p2 = len(nums) - 1
        mid = p1 + (p2 - p1) // 2
        
        if nums[mid] < nums[0]: ## its on the LHS
            return min(nums[mid], self.findMin(nums[: mid]))
        return min(nums[mid], self.findMin(nums[mid + 1 :])) ## its on the RHS


        
                

        