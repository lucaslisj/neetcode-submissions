class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        ans = 0
        while(p1 < p2):
            base = p2 - p1
            height = min(heights[p1],heights[p2])
            ans = max(ans,base * height)
            if heights[p1] <= heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return ans
