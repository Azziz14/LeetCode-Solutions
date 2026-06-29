class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        """
        Count how many patterns are substrings of the given word.
      
        Args:
            patterns: List of pattern strings to check
            word: The target string to search within
          
        Returns:
            Number of patterns that exist as substrings in word
        """
        # Initialize counter for matching patterns
        count = 0
      
        # Iterate through each pattern in the list
        for pattern in patterns:
            # Check if current pattern is a substring of word
            if pattern in word:
                count += 1
      
        return count