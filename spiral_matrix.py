import numpy as np
import time

from collections import defaultdict
from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        curr_dir = 0
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        res = []
        x = y = 0
        res.append(matrix[x][y])
        visited[x][y] = 1

        while len(res) < len(visited) * len(visited[0]):
            print(np.array(visited))
            row_mov, col_mov = dirs[curr_dir]
            x += row_mov
            y += col_mov
            if not self.in_bounds(x, y, matrix, visited):
                x -= row_mov
                y -= col_mov
                curr_dir += 1
                if curr_dir == len(dirs):
                    curr_dir = 0
                row_mov, col_mov = dirs[curr_dir]
                x += row_mov
                y += col_mov
            visited[x][y] = 1
            res.append(matrix[x][y])
            time.sleep(.5)
        return res

    def in_bounds(self, row, col, matrix, visited) -> bool:
        return (0 <= row < len(matrix)) and (0 <= col < len(matrix[0])) and visited[row][col] == 0


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
res = Solution().spiralOrder(matrix)
print(res)
print("Expected:", [1,2,3,6,9,8,7,4,5])

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res = Solution().spiralOrder(matrix)
print(res)
print("Expected:", [1,2,3,4,8,12,11,10,9,5,6,7])

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    #     curr_dir = 0
    #     visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    #     res = []
    #     x = y = 0
    #     res.append(matrix[x][y])
    #     visited[x][y] = 1

    #     while len(res) < len(visited) * len(visited[0]):
    #         print(np.array(visited))
    #         row_mov, col_mov = dirs[curr_dir]
    #         x += row_mov
    #         y += col_mov
    #         if not self.in_bounds(x, y, matrix, visited):
    #             x -= row_mov
    #             y -= col_mov
    #             curr_dir += 1
    #             if curr_dir == len(dirs):
    #                 curr_dir = 0
    #         else:
    #             visited[x][y] = 1
    #             res.append(matrix[x][y])
    #         time.sleep(1)
    #     return res
