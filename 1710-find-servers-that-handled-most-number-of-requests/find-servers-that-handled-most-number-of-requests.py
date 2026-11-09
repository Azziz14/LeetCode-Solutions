import heapq
import bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Min-heap to track busy servers: stores tuples of (release_time, server_id)
        busy = []
        
        # Sorted list of currently available server IDs
        available = list(range(k))
        
        # Track how many requests each server handled
        request_count = [0] * k
        
        for i, (arr, l) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have finished by the current arrival time
            while busy and busy[0][0] <= arr:
                _, server_id = heapq.heappop(busy)
                # Insert back into available list while maintaining sorted order
                bisect.insort(available, server_id)
            
            # 2. If no servers are available, drop the request
            if not available:
                continue
            
            # 3. Find the first available server >= (i % k)
            target = i % k
            idx = bisect.bisect_left(available, target)
            
            # If no server >= target is available, wrap around to the first available server
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # 4. Assign the request to this server
            request_count[server_id] += 1
            heapq.heappush(busy, (arr + l, server_id))
            
        # 5. Find the maximum requests handled by any server
        max_handled = max(request_count)
        
        # Return all servers that handled the maximum number of requests
        return [i for i, count in enumerate(request_count) if count == max_handled]