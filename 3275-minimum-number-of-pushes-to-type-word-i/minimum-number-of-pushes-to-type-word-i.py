class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculate the minimum number of button pushes needed to type a word.
      
        Strategy: Assign letters to 8 keys (keys 2-9 on a phone keypad).
        - First 8 letters: 1 push each (one letter per key)
        - Next 8 letters: 2 pushes each (second letter on each key)
        - Next 8 letters: 3 pushes each (third letter on each key)
        - And so on...
      
        Args:
            word: The input string to be typed
          
        Returns:
            The minimum number of button pushes required
        """
        word_length = len(word)
        total_pushes = 0
        push_multiplier = 1  # Number of pushes needed for current group of 8 letters
      
        # Process complete groups of 8 letters
        complete_groups = word_length // 8
        for _ in range(complete_groups):
            total_pushes += push_multiplier * 8  # Each of 8 letters needs push_multiplier pushes
            push_multiplier += 1  # Next group needs one more push per letter
      
        # Process remaining letters (less than 8)
        remaining_letters = word_length % 8
        total_pushes += push_multiplier * remaining_letters
      
        return total_pushes
