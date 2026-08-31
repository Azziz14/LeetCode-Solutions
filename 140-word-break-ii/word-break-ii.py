class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def dfs(start_idx):
            if start_idx == len(s):
                return [""]
            
            if start_idx in memo:
                return memo[start_idx]
            
            valid_sentences = []
            for end_idx in range(start_idx + 1, len(s) + 1):
                word = s[start_idx:end_idx]
                if word in word_set:
                    sub_sentences = dfs(end_idx)
                    for sub in sub_sentences:
                        if sub:
                            valid_sentences.append(word + " " + sub)
                        else:
                            valid_sentences.append(word)
                            
            memo[start_idx] = valid_sentences
            return valid_sentences

        return dfs(0)