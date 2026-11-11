class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # 1. Satisfy the minimum of both needs using the cheaper option between costBoth and (cost1 + cost2)
        common_need = min(need1, need2)
        total_cost = common_need * min(costBoth, cost1 + cost2)
        
        # 2. Subtract the fulfilled portion
        need1 -= common_need
        need2 -= common_need
        
        # 3. Handle any remaining need for type 1 using either cost1 or costBoth
        total_cost += need1 * min(costBoth, cost1)
        
        # 4. Handle any remaining need for type 2 using either cost2 or costBoth
        total_cost += need2 * min(costBoth, cost2)
        
        return total_cost