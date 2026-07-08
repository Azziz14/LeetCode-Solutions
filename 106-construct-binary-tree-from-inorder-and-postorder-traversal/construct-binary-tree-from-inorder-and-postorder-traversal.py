class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional['TreeNode']:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(in_start, in_end):
            if in_start > in_end:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            root_idx = inorder_map[root_val]
            
            root.right = build(root_idx + 1, in_end)
            root.left = build(in_start, root_idx - 1)
            
            return root
            
        return build(0, len(inorder) - 1)
