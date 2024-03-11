#!/usr/bin/python3
""" N Queens Problem Solver

This script solves the N Queens problem, which involves
placing N non-attacking queens on an N×N chessboard.
"""
import sys


def solve_queens_problem(board_size):
    """Solve the N Queens problem and return a list of solutions.

    Args:
        board_size (int): The size of the chessboard.

    Returns:
        list: List of solutions, where each solution is a list of
        queen positions."""

    def is_valid_position(pos, occupied_pos):
        """Check if placing a queen at a given position is valid.

        Args:
            pos (int): The column position to check.
            occupied_pos (list): List of previously placed queen positions.

        Returns:
            bool: True if the position is valid, False otherwise."""
        for i in range(len(occupied_pos)):
            if (
                occupied_pos[i] == pos or
                occupied_pos[i] - i == pos - len(occupied_pos) or
                occupied_pos[i] + i == pos + len(occupied_pos)
            ):
                return False
        return True

    def place_queens(board_size, index, occupied_pos, solutions):
        """Recursively explore and place queens on the chessboard.

        Args:
            board_size (int): The size of the chessboard.
            index (int): Current row being considered.
            occupied_pos (list): List of queen positions for each row.
            solutions (list): List to store valid solutions."""
        if index == board_size:
            solutions.append(occupied_pos[:])
            return

        for i in range(board_size):
            if is_valid_position(i, occupied_pos):
                occupied_pos.append(i)
                place_queens(board_size, index + 1, occupied_pos, solutions)
                occupied_pos.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """Main function to handle command-line arguments and display solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    main()
