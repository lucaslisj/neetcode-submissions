class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while (p1 <= p2):
            mid = p1 + (p2 - p1) // 2
            if nums[p1] == target:
                return p1
            if nums[p2] == target:
                return p2
            if nums[mid] == target:
                return mid
            ileft = (nums[p1] >= nums[mid]) # true if inflection is on LHS (the array inclusive of mid)
            iright = (nums[p2] <= nums[mid]) # true if inflection is on RHS (inclusive of mid)
            if nums[mid] > target: ## need to find places where numbers could be lower
                if not ileft and not iright: ## monotonic
                    if nums[p1] > target:
                        return -1
                    else:
                        p2 = mid - 1 ## has to be on left half if it exists
                elif ileft: #inflection on the left, monotically increasing on RHS
                    p2 = mid - 1 # has to be on the left because right nunmbers only get larger
                
                else: # inflection on the right, monotonically increasing on LHS 
                    if nums[p1] > target: # LHS all too large
                        p1 = mid + 1
                    else: # has to be on LHS since it monotonically increases from nums[p1] to nums[mid] and the target is somewhere between if it exists
                          # RHS before inflection is too large and after inflection is too small (cuz values after inflection are less than nums[p1] which is too small) 
                        p2 = mid - 1
            
            else: ## need to find places wehre numbers could get larger
                if not ileft and not iright: ## overall monotonic
                    if nums[p2] < target: 
                        return -1
                    else:
                        p1 = mid + 1
                elif ileft: #inflection on the left, RHS monotonically increasing
                    if nums[p2] < target: #RHS all too small
                        p2 = mid - 1
                    else: #has to be on RHS because RHS monotonically increases and the largest value on RHS is sufficiently large enough
                          # LHS before inflection is too large because it is larger than nums[p2] which is already too large and LHS after inflection is smaller than nums[mid] which is too small
                        p1 = mid + 1
                else: #inflection on the right, LHS monotonically increasing
                    p1 = mid + 1 ## cannot be on the left cuz all too small
        return -1



        