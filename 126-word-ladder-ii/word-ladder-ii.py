from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
            
        # Phase 1: BFS to find the shortest distance to each word
        # and store valid parent connections
        distance = {beginWord: 0}
        parent_map = defaultdict(list)
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            # Process level by level to track level distances properly
            level_visited = set()
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                curr_dist = distance[curr_word]
                
                # Try changing every character of the current word
                for i in range(len(curr_word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == curr_word[i]:
                            continue
                        
                        next_word = curr_word[:i] + c + curr_word[i+1:]
                        
                        if next_word in wordSet:
                            # If it's a shorter or equal path to next_word
                            if next_word not in distance or distance[next_word] == curr_dist + 1:
                                if next_word not in distance:
                                    distance[next_word] = curr_dist + 1
                                    queue.append(next_word)
                                    
                                parent_map[next_word].append(curr_word)
                                level_visited.add(next_word)
                                
                                if next_word == endWord:
                                    found = True
                                    
            # Remove visited words from the available word set to prevent cycles
            wordSet -= level_visited

        if not found:
            return []
            
        # Phase 2: Backtracking (DFS) from endWord to beginWord
        result = []
        
        def backtrack(word: str, path: list[str]):
            if word == beginWord:
                result.append(path[::-1]) # Reverse to get beginWord -> endWord order
                return
            
            for parent in parent_map[word]:
                path.append(parent)
                backtrack(parent, path)
                path.pop() # Backtrack step
                
        backtrack(endWord, [endWord])
        return result
