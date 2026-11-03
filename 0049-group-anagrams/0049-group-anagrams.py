class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        for w in strs:
            key = ''.join(sorted(w))
            if key not in group:
                group[key] = []
            group[key].append(w)
        return list(group.values())