from collections import defaultdict
from typing import *


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        anchor = 0
        j = 0
        res = []

        # O(n), O(n)
        indices = {val: idx for idx, val in enumerate(s)}

        for i, c in enumerate(s):
            j = max(indices[c], j)

            if i == j:
                res.append(j - anchor + 1)
                anchor = j + 1

        return res


s = "ababcbacadefegdehijhklij"
res = Solution().partitionLabels(s)
print("Output:  ", res)
print("Expected:", [9, 7, 8])


s = "eccbbbbdec"
res = Solution().partitionLabels(s)
print("Output:  ", res)
print("Expected:", [10])
