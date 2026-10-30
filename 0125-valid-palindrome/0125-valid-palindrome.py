class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(c.lower() for c in s if c.isalnum())
        start = 0 
        end = len(clean)-1
        while start < end:
            if clean[start] is not clean[end]:
                return False 
            start +=1
            end -=1
        return True 