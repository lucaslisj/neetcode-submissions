class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        ans = 0
        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > ans:
                ans = price - lowest
        return ans
        