class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {c: s.count(c) for c in set(s)}
        y = {c: t.count(c) for c in set(t)}
        return x == y
