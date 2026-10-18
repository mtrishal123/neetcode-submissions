class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in mapp.values():
                stack.append(char)
            elif char in mapp:
                if not stack or stack[-1] != mapp[char]:
                    return False
                stack.pop()
        return True
