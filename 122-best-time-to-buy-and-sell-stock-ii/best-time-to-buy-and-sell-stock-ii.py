class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Iterate from the second day to the end
        for i in range(1, len(prices)):
            # If the price increased compared to yesterday, take the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit
