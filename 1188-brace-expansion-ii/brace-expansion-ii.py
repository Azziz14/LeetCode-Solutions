class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr):
            stack = [[]]
            op = '+'
            i = 0
            while i < len(expr):
                if expr[i].isalpha():
                    word = expr[i]
                    i += 1
                    while i < len(expr) and expr[i].isalpha():
                        word += expr[i]
                        i += 1
                    self.add_item(stack, op, [word])
                elif expr[i] == '{':
                    j, bal = i, 0
                    while j < len(expr):
                        if expr[j] == '{':
                            bal += 1
                        elif expr[j] == '}':
                            bal -= 1
                        if bal == 0:
                            break
                        j += 1
                    sub = parse(expr[i+1:j])
                    self.add_item(stack, op, sub)
                    i = j + 1
                elif expr[i] == ',':
                    op = '+'
                    i += 1
                elif expr[i] == '*':
                    op = '*'
                    i += 1
            
            res = set()
            for group in stack:
                res.update(group)
            return sorted(list(res))

        # Handle implicit multiplication by inserting '*'
        exp = []
        for i, c in enumerate(expression):
            if i > 0 and (expression[i-1].isalpha() or expression[i-1] == '}') and (c.isalpha() or c == '{'):
                exp.append('*')
            exp.append(c)
        
        return parse("".join(exp))

    def add_item(self, stack, op, words):
        if op == '+':
            stack.append(words)
        else:
            prev = stack.pop()
            stack.append([a + b for a in prev for b in words])