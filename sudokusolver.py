'''

Backtracking is a common algorithm used to solve Sudoku puzzles. The basic idea is to start with an empty cell in the puzzle, 
try different numbers, and backtrack if a number does not fit. Here is an implementation of a 
backtracking algorithm to solve a Sudoku puzzle in Python:
'''

# Define a function to check if a given number can be placed in a cell
def can_place(board, row, col, num):
    # Check row and column for duplicates
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Check 3x3 square for duplicates
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
    # Return True if no duplicates found
    return True

# Define a function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try different numbers for empty cell
                for num in range(1, 10):
                    if can_place(board, row, col, num):
                        board[row][col] = num
                        # Recursively solve remaining puzzle
                        if solve_sudoku(board):
                            return True
                        # Backtrack if number does not fit
                        board[row][col] = 0
                # Return False if no number fits
                return False
    # Return True if all cells filled
    return True

# Define a sample Sudoku puzzle
board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]

# Solve the Sudoku puzzle using backtracking
if solve_sudoku(board):
    # Print the solution
    for row in board:
        print(row)
else:
    print("No solution exists.")
