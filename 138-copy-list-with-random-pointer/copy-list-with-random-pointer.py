class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        copied_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next
            if copy.next:
                copy.next = copy.next.next    
        return copied_head