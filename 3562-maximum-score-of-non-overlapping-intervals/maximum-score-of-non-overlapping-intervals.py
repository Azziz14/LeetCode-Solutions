from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indexed_intervals = []
        for i, (l, r, w) in enumerate(intervals):
            indexed_intervals.append((l, r, w, i))
        
        indexed_intervals.sort(key=lambda x: (x[0], x[1]))
        
        starts = [x[0] for x in indexed_intervals]
        
        dp = {}
        
        def solve(idx, count):
            if count == 4 or idx == n:
                return 0, []
            
            if (idx, count) in dp:
                return dp[(idx, count)]
            
            skip_weight, skip_indices = solve(idx + 1, count)
            
            l, r, w, original_idx = indexed_intervals[idx]
            
            target_idx = bisect_right(starts, r)
            
            take_weight, take_indices = solve(target_idx, count + 1)
            take_weight += w
            take_indices = take_indices + [original_idx]
            
            if take_weight > skip_weight:
                res = (take_weight, take_indices)
            elif take_weight < skip_weight:
                res = (skip_weight, skip_indices)
            else:
                if sorted(take_indices) < sorted(skip_indices):
                    res = (take_weight, take_indices)
                else:
                    res = (skip_weight, skip_indices)
            
            dp[(idx, count)] = res
            return res

        _, best_indices = solve(0, 0)
        return sorted(best_indices)