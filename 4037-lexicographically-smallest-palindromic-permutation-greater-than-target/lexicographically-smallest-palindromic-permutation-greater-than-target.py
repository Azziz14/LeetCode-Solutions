from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        
        odd_chars = [ch for ch, cnt in counts.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        half_len = n // 2
        half_counts = {ch: cnt // 2 for ch, cnt in counts.items()}
        
        def build_palindrome(half: list) -> str:
            first = "".join(half)
            return first + mid_char + first[::-1]
            
        def fill_remaining(available: dict) -> list:
            res = []
            for ch in sorted(available.keys()):
                res.extend([ch] * available[ch])
            return res

        exact_half = []
        curr_counts = half_counts.copy()
        can_match_prefix = True
        
        for i in range(half_len):
            t_char = target[i]
            if curr_counts.get(t_char, 0) > 0:
                exact_half.append(t_char)
                curr_counts[t_char] -= 1
            else:
                can_match_prefix = False
                break
                
        if can_match_prefix:
            cand = build_palindrome(exact_half)
            if cand > target:
                return cand

        curr_counts = half_counts.copy()
        prefix = []
        
        history = [(list(prefix), curr_counts.copy())]
        for i in range(half_len):
            t_char = target[i]
            if curr_counts.get(t_char, 0) > 0:
                prefix.append(t_char)
                curr_counts[t_char] -= 1
                history.append((list(prefix), curr_counts.copy()))
            else:
                break
                
        for idx in range(len(history) - 1, -1, -1):
            pref, avail = history[idx]
            if idx == half_len:
                continue
                
            t_char = target[idx]
            
            for ch in sorted(avail.keys()):
                if ch > t_char and avail[ch] > 0:
                    next_avail = avail.copy()
                    next_avail[ch] -= 1
                    
                    full_half = pref + [ch] + fill_remaining(next_avail)
                    cand = build_palindrome(full_half)
                    
                    if cand > target:
                        return cand
                        
        return ""