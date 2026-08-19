from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Dictionary to store reserved seats for each row using bit manipulation
        # Each row's reserved seats are represented as a bitmask
        reserved_by_row = defaultdict(int)
      
        # Convert reserved seats to bitmask representation
        # Seat j in row i becomes bit (10 - j) in the bitmask
        for row, seat in reservedSeats:
            reserved_by_row[row] |= 1 << (10 - seat)
      
        # Define masks for three possible 4-person family group positions:
        # - Left group: seats 2-5 (0b0111100000)
        # - Right group: seats 6-9 (0b0000011110)
        # - Middle group: seats 4-7 (0b0001111000)
        family_group_masks = (0b0111100000, 0b0000011110, 0b0001111000)
      
        # Start with maximum possible families in rows without any reservations
        # Each empty row can fit 2 families (left and right groups)
        total_families = (n - len(reserved_by_row)) * 2
      
        # Check each row with reservations
        for row_reservation in reserved_by_row.values():
            # Try to place family groups in this row
            for mask in family_group_masks:
                # Check if this group position has no conflicts with reserved seats
                if (row_reservation & mask) == 0:
                    # Mark these seats as occupied and count the family
                    row_reservation |= mask
                    total_families += 1
      
        return total_families