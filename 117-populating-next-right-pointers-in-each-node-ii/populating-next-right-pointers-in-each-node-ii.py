class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
            
        # Start tracking from the root node
        curr = root
        
        while curr:
            # Dummy node acts as a fixed anchor before the start of the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse horizontally across the current level
            while curr:
                # If left child exists, attach it to our next-level linked list
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                    
                # If right child exists, attach it to our next-level linked list
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                    
                # Move to the next parent node on the current level
                curr = curr.next
                
            # Move down to the first node of the newly completed level
            curr = dummy.next
            
        return root
