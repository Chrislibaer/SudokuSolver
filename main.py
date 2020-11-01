import numpy as np
import pandas as pd


class Board():
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path, header=None).to_numpy()

    def print_board(self):
        print(self.data)

    def check_correct(self):
        # rows
        for i in range(9):
            duplicates = self.check_duplicates(self.data[i, :])
            if duplicates:
                return False
        # cols
        for i in range(9):
            duplicates = self.check_duplicates(self.data[:, i])
            if duplicates:
                return False
        # boxes
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                duplicates = self.check_duplicates(self.data[i:i+3, j:j+3])
                if duplicates:
                    return False
        return True

    def check_duplicates(self, row):
        return not (len(np.unique(row)) - 1 >= np.count_nonzero(row) or len(np.unique(row)) == 9)


class Solver():
    def __init__(self, board):
        self.board = board

    def find_zero(self):
        for i in range(9):
            for j in range(9):
                if self.board.data[i, j] == 0:
                    return i, j
        return None

    def solve(self):
        pos = self.find_zero()
        if not pos:
            return True
        else:
            i, j = pos

        for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            self.board.data[i, j] = n
            if not self.board.check_correct():
                self.board.data[i, j] = 0
            else:
                if self.solve():
                    return True

                self.board.data[i, j] = 0

        return False


def main():
    board = Board("board.csv")
    board.print_board()

    solver = Solver(board)
    solver.solve()
    solver.board.print_board()
    pd.DataFrame(solver.board.data).to_csv("solution.csv", header=False, index=False)


if __name__ == '__main__':
    main()
