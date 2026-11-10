class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0)+1
        freq = sorted(freq.items(), key=lambda kv:kv[1], reverse=True)[:k]
        return [k for k, v in freq]