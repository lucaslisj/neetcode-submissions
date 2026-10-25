class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = 101
        ans = 0
        for i in range(len(prices)):
            minn = min(minn,prices[i])
            ans = max(ans, prices[i] - minn)
        return ans