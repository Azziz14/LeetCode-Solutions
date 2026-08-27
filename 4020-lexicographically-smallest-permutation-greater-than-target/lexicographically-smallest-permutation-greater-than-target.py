from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        prefix_counts = [None] * (n + 1)
        prefix_counts[0] = counts.copy()
        
        matched_len = 0
        curr_counts = counts.copy()
        for i in range(n):
            char = target[i]
            if curr_counts[char] > 0:
                curr_counts[char] -= 1
                matched_len += 1
                prefix_counts[matched_len] = curr_counts.copy()
            else:
                break
        for i in range(matched_len, -1, -1):
            if i == n:
                continue
                
            avail = prefix_counts[i]
            target_char = target[i]
            for ch_code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(ch_code)
                if avail[ch] > 0:
                    rem = avail.copy()
                    rem[ch] -= 1
                    
                    suffix = []
                    for c in sorted(rem.keys()):
                        suffix.append(c * rem[c])
                        
                    return target[:i] + ch + "".join(suffix)
                    
        return ""