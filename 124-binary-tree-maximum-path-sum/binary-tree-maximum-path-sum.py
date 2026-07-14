# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize with negative infinity to handle trees with only negative values
        self.max_sum = float('-inf')
        
        def get_max_gain(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively calculate the maximum gain from left and right subtrees
            # If the gain is negative, ignore it by resetting to 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of a complete path passing through the current node as the peak
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum gain the current node can provide to its parent
            return node.val + max(left_gain, right_gain)
            
        get_max_gain(root)
        return self.max_sum
