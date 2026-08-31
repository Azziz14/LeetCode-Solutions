class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def dfs(start_idx):
            # If we've reached the end of the string, return a list containing an empty string (representing a valid path)
            if start_idx == len(s):
                return [""]
            
            if start_idx in memo:
                return memo[start_idx]
            
            valid_sentences = []
            
            # Try every possible prefix ending at end_idx
            for end_idx in range(start_idx + 1, len(s) + 1):
                word = s[start_idx:end_idx]
                if word in word_set:
                    # Recursively find sentences for the remaining substring
                    sub_sentences = dfs(end_idx)
                    for sub in sub_sentences:
                        # Append the current word with the rest of the sentence
                        if sub:
                            valid_sentences.append(word + " " + sub)
                        else:
                            valid_sentences.append(word)
                            
            memo[start_idx] = valid_sentences
            return valid_sentences

        return dfs(0)