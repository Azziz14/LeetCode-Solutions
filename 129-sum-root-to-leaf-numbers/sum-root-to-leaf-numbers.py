# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0
            
            # Calculate path value up to the current node
            current_sum = current_sum * 10 + node.val
            
            # If leaf node is reached, return the path sum
            if not node.left and not node.right:
                return current_sum
            
            # Recursively sum up paths from left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
            
        return dfs(root, 0)
