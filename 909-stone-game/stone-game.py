class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        from functools import cache
      
        @cache
        def calculate_score_difference(left: int, right: int) -> int:
            if left > right:
                return 0
            take_left = piles[left] - calculate_score_difference(left + 1, right)
            take_right = piles[right] - calculate_score_difference(left, right - 1)
          
            
            return max(take_left, take_right)
        return calculate_score_difference(0, len(piles) - 1) > 0