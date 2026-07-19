class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            
            # Push right child first so left child is processed first
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return result
