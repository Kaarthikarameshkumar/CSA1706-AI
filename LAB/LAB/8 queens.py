# Python program to solve the 8-Queen problem using Backtracking

N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve(board, col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Main program
board = [[0 for _ in range(N)] for _ in range(N)]

if solve(board, 0):
    print("One solution to the 8-Queen problem:")
    print_board(board)
else:
    print("No solution exists.")
