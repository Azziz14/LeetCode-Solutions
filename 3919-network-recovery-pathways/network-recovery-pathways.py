import collections
import heapq

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        # Derive n from the length of the online status array
        n = len(online)
        
        # Build the adjacency list: adj[u] = [(v, cost), ...]
        adj = collections.defaultdict(list)
        for u, v, cost in edges:
            adj[u].append((v, cost))
            
        # Helper function to check if a path score >= mid is possible
        def check(mid):
            # Min-heap stores tuples of (accumulated_cost, current_node)
            pq = [(0, 0)]
            # Track minimum cost to reach each node under the current 'mid' constraint
            min_cost = {i: float('inf') for i in range(n)}
            min_cost[0] = 0
            
            while pq:
                curr_cost, u = heapq.heappop(pq)
                
                if curr_cost > min_cost[u]:
                    continue
                if u == n - 1:
                    return curr_cost <= k
                    
                for v, cost in adj[u]:
                    # Filter out edges below our guessed bottleneck score
                    # Filter out intermediate nodes that are offline
                    if cost >= mid and (v == n - 1 or online[v]):
                        next_cost = curr_cost + cost
                        if next_cost < min_cost[v] and next_cost <= k:
                            min_cost[v] = next_cost
                            heapq.heappush(pq, (next_cost, v))
            return False

        # Extract all unique edge costs to bound our binary search
        possible_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        low = 0
        high = len(possible_costs) - 1
        ans = -1
        
        # Binary search over the indices of sorted unique edge costs
        while low <= high:
            mid_idx = (low + high) // 2
            mid_val = possible_costs[mid_idx]
            
            if check(mid_val):
                ans = mid_val  # Track the maximum valid bottleneck score found
                low = mid_idx + 1  # Try to find a larger minimum edge cost
            else:
                high = mid_idx - 1  # Reduce the minimum edge constraint
                
        return ans
