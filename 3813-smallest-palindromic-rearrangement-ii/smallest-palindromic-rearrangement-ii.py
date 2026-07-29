import collections

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = collections.Counter(s)
        
        # Step 2: Validate if a palindrome can be formed
        odd_chars = [char for char, freq in counts.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        # Keep track of the lone middle character if length is odd
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Prepare counts for the left half
        left_counts = {}
        total_left_len = 0
        for char in sorted(counts.keys()):
            left_counts[char] = counts[char] // 2
            total_left_len += left_counts[char]

        # Precompute factorials up to total_left_len for the initial calculation
        # Using a fixed-size loop for initial setup is highly efficient
        fact = [1] * (total_left_len + 1)
        for i in range(1, total_left_len + 1):
            fact[i] = fact[i - 1] * i

        # Calculate total unique permutations for the initial left half configuration
        total_perms = fact[total_left_len]
        for freq in left_counts.values():
            if freq > 1:
                total_perms //= fact[freq]

        # If the requested k is larger than the total possible permutations, it's impossible
        if total_perms < k:
            return ""
            
        left_half = []
        available_chars = sorted([c for c, freq in left_counts.items() if freq > 0])

        # Step 3: Efficient digit placement using O(1) mathematical transitions
        for i in range(total_left_len):
            remaining_len = total_left_len - i
            
            for char in available_chars:
                if left_counts[char] > 0:
                    # Mathematical Reduction Rule:
                    # If we pick 'char', the new total permutation count is derived by:
                    # multiplying by the character's current frequency, and dividing by the remaining total length.
                    current_perms = (total_perms * left_counts[char]) // remaining_len
                    
                    if k <= current_perms:
                        # The target string lies within this character's lexicographical block
                        left_half.append(char)
                        left_counts[char] -= 1
                        total_perms = current_perms  # Transition to the next state seamlessly
                        break
                    else:
                        # Skip this character block and deduct its permutation size from k
                        k -= current_perms

            # Clean up characters that have run out of stock to keep the inner loop fast
            available_chars = [c for c in available_chars if left_counts[c] > 0]
                        
        # Step 4: Mirror the string to produce the full palindrome
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]
