class Solution:
    def trap(self, height: List[int]) -> int:
        left_greatest = [] # tracks the largest bar on its left
        right_greatest = [] # tracks largest bar on its right
        maxx = 0
        ans = 0
        for i in range(0,len(height)):
            if i == 0:
                left_greatest.append(0)
                continue
            maxx = max(maxx,height[i - 1])
            left_greatest.append(maxx)
        maxx = 0
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right_greatest.append(0)
                continue
            maxx = max(maxx,height[i + 1])
            right_greatest.insert(0, maxx)
        for i in range(0,len(height)):
            ans += max(0, min(left_greatest[i],right_greatest[i]) - height[i])
        return ans


