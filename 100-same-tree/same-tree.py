class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both trees are empty, so they are identical
        if not p and not q:
            return True
        
        # One tree is empty and the other is not, so they are different
        if not p or not q:
            return False
        
        # The node values do not match
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
