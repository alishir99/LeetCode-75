class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}
        out = []
        for w in strs:
            key = ''.join(sorted(w))
            if key not in group:
                group[key] = []
            group[key].append(w)
        for k,v in group.items():
            out.append(v)

        return out
    