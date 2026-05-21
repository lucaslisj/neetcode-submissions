class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        ans = 1001
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            mid = p1 + (p2 - p1) // 2
            ans = min(ans, nums[mid])
            if nums[mid] < nums[0]: ## on LHS
                p2 = mid - 1
            else: ## on RHS
                p1 = mid + 1
        return ans

        
                

        