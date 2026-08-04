class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # If total fuel available is less than total fuel needed, 
        # a complete circuit is impossible.
        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            # If the tank falls below 0, station i cannot be reached 
            # from the current start_index or any station before it.
            if total_tank < 0:
                # Reset start position to the next station
                start_index = i + 1
                # Reset the running tank for the new starting point
                total_tank = 0
                
        return start_index
