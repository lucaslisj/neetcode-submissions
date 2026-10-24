class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numtoindex = {}
        for index, num in enumerate(nums):
            if target - num in numtoindex:
                if index > numtoindex[target - num]:
                    return [numtoindex[target - num], index]
                return [index, numtoindex[target - num]]
            numtoindex[num] = index
        
            