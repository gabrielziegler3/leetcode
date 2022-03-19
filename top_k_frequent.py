import heapq
from collections import defaultdict
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        freq = {k: 0 for k in nums}

        # O(n)
        for idx, n in enumerate(nums):
            freq[n] += 1

        # O(n log(k))
        return heapq.nlargest(k, freq.keys(), key=freq.get)


# O (n log(k)) time and O (n + k) space

nums = [1, 1, 1, 2, 2, 3]
k = 2
res = Solution().topKFrequent(nums, k)
print(res)
print("Expected:", [1, 2])
