class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c
        
        return new_str == new_str[::-1]