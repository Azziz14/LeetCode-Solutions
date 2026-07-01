class Solution:
    def partition(self, head, x):
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        small = small_dummy
        big = big_dummy

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next

        # end big list
        big.next = None

        # connect small + big
        small.next = big_dummy.next

        return small_dummy.next