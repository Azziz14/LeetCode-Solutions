class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # Base case: empty tree
        if not root:
            return False
            
        # Base case: leaf node
        if not root.left and not root.right:
            return root.val == targetSum
            
        # Update targetSum for the child nodes
        remaining_sum = targetSum - root.val
        
        # Recursively check left and right subtrees
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))
