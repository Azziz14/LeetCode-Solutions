class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_parts = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                # Sum the digits of the current group and convert back to string
                group_sum = sum(int(ch) for ch in group)
                next_parts.append(str(group_sum))
            # Merge the new groups together
            s = "".join(next_parts)
        return s