from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def dfs(root):
            if not root:
                return root

            dfs(root.right)
            self.total += root.val
            root.val = self.total
            dfs(root.left)

        dfs(root)

        return root
