class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Step 1: Build the adjacency list for the graph
        graph = {i: [] for i in range(n)}
        for u, v in invocations:
            graph[u].append(v)
        
        # Step 2: Identify all suspicious methods using DFS
        suspicious = set()
        
        def dfs(node):
            suspicious.add(node)
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    dfs(neighbor)
                    
        dfs(k)
        
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Cannot remove anything, return all methods
                return list(range(n))
                
        # Step 4: Return remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]
