class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        # Step 1: Deduplicate elements and compute max bounds
        unique_nums = list(set(nums))
        max_val = max(unique_nums)
        
        # Calculate upper limit for XOR capacity (next power of 2)
        limit = 1
        while limit <= max_val:
            limit <<= 1
        limit <<= 1  # Expand bound to accommodate combination pairs
        
        # Boolean arrays for absolute O(1) existence checks
        has_num = [False] * limit
        for num in unique_nums:
            has_num[num] = True
            
        # Step 2: Record all valid 2-element XOR outputs
        has_pair = [False] * limit
        for i in range(limit):
            if has_num[i]:
                for num in unique_nums:
                    has_pair[i ^ num] = True
                    
        # Step 3: Record all valid 3-element XOR outputs
        has_triplet = [False] * limit
        unique_count = 0
        
        for i in range(limit):
            if has_pair[i]:
                for num in unique_nums:
                    triplet_xor = i ^ num
                    if not has_triplet[triplet_xor]:
                        has_triplet[triplet_xor] = True
                        unique_count += 1
                        
        return unique_count
