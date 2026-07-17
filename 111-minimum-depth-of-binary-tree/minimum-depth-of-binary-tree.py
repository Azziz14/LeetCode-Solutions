from collections import deque

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        # Base case: empty tree
        if not root:
            return 0
            
        # Initialize queue with (node, current_depth)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # The first leaf node we encounter gives the minimum depth
            if not node.left and not node.right:
                return depth
                
            # Add children to the queue
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return 0
