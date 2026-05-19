class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            num1 = nums[i]
            target = -num1

            seen = set()
            cannotuse = set()
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                if target - num2 in seen and target - num2 not in cannotuse:
                    ans.append([num1,num2,target-num2])
                    cannotuse.add(num2)
                    cannotuse.add(target - num2)
                else:
                    seen.add(num2)
        return ans
            