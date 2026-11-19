class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alnum(c):
            return 'a'<=c <='z' or 'A' <= c <='Z' or '0' <= c <= '9'
        def to_lower(c):
            if 'A' <= c <= 'Z':
                return chr(ord(c)+32)
            return c
        clean = ''.join(to_lower(c) for c in s if alnum(c))
        return clean==clean[::-1] 