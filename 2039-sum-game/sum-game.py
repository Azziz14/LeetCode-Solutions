class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')
        
        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        
       
        return (left_sum - right_sum) * 2 != (right_q - left_q) * 9