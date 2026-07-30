class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
      
        # Build a 2D table to store palindrome information
        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome
        is_palindrome = [[True] * n for _ in range(n)]
      
        # Fill the palindrome table using dynamic programming
        # Start from the end of string and work backwards
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                # A substring is palindrome if:
                # 1. First and last characters match
                # 2. The inner substring is also a palindrome (or length <= 2)
                is_palindrome[start][end] = (s[start] == s[end] and 
                                             is_palindrome[start + 1][end - 1])
      
        # min_cuts[i] represents minimum cuts needed for s[0:i+1]
        # Initialize with worst case: i cuts for string of length i+1
        min_cuts = list(range(n))
      
        # Calculate minimum cuts for each position
        for i in range(1, n):
            # Check all possible last palindrome ending at position i
            for j in range(i + 1):
                # If s[j:i+1] is a palindrome
                if is_palindrome[j][i]:
                    if j == 0:
                        # If entire s[0:i+1] is palindrome, no cuts needed
                        min_cuts[i] = 0
                    else:
                        # Otherwise, it's cuts for s[0:j] plus one more cut
                        min_cuts[i] = min(min_cuts[i], 1 + min_cuts[j - 1])
      
        # Return minimum cuts for entire string
        return min_cuts[-1]