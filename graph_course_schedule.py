from collections import defaultdict
from pprint import pprint
import numpy as np
from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {node: [] for node in range(numCourses)}

        for course, prereq in prerequisites:
            nodes[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            # no prereqs
            if not nodes[course]:
                return True

            visited.add(course)
            for req in nodes[course]:
                if not dfs(req):
                    return False
            nodes[course] = []
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


numCourses = 2
prerequisites = [[1, 0]]
res = Solution().canFinish(numCourses, prerequisites)
print(res)
print()

numCourses = 3
prerequisites = [[0, 1], [1, 2]]
res = Solution().canFinish(numCourses, prerequisites)
print(res)
print()

numCourses = 2
prerequisites = prerequisites = [[1, 0], [0, 1]]
res = Solution().canFinish(numCourses, prerequisites)
print(res)
print()
