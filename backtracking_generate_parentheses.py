from collections import defaultdict
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(comb, left, right):
            if len(comb) == 2 * n:
                res.append(comb[:])
                return
            if left < n:
                comb += "("
                backtrack(comb, left + 1, right)
                comb = comb[:-1]
            if left > right:
                comb += ")"
                backtrack(comb, left, right + 1)
                comb = comb[:-1]

        backtrack("", 0, 0)

        return res


i = 3
res = Solution().generateParenthesis(i)
print(res)
