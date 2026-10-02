class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current):
            # If the current string has reached the maximum length of 2 * n, add it to results
            if len(current) == 2 * n:
                res.append("".join(current))
                return
            
            # We can add an opening bracket if we haven't used all n opening brackets
            if open_count < n:
                current.append('(')
                backtrack(open_count + 1, close_count, current)
                current.pop()
                
            # We can add a closing bracket if there are more opening brackets than closing brackets
            if close_count < open_count:
                current.append(')')
                backtrack(open_count, close_count + 1, current)
                current.pop()
                
        backtrack(0, 0, [])
        return res