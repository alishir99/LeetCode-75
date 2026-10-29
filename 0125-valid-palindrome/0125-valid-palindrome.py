class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if 'A' <= c <= 'Z':
                clean += chr(ord(c)+32)
            elif 'a' <= c <= 'z' or "0" <= c <="9":
                clean +=c
        return clean == clean[::-1]