class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.append([nums[left],nums[right],nums[i]])
                    leftinitial = nums[left]
                    rightinitial = nums[right]
                    while left < right and nums[left] == leftinitial:
                        left += 1
                    while right > left and nums[right] == rightinitial:
                        right -= 1
                elif nums[left] + nums[right] > target:
       
                        right -= 1
                else:
       
                        left += 1
        return ans