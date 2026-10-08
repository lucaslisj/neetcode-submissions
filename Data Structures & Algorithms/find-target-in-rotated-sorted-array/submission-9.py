class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] == target:
                return l
            if nums[mid] == target:
                return mid
            if nums[r] == target:
                return r
            print("Left: " + str(l))
            print("Mid: " + str(mid))
            print("Right: " + str(r))

            if nums[mid] > target:
                if  nums[l] > nums[mid] or nums[l] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[l] > target or nums[l] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1