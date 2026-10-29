class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        stack = []
        for c in clean:
            stack.append(c)
        rev = ""
        while stack:
            rev +=stack.pop()
        return clean == rev