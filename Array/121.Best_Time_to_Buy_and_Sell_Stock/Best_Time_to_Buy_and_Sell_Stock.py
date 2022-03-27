class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = 1000000
        for price in prices:
            if not mn < 1000000 and price > mn: ans = max(ans, price - mn)
            if price < mn: mn = price
        return ans
        