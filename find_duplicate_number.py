from collections import defaultdict
from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for i, n in enumerate(nums):
            if n in unique:
                return n
            else:
                unique.add(n)


nums = [1,3,4,2,2]
res = Solution().findDuplicate(nums)
print("Output:  ", res)
print("Expected:", 2)
print()

nums = [3,1,3,4,2]
res = Solution().findDuplicate(nums)
print("Output:  ", res)
print("Expected:", 3)
print()

nums = [1,1]
res = Solution().findDuplicate(nums)
print("Output:  ", res)
print("Expected:", 1)
print()

nums = [2,2,2,2,2]
res = Solution().findDuplicate(nums)
print("Output:  ", res)
print("Expected:", 2)
print()
