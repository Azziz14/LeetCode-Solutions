class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            # If a left child exists, we need to restructure it
            if curr.left:
                # Find the rightmost node in the left subtree
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Connect the rightmost node of left subtree to current's right subtree
                predecessor.right = curr.right
                
                # Move the left subtree to become the right subtree
                curr.right = curr.left
                curr.left = None
                
            # Move down the flattened right path
            curr = curr.right
