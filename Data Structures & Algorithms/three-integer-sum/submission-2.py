class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            j = i + 1
            seen = set()
            target = -nums[i]
            while j < len(nums):
                cur = nums[j]
                if target - cur in seen:
                    lst = [target - cur,cur,nums[i]]
                    lst.sort()
                    ans.add(tuple(lst))
                seen.add(cur)
                j += 1
        anss = []
        for lst in ans:
            one = lst[0]
            two = lst[1]
            three = lst[2]
            anss.append([one,two,three])
        return anss