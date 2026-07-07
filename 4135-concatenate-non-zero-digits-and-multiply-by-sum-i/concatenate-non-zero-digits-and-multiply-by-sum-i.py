class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert to string to easily process digits in order
        digits = [int(d) for d in str(n) if d != '0']
        
        if not digits:
            return 0
        
        # Reconstruct x from the non-zero digits
        x = int("".join(map(str, digits)))
        total_sum = sum(digits)
        
        return x * total_sum
