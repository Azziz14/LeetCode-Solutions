class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Precompute powers of 10 for O(1) query time
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        # Prefix arrays (1-indexed for convenience)
        P = [0] * (n + 1)      # Positional value prefix hash
        cnt = [0] * (n + 1)    # Count of non-zero digits
        vsum = [0] * (n + 1)   # Sum of digits
        
        for i in range(1, n + 1):
            digit = int(s[i-1])
            if digit != 0:
                P[i] = (P[i-1] * 10 + digit) % MOD
                cnt[i] = cnt[i-1] + 1
                vsum[i] = vsum[i-1] + digit
            else:
                P[i] = P[i-1]
                cnt[i] = cnt[i-1]
                vsum[i] = vsum[i-1]
                
        ans = []
        for l, r in queries:
            # Convert 0-indexed query to 1-indexed representation
            l_idx, r_idx = l + 1, r + 1
            
            # Number of non-zero digits in the range
            k = cnt[r_idx] - cnt[l_idx - 1]
            if k == 0:
                ans.append(0)
                continue
                
            # Extract concatenated number x using the rolling hash formula
            x = (P[r_idx] - P[l_idx - 1] * pow10[k]) % MOD
            
            # Extract the sum of digits
            current_sum = vsum[r_idx] - vsum[l_idx - 1]
            
            # Compute final query answer
            ans.append((x * current_sum) % MOD)
            
        return ans
