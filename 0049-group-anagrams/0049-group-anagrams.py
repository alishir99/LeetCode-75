class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))
            group[key].append(w)
        return list(group.values())
    