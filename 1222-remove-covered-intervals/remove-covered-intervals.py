from typing import List
import math

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by start time (ascending), 
        # if start times are equal, sort by end time (descending)
        # This ensures that if two intervals start at the same point,
        # the longer one comes first
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
      
        # Count of intervals that are not covered by other intervals
        non_covered_count = 0
      
        # Track the maximum end point seen so far
        # Initialize to negative infinity to ensure first interval is counted
        max_end_point = -math.inf
      
        # Iterate through sorted intervals
        for start, end in intervals:
            # If current interval's end extends beyond the maximum seen so far,
            # it's not covered by any previous interval
            if end > max_end_point:
                non_covered_count += 1
                max_end_point = end
            # Otherwise, this interval is covered by a previous interval
            # (no need to update max_end_point as end <= max_end_point)
      
        return non_covered_count
        