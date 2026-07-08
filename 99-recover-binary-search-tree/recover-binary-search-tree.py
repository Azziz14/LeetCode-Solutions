class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            # 1. Traverse the left subtree
            inorder(node.left)
            
            # 2. Process current node: check for BST property violation
            if self.prev and self.prev.val > node.val:
                # If this is the first violation, the larger node (prev) is out of order
                if not self.first:
                    self.first = self.prev
                # The smaller node (node) is always a candidate for the second swapped node
                self.second = node
            
            # Update prev to be the current node before heading right
            self.prev = node
            
            # 3. Traverse the right subtree
            inorder(node.right)
            
        # Run traversal and swap values back to fix the tree
        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
