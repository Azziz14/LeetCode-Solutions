class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Calculate the minimum edit distance (Levenshtein distance) between two strings.
      
        Args:
            word1: The first string
            word2: The second string
          
        Returns:
            The minimum number of operations (insert, delete, replace) to transform word1 to word2
        """
        m, n = len(word1), len(word2)
      
        # Create a 2D DP table where dp[i][j] represents the edit distance
        # between word1[0:i] and word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
      
        # Initialize first row: transforming empty string to word2[0:j]
        # requires j insertions
        for j in range(1, n + 1):
            dp[0][j] = j
      
        # Fill the DP table
        for i, char1 in enumerate(word1, 1):
            # Initialize first column: transforming word1[0:i] to empty string
            # requires i deletions
            dp[i][0] = i
          
            for j, char2 in enumerate(word2, 1):
                if char1 == char2:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Characters don't match, take minimum of:
                    # dp[i-1][j] + 1: delete from word1
                    # dp[i][j-1] + 1: insert into word1
                    # dp[i-1][j-1] + 1: replace in word1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
      
        return dp[m][n]