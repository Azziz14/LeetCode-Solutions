class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        # Base Case 1: Empty list
        if not head:
            return None
        
        # Base Case 2: Only one element
        if not head.next:
            return TreeNode(head.val)
            
        # Step 1: Use slow/fast pointers to find the middle
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Disconnect the left half from the middle node
        if prev:
            prev.next = None
            
        # Step 3: Create the root node
        root = TreeNode(slow.val)
        
        # Step 4: Recursively build the left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
