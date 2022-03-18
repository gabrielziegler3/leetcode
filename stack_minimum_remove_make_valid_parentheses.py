from collections import defaultdict
from typing import *


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx_to_remove = set()
        stack = []
        res = ""

        for idx, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(idx)
            else:
                if stack:
                    stack.pop()
                else:
                    idx_to_remove.add(idx)

        idx_to_remove = set(stack).union(idx_to_remove)

        for idx, c in enumerate(s):
            # O(1)
            if idx in idx_to_remove:
                continue
            else:
                res += c

        return res


s = "lee(t(c)o)de)"
res = Solution().minRemoveToMakeValid(s)
print(res)


s = "))(("
res = Solution().minRemoveToMakeValid(s)
print(res)
