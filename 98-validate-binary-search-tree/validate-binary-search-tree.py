class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # Base case: an empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must fall strictly within the allowed range
            if not (low < node.val < high):
                return False
            
            # Left child's upper bound becomes node.val
            # Right child's lower bound becomes node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
            
        return validate(root)
