import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        
        # Min-heap for available servers: stores tuples of (weight, index)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        
        # Min-heap for busy servers: stores tuples of (time_free, weight, index)
        busy_servers = []
        
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            current_time = max(current_time, j)
            
            # If no servers are available, jump time to when the next server frees up
            if not free_servers and busy_servers[0][0] > current_time:
                current_time = busy_servers[0][0]
                
            # Release all servers that become free at or before current_time
            while busy_servers and busy_servers[0][0] <= current_time:
                time_free, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
                
            # Assign the task to the top available server
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            
            # Push the server into the busy heap with its future release time
            heapq.heappush(busy_servers, (current_time + tasks[j], weight, index))
            
        return ans