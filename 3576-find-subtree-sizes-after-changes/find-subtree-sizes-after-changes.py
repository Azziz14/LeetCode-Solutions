class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        new_parent = list(parent)
        last_seen = {}
        
        def dfs_reparent(u):
            char = s[u]
            prev = last_seen.get(char)
            if prev is not None:
                new_parent[u] = prev
            last_seen[char] = u
            
            for v in adj[u]:
                dfs_reparent(v)
                
            if prev is None:
                del last_seen[char]
            else:
                last_seen[char] = prev
                
        dfs_reparent(0)
        
        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
            
        ans = [0] * n
        
        def dfs_size(u):
            size = 1
            for v in new_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size
            
        dfs_size(0)
        return ans