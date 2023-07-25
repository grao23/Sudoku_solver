def solve_sudoku(board):
    if not find_empty_location(board):
        return True
    
    row, col = find_empty_location(board)
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False


def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid_move(board, row, col, num):
    return (
        is_valid_in_row(board, row, num) and
        is_valid_in_column(board, col, num) and
        is_valid_in_box(board, row - row % 3, col - col % 3, num)
    )


def is_valid_in_row(board, row, num):
    for col in range(9):
        if board[row][col] == num:
            return False
    return True


def is_valid_in_column(board, col, num):
    for row in range(9):
        if board[row][col] == num:
            return False
    return True


def is_valid_in_box(board, start_row, start_col, num):
    for row in range(3):
        for col in range(3):
            if board[row + start_row][col + start_col] == num:
                return False
    return True


def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=' ')
        print()


# Example board to solve
board = [
    [0, 0, 6, 0, 5, 7, 8, 2, 0],
    [2, 1, 0, 0, 0, 6, 7, 5, 0],
    [7, 5, 3, 0, 0, 4, 0, 0, 9],
    [0, 6, 0, 0, 0, 5, 3, 0, 0],
    [0, 0, 0, 7, 0, 0, 4, 0, 2],
    [3, 0, 0, 9, 2, 8, 0, 0, 6],
    [0, 2, 0, 5, 4, 0, 0, 0, 1],
    [0, 0, 1, 0, 7, 0, 9, 4, 8],
    [0, 0, 9, 0, 0, 1, 0, 7, 0]
]

if solve_sudoku(board):
    print("Sudoku Solved:")
    print_board(board)
else:
    print("No solution exists.")