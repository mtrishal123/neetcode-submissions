class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if c == ')' and stk[-1] == '(' and stk:
                    stk.pop()
                elif c == ']' and stk[-1] == '[' and stk:
                    stk.pop()
                elif c == '}' and stk[-1] == '{' and stk:
                    stk.pop()
        return len(stk) == 0