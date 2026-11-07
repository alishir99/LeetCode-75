class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = defaultdict(list)
        for w in strs:
            cout = [0]*26
            for c in w:
                cout[ord(c)-ord('a')] +=1

            key = tuple(cout)
            group[key].append(w)
        return list(group.values())
    