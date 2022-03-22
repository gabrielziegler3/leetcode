import numpy as np


class Solution:
    def totalNQueens(self, n: int) -> int:
        visited_cols = set()
        visited_pos_diag = set()
        visited_neg_diag = set()

        self.n_solutions = 0
        self.backtrack(
            n,
            row=0,
            n_queens=0,
            visited_cols=visited_cols,
            visited_pos_diag=visited_pos_diag,
            visited_neg_diag=visited_neg_diag,
        )

        return self.n_solutions

    def backtrack(
        self, n, row, n_queens, visited_cols, visited_pos_diag, visited_neg_diag
    ):
        if row == n:
            pass
        # print(f"Trying to put {n_queens} at {row}")
        if n_queens == n:
            self.n_solutions += 1

        for col in range(n):
            neg_diag = row - col
            pos_diag = row + col

            if (
                col in visited_cols
                or neg_diag in visited_neg_diag
                or pos_diag in visited_pos_diag
            ):
                continue

            n_queens += 1
            visited_neg_diag.add(neg_diag)
            visited_pos_diag.add(pos_diag)
            visited_cols.add(col)
            self.backtrack(
                n, row + 1, n_queens, visited_cols, visited_pos_diag, visited_neg_diag
            )
            n_queens -= 1
            visited_neg_diag.remove(neg_diag)
            visited_pos_diag.remove(pos_diag)
            visited_cols.remove(col)

        return n_queens

    # Neg diag
    # row - col
    # 0 -1 -2 -3
    # 1  0 -1 -2
    # 2  1  0 -1
    # 3  2  1  0

    # Pos diag
    # row + col
    # 0  1  2  3
    # 1  2  3  4
    # 2  3  4  5
    # 3  4  5  6


n = 4
print(np.array(n))
res = Solution().totalNQueens(n)
print(res)
print("Expected:", 2)
print()

n = 5
print(np.array(n))
res = Solution().totalNQueens(n)
print(res)
print("Expected:", 10)
print()

n = 1
print(np.array(n))
res = Solution().totalNQueens(n)
print(res)
print("Expected:", 1)
print()
#
n = 8
print(np.array(n))
res = Solution().totalNQueens(n)
print(res)
print("Expected:", 92)
print()

n = 12
print(np.array(n))
res = Solution().totalNQueens(n)
print(res)
print("Expected:", 14200)
print()
