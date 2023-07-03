#!/usr/bin/python3
import sys


class Nqueens:

    def __init__(self, n):
        self.board = []
        [self.board.append([]) for i in range(n)]
        [row.append(' ') for i in range(n) for row in self.board]

    def board_deepcopy(self, b):
        if isinstance(b, list):
            return list(map(self.board_deepcopy, b))
        return (b)

    def get_solution(self, board):
        solution = []
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == "Q":
                    solution.append([r, c])
                    break
        return (solution)

    def xout(self, board, row, col):
        for c in range(col + 1, len(board)):
            board[row][c] = "x"
        for c in range(col - 1, -1, -1):
            board[row][c] = "x"
        for r in range(row + 1, len(board)):
            board[r][col] = "x"
        for r in range(row - 1, -1, -1):
            board[r][col] = "x"
        c = col + 1
        for r in range(row + 1, len(board)):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row - 1, -1, -1):
            if c < 0:
                break
            board[r][c]
            c -= 1
        c = col + 1
        for r in range(row - 1, -1, -1):
            if c >= len(board):
                break
            board[r][c] = "x"
            c += 1
        c = col - 1
        for r in range(row + 1, len(board)):
            if c < 0:
                break
            board[r][c] = "x"
            c -= 1

    def recursive_solve(self, board, row, queens, solutions):
        if queens == len(board):
            solutions.append(self.get_solution(board))
            return (solutions)

        for c in range(len(board)):
            if board[row][c] == " ":
                tmp_board = self.board_deepcopy(board)
                tmp_board[row][c] = "Q"
                self.xout(tmp_board, row, c)
                solutions = self.recursive_solve(tmp_board, row + 1,
                                                 queens + 1, solutions)

        return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = Nqueens(int(sys.argv[1]))
    solutions = board.recursive_solve(board.board, 0, 0, [])
    for sol in solutions:
        print(sol)
