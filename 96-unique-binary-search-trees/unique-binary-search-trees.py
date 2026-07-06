class Solution:
    def numTrees(self, n: int) -> int:
        """
        Calculate the number of structurally unique BSTs that can be formed with n nodes.
        Uses dynamic programming to compute Catalan numbers.
      
        Args:
            n: Number of nodes (1 to n)
      
        Returns:
            Number of unique BST structures possible
        """
        # dp[i] represents the number of unique BSTs that can be formed with i nodes
        # Initialize with dp[0] = 1 (empty tree) and rest as 0
        dp = [1] + [0] * n
      
        # Build up the solution for each number of nodes from 1 to n
        for num_nodes in range(1, n + 1):
            # For each possible root position (1 to num_nodes)
            for root_position in range(1, num_nodes + 1):
                # Calculate number of BSTs with this root
                # Left subtree has (root_position - 1) nodes
                # Right subtree has (num_nodes - root_position) nodes
                left_subtree_count = dp[root_position - 1]
                right_subtree_count = dp[num_nodes - root_position]
              
                # Total combinations = left combinations × right combinations
                dp[num_nodes] += left_subtree_count * right_subtree_count
      
        return dp[n]
