class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i in range(len(nums)):
            cur = nums[i]
            if target - cur not in val_index:
                val_index[cur] = i
            else:
                if i < val_index[target - cur]:
                    return [i,val_index[target-cur]]
                else:
                    return [val_index[target-cur],i]

