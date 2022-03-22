import numpy as np

from collections import deque
from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def bfs(pos, grid, visited):
            curr_island = set()
            queue = deque([pos])

            while queue:
                x, y = queue.popleft()
                visited.add((x, y))

                if grid[x][y] == "1":
                    curr_island.add((x, y))

                if self.inbounds(x + 1, y, grid, curr_island) and grid[x + 1][y] == "1":
                    queue.append((x + 1, y))
                if self.inbounds(x, y + 1, grid, curr_island) and grid[x][y + 1] == "1":
                    queue.append((x, y + 1))
                if self.inbounds(x - 1, y, grid, curr_island) and grid[x - 1][y] == "1":
                    queue.append((x - 1, y))
                if self.inbounds(x, y - 1, grid, curr_island) and grid[x][y - 1] == "1":
                    queue.append((x, y - 1))

            return curr_island

        def dfs(x, y, grid, visited):
            if not self.inbounds(x, y, grid, visited) or grid[x][y] == "0":
                return

            visited.add((x, y))

            dfs(x+1, y, grid, visited)
            dfs(x-1, y, grid, visited)
            dfs(x, y+1, grid, visited)
            dfs(x, y-1, grid, visited)

            return visited

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not (row, col) in visited:
                    # print("start BFS")
                    # island = bfs((row, col), grid[:], visited)
                    # print("end BFS")
                    island = dfs(row, col, grid, visited=visited)
                    visited = visited.union(island)
                    print(island)
                    count += 1

        return count

    def inbounds(self, x, y, grid, curr_island):
        return (
            0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in curr_island
        )


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
res = Solution().numIslands(grid)
print("Output:   ", res)
print("Expected: ", 1)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
res = Solution().numIslands(grid)
print("Output:   ", res)
print("Expected: ", 3)


grid = [
    ["1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1"],
]
res = Solution().numIslands(grid)
print("Output:   ", res)
print("Expected: ", 2)

# TLE case. BFS will timeout here, but DFS wont
grid = [
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
    ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
    ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
    ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]
]
res = Solution().numIslands(grid)
print("Output:   ", res)
print("Expected: ", 1)

