from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal of a binary tree.
      
        Args:
            root: The root node of the binary tree.
          
        Returns:
            A list containing the values of nodes in inorder sequence.
        """
      
        def traverse_inorder(node: Optional[TreeNode]) -> None:
            """
            Helper function to recursively traverse the tree in inorder.
            Left subtree -> Current node -> Right subtree
          
            Args:
                node: The current node being processed.
            """
            # Base case: if node is None, return
            if node is None:
                return
          
            # Traverse left subtree first
            traverse_inorder(node.left)
          
            # Process current node (add its value to result)
            result.append(node.val)
          
            # Traverse right subtree
            traverse_inorder(node.right)
      
        # Initialize result list to store traversal values
        result: List[int] = []
      
        # Start traversal from root
        traverse_inorder(root)
      
        return result