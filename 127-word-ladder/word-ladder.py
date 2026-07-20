from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Convert list to set for O(1) lookups
        word_set = set(wordList)
        
        # If the endWord is not in the dictionary, no valid path exists
        if endWord not in word_set:
            return 0
        
        # Initialize BFS queue with (current_word, sequence_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, level = queue.popleft()
            
            # If we reached the target word, return the current sequence length
            if word == endWord:
                return level
            
            # Generate all possible 1-letter variations of the current word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    # If the variation is a valid word in our set
                    if next_word in word_set:
                        # Remove to mark as visited
                        word_set.remove(next_word)
                        # Push to queue with incremented level
                        queue.append((next_word, level + 1))
                        
        return 0
