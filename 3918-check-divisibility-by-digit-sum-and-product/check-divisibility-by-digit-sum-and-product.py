class Solution:
    def checkDivisibility(self, n: int) -> bool:
        """
        Check if n is divisible by the sum of (digit_sum + digit_product).
      
        Args:
            n: The input integer to check
          
        Returns:
            True if n is divisible by (sum of digits + product of digits), False otherwise
        """
        digit_sum = 0
        digit_product = 1
        temp_n = n
      
        # Extract each digit from the number
        while temp_n > 0:
            # Get the last digit and remaining number
            temp_n, digit = divmod(temp_n, 10)
          
            # Update sum and product of digits
            digit_sum += digit
            digit_product *= digit
      
        # Check if n is divisible by the sum of digit_sum and digit_product
        return n % (digit_sum + digit_product) == 0
