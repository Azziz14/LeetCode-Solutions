class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        i, n = 0, len(words)
        
        while i < n:
            current_words = [words[i]]
            current_length = len(words[i])
            i += 1
            
            # Pack words into the current line
            while i < n and current_length + 1 + len(words[i]) <= maxWidth:
                current_length += 1 + len(words[i])
                current_words.append(words[i])
                i += 1
                
            # Left-justify if it's the last line or there's only one word in the line
            if i == n or len(current_words) == 1:
                left_aligned = " ".join(current_words)
                padding = " " * (maxWidth - len(left_aligned))
                ans.append(left_aligned + padding)
                continue
                
            # Fully justify if there are multiple words
            total_spaces = maxWidth - (current_length - len(current_words) + 1)
            gaps = len(current_words) - 1
            
            space_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            
            row = []
            for j, word in enumerate(current_words[:-1]):
                row.append(word)
                spaces_to_add = space_per_gap + (1 if j < extra_spaces else 0)
                row.append(" " * spaces_to_add)
            
            row.append(current_words[-1])
            ans.append("".join(row))
            
        return ans
