import numpy as np

from collections import Counter
from typing import *


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # O(n), O(1)
        most_common_top = Counter(tops).most_common(1)[0]
        most_common_bottom = Counter(bottoms).most_common(1)[0]
        res = 0

        if not (most_common_top[1] + most_common_bottom[1]) >= len(tops):
            return -1

        if most_common_top[1] < most_common_bottom[1]:
            tops, bottoms = bottoms, tops
            most_common_bottom, most_common_top = most_common_top, most_common_bottom

        for idx, val in enumerate(tops):
            if val != most_common_top[0]:
                if bottoms[idx] == most_common_top[0]:
                    res += 1
                else:
                    return -1
        return res


tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
res = Solution().minDominoRotations(tops, bottoms)
print(res)
print("Expected:", 2)

tops = [3, 5, 1, 2, 3]
bottoms = [3, 6, 3, 3, 4]
res = Solution().minDominoRotations(tops, bottoms)
print(res)
print("Expected:", -1)

tops = [1, 2, 1, 1, 1, 2, 2, 2]
bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
res = Solution().minDominoRotations(tops, bottoms)
print(res)
print("Expected:", 1)

tops = [1, 4, 1, 3, 1, 2, 2, 5]
bottoms = [2, 2, 2, 2, 2, 2, 2, 2]
res = Solution().minDominoRotations(tops, bottoms)
print(res)
print("Expected:", 0)
