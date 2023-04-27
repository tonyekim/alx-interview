#!/usr/bin/python3
'''Program that solves the N Queens problem'''
import sys


def is_valid(board, rank, file, n):
    '''
    Checks the validity of placing a queen at a given position on the board
    Args:
        board (list): List of n rank(rows) and n file(columns)
        rank (int): Current row being evaluated
        file (int): Current column being evaluated
        n (list): The board size
    Returns (boolean):
        True if valid to place a queen on the board, otherwise False
    '''
    # Checks if there are no Queens in the same file(column)
    for x in range(rank):
        if board[x][file]:
            return False
    # Checks if there are no Queens in the same diagonal
    for x, y in zip(range(rank, -1, -1), range(file, -1, -1)):
        if board[x][y]:
            return False
    # Checks if there are no Queens in the same anti-diagonal
    for x, y in zip(range(rank, -1, -1), range(file, n)):
        if board[x][y]:
            return False
    return True


def nqueens_generator(board, rank, n, outcome):
    '''
    Helps to generate all valid solutions to the N Queens problem
    Args:
        board (list): List of n rank(rows) and n file(columns)
        rank (int): Current row being evaluated
        n (int): The board size
        outcome (list): List to store solutions as arguments
    '''
    # Append a copy of the board to the outcome list if we have
    # placed all Queens in all ranks(rows) of the board
    if rank == n:
        outcome.append(board[:])  # make a copy of the board
        return
    # Try to place a Queen in each file(column) of the current rank(row)
    for file in range(n):
        if is_valid(board, rank, file, n):
            board[rank][file] = 1
            nqueens_generator(board, rank + 1, n, outcome)
            board[rank][file] = 0


def nqueens_solution(n):
    '''
    Generates the actual solution to the N Queen problem
    Args:
        n (int): The board size
    Returns:
        List of solutions found
    '''
    # Checks if n is an integer
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    # Checks if n is less than 4
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * n for x in range(n)]
    outcome = []
    nqueens_generator(board, 0, n, outcome)
    for solution in outcome:
        print(solution)


if __name__ == "__main__":
    # Checks if the user called the program with the wrong num of args
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens_solution(n)