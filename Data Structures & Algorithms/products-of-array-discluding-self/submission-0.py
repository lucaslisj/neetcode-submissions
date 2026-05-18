class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            total *= num
        ans = []
        if zero_count > 1:
            for i in range(len(nums)):
                ans.append(0)
            return ans
        
        for num in nums:
            if zero_count == 1:
                if num != 0:
                    ans.append(0)
                else:
                    ans.append(total)
            else:
                ans.append(total // num)
        return ans