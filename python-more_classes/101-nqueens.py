#!/usr/bin/env python3
import sys


class Chess:
    def __init__(self, size=4):
        # Trigger setter validations
        self.size = size
        self.chessboard = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.solutions = []

    # --- GETTERS & SETTERS ---

    @property
    def size(self):
        """Getter for size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 4:
            raise ValueError("size must be at least 4")
        self._size = value

    @property
    def chessboard(self):
        """Getter for the chessboard matrix."""
        return self._chessboard

    @chessboard.setter
    def chessboard(self, value):
        """Setter for the chessboard with type validation."""
        if not isinstance(value, list):
            raise TypeError("chessboard must be a list")
        self._chessboard = value

    @property
    def solutions(self):
        """Getter for stored solutions."""
        return self._solutions

    @solutions.setter
    def solutions(self, value):
        """Setter for solutions with type validation."""
        if not isinstance(value, list):
            raise TypeError("solutions must be a list")
        self._solutions = value

    # --- SOLVER METHODS ---

    def is_safe(self, row, col):
        """
        Checks if placing a queen at (row, col) is safe from other queens above it.
        """
        # 1. Check vertical column going up
        for i in range(row):
            if self.chessboard[i][col] == 1:
                return False

        # 2. Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.chessboard[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # 3. Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < self.size:
            if self.chessboard[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def get_queen_positions(self):
        """
        Extracts the (row, col) coordinates of all queens currently on the board.
        """
        positions = []
        for r in range(self.size):
            for c in range(self.size):
                if self.chessboard[r][c] == 1:
                    positions.append([r, c])
        return positions

    def _solve_recursive(self, row):
        """
        Core backtracking solver.
        """
        # Base case: All rows populated with a queen
        if row == self.size:
            self.solutions.append(self.get_queen_positions())
            return

        # Try placing a queen in each column of the current row
        for col in range(self.size):
            if self.is_safe(row, col):
                # Place queen
                self.chessboard[row][col] = 1

                # Recurse to next row
                self._solve_recursive(row + 1)

                # Backtrack (remove queen)
                self.chessboard[row][col] = 0

    def solve(self):
        """
        Resets previous results and starts the resolution process.
        """
        self.solutions = []
        self._solve_recursive(0)
        return self.solutions


def print_board(solution, size):
    """
    Displays a visual representation of the chessboard solution.
    """
    for r in range(size):
        row_str = ""
        for c in range(size):
            if [r, c] in solution:
                row_str += " Q "
            else:
                row_str += " . "
        print(row_str)
    print("-" * (size * 3))


# --- EXECUTION ---
if __name__ == "__main__":
    # 1. Vérification du nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # 2. Conversion de l'argument en entier
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # 3. Instanciation (déclenche la validation du setter @size.setter)
    try:
        game = Chess(N)
    except ValueError as e:
        print(e)
        sys.exit(1)

    # 4. Résolution et affichage
    print(f"=== Solving the {N}-Queens Problem ===\n")

    results = game.solve()

    print(f"Total solutions found for N={N}: {len(results)}\n")

    for idx, solution in enumerate(results, 1):
        print(f"--- Solution #{idx} ---")
        print(f"Positions (row, col): {solution}")
        print_board(solution, N)