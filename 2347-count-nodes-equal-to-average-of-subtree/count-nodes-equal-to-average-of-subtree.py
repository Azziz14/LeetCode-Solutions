# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.matching_nodes_count = 0
        
        def calculate_subtree_stats(node: TreeNode) -> tuple[int, int]:
            if not node:
                return 0, 0  # (subtree_sum, subtree_count)
            
            # Post-order traversal: collect data from children
            left_sum, left_count = calculate_subtree_stats(node.left)
            right_sum, right_count = calculate_subtree_stats(node.right)
            
            # Calculate metrics for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check the average condition (integer division matches floor requirement)
            if current_sum // current_count == node.val:
                self.matching_nodes_count += 1
                
            return current_sum, current_count

        calculate_subtree_stats(root)
        return self.matching_nodes_count
