from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k

        return self.dfs(root)

    def dfs(self, curr):
        stack = []

        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                self.k -= 1
                if self.k == 0:
                    return curr.val
                curr = curr.right
            else:
                break
