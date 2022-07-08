class Solution:
    def __init__(self):
        self.memoization = {}

    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        if n in self.memoization:
            return self.memoization[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memoization[n] = res
        return res

# from functools import cache
# 
# class Solution:
#     @cache
#     def climbStairs(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return 1
#         return self.climbStairs(n-1) + self.climbStairs(n-2)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         self.possibilities = 0
# 
#         self._backtracking(n)
# 
#         return self.possibilities
# 
#     def _backtracking(self, remaining):
#         if remaining == 0:
#             self.possibilities += 1
#             return
# 
#         if remaining < 0:
#             return
# 
#         moves = (1, 2)
#         for move in moves:
#             remaining -= move
#             self._backtracking(remaining)
#             remaining += move




for n in range(10):
    res = Solution().climbStairs(n)
    print(res)

n = 50
res = Solution().climbStairs(n)
print(res)
