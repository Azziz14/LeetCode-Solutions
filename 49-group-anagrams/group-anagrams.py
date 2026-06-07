from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        # Key: sorted string (anagram signature)
        # Value: list of original strings that are anagrams
        anagram_groups = defaultdict(list)

        # Iterate through each string in the input list
        for string in strs:
            # Create a key by sorting the characters of the string
            # All anagrams will have the same sorted character sequence
            sorted_key = ''.join(sorted(string))

            # Add the original string to its anagram group
            anagram_groups[sorted_key].append(string)

        # Convert the dictionary values to a list and return
        # Each value is a list of strings that are anagrams of each other
        return list(anagram_groups.values())
