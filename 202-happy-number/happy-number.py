class Solution:
    def isHappy(self, n: int) -> bool:
        # Helper function to compute the sum of squares of digits
        def get_next(num: int) -> int:
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum
            
        # Initialize Tortoise and Hare pointers
        slow = n
        fast = get_next(n)
        
        # Loop until fast reaches 1 or pointers meet in a cycle
        while fast != 1 and slow != fast:
            slow = get_next(slow)          # Moves 1 step
            fast = get_next(get_next(fast)) # Moves 2 steps
            
        return fast == 1
