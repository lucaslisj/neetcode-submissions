class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        exceptlast = self.subsets(nums[:-1])
        ans = []
        for lst in exceptlast:
            ans.append(lst)
            ans.append(lst + [nums[-1]])
        return ans
