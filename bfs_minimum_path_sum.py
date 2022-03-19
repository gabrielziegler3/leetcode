import numpy as np

from collections import deque
from typing import *


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set()

        def bfs(x, y, grid, visited):
            queue = deque([(x, y)])

            while queue:
                x, y = queue.popleft()

                if (x, y) in visited:
                    continue

                if not self.in_bounds(x, y, grid):
                    continue

                visited.add((x, y))
                queue.append((x + 1, y))
                queue.append((x, y + 1))

                if x == 0 and y == 0:
                    continue
                elif x == 0 and y > 0:
                    grid[x][y] += grid[x][y - 1]
                elif y == 0 and x > 0:
                    grid[x][y] += grid[x - 1][y]
                else:
                    grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])

        bfs(0, 0, grid, visited)

        print(np.array(grid))
        return grid[-1][-1]

    def in_bounds(self, row, col, matrix) -> bool:
        return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0]))


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print("input:\n", np.array(grid))
res = Solution().minPathSum(grid)
print(res)
print("Expected:", 7)
