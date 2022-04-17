from collections import defaultdict
from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        def backtrack(start, comb):
            nonlocal res
            if comb in res:
                return

            res.append(comb[:])

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i+1, comb)
                comb.pop()

        backtrack(0, [])

        return res


nums = [1, 2, 2]
res = Solution().subsetsWithDup(nums)
print("Output:  ", res)
print("Expected:", [[],[1],[1,2],[1,2,2],[2],[2,2]])

nums = [4,4,4,1,4]
res = Solution().subsetsWithDup(nums)
print("Output:  ", res)
print("Expected:", [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])

