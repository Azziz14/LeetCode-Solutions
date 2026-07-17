class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def check_height(node: TreeNode | None) -> int:
            # Base case: an empty tree has a height of 0
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # If current node violates balance condition, return -1
            if abs(left_height - right_height) > 1:
                return -1
                
            # Return actual height of this node's subtree
            return max(left_height, right_height) + 1

        # If check_height returns -1, the tree is unbalanced
        return check_height(root) != -1
