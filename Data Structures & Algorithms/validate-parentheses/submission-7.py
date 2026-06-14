class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapper = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in mapper:
                if stk and stk[-1] == mapper[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False