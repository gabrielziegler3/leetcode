import numpy as np
from collections import defaultdict
from typing import *


class Solution:
    # time complexity: O(m x n x 3^k), space complexity: O(k)
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not self.preliminar_checks(board, word):
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(row, col, word, board, visited=set()):
                    return True
        return False

    def preliminar_checks(self, board, word):
        board_set = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                board_set.add(board[row][col])
        return len(word) <= (len(board) * len(board[0])) and set(word).issubset(
            board_set
        )

    def backtrack(self, row, col, word, board, visited):
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        if not word:
            return True
        if (
            not self.in_bounds(row, col, board)
            or not board[row][col] == word[0]
            or (row, col) in visited
        ):
            return False

        visited.add((row, col))
        for d in dirs:
            row += d[0]
            col += d[1]
            if self.backtrack(row, col, word[1:], board, visited):
                return True
            row -= d[0]
            col -= d[1]
        visited.remove((row, col))
        return False

    def in_bounds(self, row, col, board):
        return 0 <= row < len(board) and 0 <= col < len(board[0])


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(f"Searching for {word} in:")
print(np.array(board))
res = Solution().exist(board, word)
print(res)
print("Expected:", True)
print()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(f"Searching for {word} in:")
print(np.array(board))
res = Solution().exist(board, word)
print(res)
print("Expected:", False)
print()

board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
print(f"Searching for {word} in:")
print(np.array(board))
res = Solution().exist(board, word)
print(res)
print("Expected:", True)
print()

board = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
]
word = "AAAAAAAAAAAABAA"
print(f"Searching for {word} in:")
print(np.array(board))
res = Solution().exist(board, word)
print(res)
print("Expected:", False)
print()

board = [["a"]]
word = "a"
print(f"Searching for {word} in:")
print(np.array(board))
res = Solution().exist(board, word)
print(res)
print("Expected:", False)
print()
