class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Sort the first half of the string characters
        first_half = sorted(s[:n // 2])
        first_half_str = "".join(first_half)
        
        # Identify the middle character if the string length is odd
        mid_char = s[n // 2] if n % 2 != 0 else ""
        
        # Mirror the sorted first half to build the full palindrome
        return first_half_str + mid_char + first_half_str[::-1]
