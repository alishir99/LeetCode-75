class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        first = {}
        for c in s:
            first[c] = first.get(c, 0)+1
        for c in t:
            if c not in first:
                first[c] = first.get(c, 0)+1
            else:
                first[c] -=1
        for v in first.values():
            if v!=0:
                return False 
        return True
