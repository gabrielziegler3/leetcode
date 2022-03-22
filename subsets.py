from collections import defaultdict
from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, comb):
            nonlocal res

            res.append(comb.copy())

            if len(comb) == len(nums):
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(0, [])

        return res


nums = [1, 2, 3]
res = Solution().subsets(nums)
print("Output:  ", res)
print("Expected:", [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#
#         def backtrack(start, comb, size):
#             nonlocal res
#
#             if len(comb) == size:
#                 res.append(comb.copy())
#                 return
#
#             for i in range(start, len(nums)):
#                 comb.append(nums[i])
#                 backtrack(i+1, comb, size)
#                 comb.pop()
#
#         for i in range(len(nums) + 1):
#             backtrack(0, [], size=i)
#
#         return res
