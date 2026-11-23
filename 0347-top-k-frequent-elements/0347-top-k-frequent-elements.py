class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {n: nums.count(n) for n in set(nums)}
        return sorted(freq, key=freq.get, reverse=True)[:k]