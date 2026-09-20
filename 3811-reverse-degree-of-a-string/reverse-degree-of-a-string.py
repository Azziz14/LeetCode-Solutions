class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            rev_alphabet_index = 123 - ord(char)
            total += rev_alphabet_index * i
        return total