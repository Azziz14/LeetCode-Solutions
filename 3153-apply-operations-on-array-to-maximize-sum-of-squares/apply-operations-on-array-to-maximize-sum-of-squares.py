class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 30
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        
        arr = [0] * len(nums)
        for i in range(30):
            for j in range(bit_counts[i]):
                arr[j] |= (1 << i)
                
        MOD = 10**9 + 7
        arr.sort(reverse=True)
        
        ans = 0
        for i in range(k):
            ans = (ans + arr[i] * arr[i]) % MOD
            
        return ans