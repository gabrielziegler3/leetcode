from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        self.paths = []

        def dfs(idx, curr_path):
            curr_path.append(idx)
            if target == idx:
                self.paths.append(curr_path[:])
                return
            for i in graph[idx]:
                dfs(i, curr_path[:])

        dfs(0, [])
        return self.paths

