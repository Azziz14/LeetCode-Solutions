class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid_segment(start: int, end: int) -> bool:
            """
            Check if substring s[start:end+1] is a valid IP segment.
            Valid segment: 0-255, no leading zeros (except "0" itself)
            """
            # Check for leading zeros (invalid if segment starts with 0 and has multiple digits)
            if s[start] == "0" and start != end:
                return False
          
            # Check if the numeric value is within valid IP range [0, 255]
            segment_value = int(s[start:end + 1])
            return 0 <= segment_value <= 255
      
        def backtrack(start_index: int) -> None:
            """
            Recursively build valid IP addresses using backtracking.
            start_index: current position in the string to process
            """
            # Base case: successfully formed 4 segments and used all characters
            if start_index >= string_length and len(current_segments) == 4:
                result.append(".".join(current_segments))
                return
          
            # Pruning: stop if we've exceeded string length or already have 4 segments
            if start_index >= string_length or len(current_segments) >= 4:
                return
          
            # Try segments of length 1, 2, or 3 (IP segments can have at most 3 digits)
            for end_index in range(start_index, min(start_index + 3, string_length)):
                if is_valid_segment(start_index, end_index):
                    # Add current segment to the path
                    current_segments.append(s[start_index:end_index + 1])
                  
                    # Recursively process remaining string
                    backtrack(end_index + 1)
                  
                    # Backtrack: remove the segment for next iteration
                    current_segments.pop()
      
        # Initialize variables
        string_length = len(s)
        result = []  # Stores all valid IP addresses
        current_segments = []  # Temporary list to build current IP address
      
        # Start the backtracking process
        backtrack(0)
      
        return result