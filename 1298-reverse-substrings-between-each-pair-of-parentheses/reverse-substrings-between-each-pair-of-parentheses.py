class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                curr_chars = []
                while stack and stack[-1] != '(':
                    curr_chars.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                for c in curr_chars:
                    stack.append(c)
            else:
                stack.append(char)
        return "".join(stack)