from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.inorder = deque([])
        self._inorder(root)

    def next(self) -> int:
        return self.inorder.popleft()

    def _inorder(self, root):
        if not root:
            return

        self._inorder(root.left)
        self.inorder.append(root.val)
        self._inorder(root.right)

    def hasNext(self) -> bool:
        return len(self.inorder) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
