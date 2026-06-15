class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_P = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l += 1
            else:
                max_P = max(max_P, prices[r] - prices[l])
        return max_P