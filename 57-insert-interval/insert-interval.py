class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Insert a new interval into a list of non-overlapping intervals and merge if necessary.
      
        Args:
            intervals: List of non-overlapping intervals sorted by start time
            newInterval: The interval to be inserted
          
        Returns:
            List of intervals after insertion with all overlapping intervals merged
        """
      
        def merge_intervals(interval_list: List[List[int]]) -> List[List[int]]:
            """
            Merge overlapping intervals in a list.
          
            Args:
                interval_list: List of intervals that may have overlaps
              
            Returns:
                List of merged non-overlapping intervals
            """
            # Sort intervals by their start time
            interval_list.sort()
          
            # Initialize result with the first interval
            merged_result = [interval_list[0]]
          
            # Iterate through remaining intervals
            for start, end in interval_list[1:]:
                # Check if current interval overlaps with the last merged interval
                if merged_result[-1][1] < start:
                    # No overlap - add as a new interval
                    merged_result.append([start, end])
                else:
                    # Overlap exists - extend the end time of the last merged interval
                    merged_result[-1][1] = max(merged_result[-1][1], end)
          
            return merged_result
      
        # Add the new interval to the existing intervals
        intervals.append(newInterval)
      
        # Merge all intervals and return the result
        return merge_intervals(intervals)
