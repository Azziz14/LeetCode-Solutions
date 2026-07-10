class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # Step 1: Track original indices and sort by node value
        sorted_nodes = sorted([(nums[i], i) for i in range(n)])
        
        # Map original index -> sorted position index
        pos = [0] * n
        for idx, (_, orig_idx) in enumerate(sorted_nodes):
            pos[orig_idx] = idx

        # Step 2: Compute furthest 1-step jump for each position using two pointers
        # LOG size 18 covers up to 2^17 = 131,072 elements (N <= 10^5)
        LOG = 18 
        st = [[0] * LOG for _ in range(n)]
        
        r = 0
        for i in range(n):
            r = max(r, i)
            # Expand the window while the value difference is within maxDiff
            while r + 1 < n and sorted_nodes[r + 1][0] - sorted_nodes[i][0] <= maxDiff:
                r += 1
            st[i][0] = r

        # Step 3: Populate the Binary Lifting Table (DP)
        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        # Step 4: Process Queries
        answer = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if a > b:
                a, b = b, a  # Graph is undirected; traversal direction doesn't matter
                
            if a == b:
                answer.append(0)
                continue
                
            curr = a
            steps = 0
            
            # Binary lifting: jump by decreasing powers of 2 as long as we stay strictly left of target b
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)
                    
            # Check if one final structural step can cover or pass target b
            if st[curr][0] >= b:
                answer.append(steps + 1)
            else:
                answer.append(-1)  # Unreachable / disjoint sub-graphs

        return answer
