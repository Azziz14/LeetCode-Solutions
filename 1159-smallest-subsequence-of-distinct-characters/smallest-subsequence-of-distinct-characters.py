class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Step 1: Find the last occurrence index of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        stack = []
        seen = set()  # To check if a character is already in our stack
        
        # Step 2: Iterate through the string
        for idx, char in enumerate(s):
            # Skip if the character is already included in the current sequence
            if char in seen:
                continue
                
            # Pop elements from stack if they are larger than char 
            # AND occur again later in the string
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > idx:
                removed_char = stack.pop()
                seen.remove(removed_char)
                
            # Add the current character to stack and marked as seen
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)
