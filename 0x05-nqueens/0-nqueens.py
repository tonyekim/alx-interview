#!/usr/bin/python3
import sys

def print_solution(solution):
    """Prints the solution in the required format."""
    print("[", end="")
    for i in range(len(solution)):
        print("[{}, {}]".format(i, solution[i]), end="")
        if i != len(solution) - 1:
            print(", ", end="")
    print("]")

def is_valid(solution, col, left_diag, right_diag):
    """Checks if placing a queen at (len(solution), col) is valid."""
    n = len(solution)
    if col in solution or \
       left_diag[n - col] or \
       right_diag[n + col]:
        return False
    return True

def solve_nqueens(n, col, solution, left_diag, right_diag):
    """Solves the N Queens problem using recursive backtracking."""
    if col == n:
        print_solution(solution)
    else:
        for i in range(n):
            if is_valid(solution, i, left_diag, right_diag):
                solution.append(i)
                left_diag[n - i] = True
                right_diag[n + i] = True
                solve_nqueens(n, col + 1, solution, left_diag, right_diag)
                right_diag[n + i] = False
                left_diag[n - i] = False
                solution.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the backtracking variables
    solution = []
    left_diag = [False] * (2*n - 1)
    right_diag = [False] * (2*n - 1)

    # Solve the N Queens problem
    solve_nqueens(n, 0, solution, left_diag, right_diag)
