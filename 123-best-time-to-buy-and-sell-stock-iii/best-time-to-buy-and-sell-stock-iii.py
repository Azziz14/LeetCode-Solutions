class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        # Initialize states
        # Float('-inf') handles edge cases where prices array has fewer valid operations
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        
        for price in prices:
            # Maximize cash after 1st buy (lowest price seen so far)
            buy1 = max(buy1, -price)
            
            # Maximize profit after 1st sell
            sell1 = max(sell1, buy1 + price)
            
            # Maximize cash after 2nd buy (reinvesting sell1 profit)
            buy2 = max(buy2, sell1 - price)
            
            # Maximize profit after 2nd sell
            sell2 = max(sell2, buy2 + price)
            
        return sell2
