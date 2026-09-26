class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge array to a hash map for O(1) lookups
        mapping = {k: v for k, v in knowledge}
        
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Find the closing bracket
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                
                # Extract the key between '(' and ')'
                key = s[i+1:j]
                
                # Append the mapped value or '?' if the key is unknown
                result.append(mapping.get(key, '?'))
                
                # Move the pointer past the closing bracket
                i = j + 1
            else:
                result.append(s[i])
                i += 1
                
        return "".join(result)