class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            num1 = nums[i]
            target = -num1
            p1 = i + 1
            p2 = len(nums) - 1
            while(p1 < p2):
                if nums[p1] + nums[p2] == target:
                    ans.append([num1,nums[p1],nums[p2]])
                    p1 += 1
                    while(p1 < p2 and nums[p1] == nums[p1 - 1]):
                        p1 += 1
                elif nums[p1] + nums[p2] > target:
                    p2 -= 1
                else:
                    p1 += 1
        return ans
            