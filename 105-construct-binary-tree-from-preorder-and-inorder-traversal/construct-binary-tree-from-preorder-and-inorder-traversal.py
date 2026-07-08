# Do NOT include the "class TreeNode:" block here. LeetCode provides it behind the scenes.

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def array_to_tree(left_in, right_in):
            if left_in > right_in:
                return None
            
            root_val = preorder[self.pre_idx]
            # This will now correctly use LeetCode's internal TreeNode class
            root = TreeNode(root_val) 
            self.pre_idx += 1
            
            pivot = inorder_map[root_val]
            
            root.left = array_to_tree(left_in, pivot - 1)
            root.right = array_to_tree(pivot + 1, right_in)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)
