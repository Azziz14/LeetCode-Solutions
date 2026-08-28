from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for ch in strs: 
            key = ''.join(sorted(ch))
            if key not in group:
                group[key]=[]
            group[key].append(ch)
        return list(group.values())
