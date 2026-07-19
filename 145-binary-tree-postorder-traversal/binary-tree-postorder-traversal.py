class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
            
        result = []
        stack = [root]
        
        # Traverse in Root -> Right -> Left order
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            
            # Push left first so right is popped and processed first
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                
        # Reverse the entire result array to get Left -> Right -> Root
        return result[::-1]
