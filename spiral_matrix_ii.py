import numpy as np
import time

from collections import defaultdict, deque
from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        curr_dir = 0
        fill_values = deque(range(1, (n * n) + 1))

        visited = [[0] * n for _ in range(n)]
        res = [[0] * n for _ in range(n)]

        x = y = 0
        visited[x][y] = 1
        res[x][y] = fill_values.popleft()

        while fill_values:
            print(np.array(res))
            row_mov, col_mov = dirs[curr_dir]
            x += row_mov
            y += col_mov
            if not self.in_bounds(x, y, n, visited):
                x -= row_mov
                y -= col_mov
                curr_dir += 1
                if curr_dir == len(dirs):
                    curr_dir = 0
                row_mov, col_mov = dirs[curr_dir]
                x += row_mov
                y += col_mov
            visited[x][y] = 1
            res[x][y] = fill_values.popleft()
            time.sleep(0.08)
        return res

    def in_bounds(self, row, col, n, visited) -> bool:
        return (0 <= row < n) and (0 <= col < n) and visited[row][col] == 0


n = 1
res = Solution().generateMatrix(n)
print(np.array(res))
print("Expected:", np.array([[1]]))

time.sleep(2)

n = 3
res = Solution().generateMatrix(n)
print(np.array(res))
print("Expected:", np.array([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))

time.sleep(2)

n = 10
res = Solution().generateMatrix(n)
print(np.array(res))
print("Expected:", np.array([[1, 2, 3], [8, 9, 4], [7, 6, 5]]))
