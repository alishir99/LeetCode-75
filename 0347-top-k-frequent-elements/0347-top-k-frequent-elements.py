class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] +=1
        out = [[] for _ in range(len(nums)+1)]
        for num, count in map.items():
            out[count].append(num)
        res = []
        for i in range(len(out)-1, -1, -1):
            for num in out[i]:
                res.append(num)
                if len(res)==k:
                    return res