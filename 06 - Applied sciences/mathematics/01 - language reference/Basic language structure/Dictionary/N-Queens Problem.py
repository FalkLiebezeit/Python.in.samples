"""N-Queens Problem: Find and display all solutions for an N x N chessboard.

This script uses backtracking to place N queens on an N x N chessboard
so that no two queens threaten each other. Each solution is printed.
"""

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list of list): Current chessboard state.
        row (int): Row index.
        col (int): Column index.

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check left side of the current row
    for c in range(col):
        if board[row][c] == 'Q':
            return False

    # Check upper-left diagonal
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[r][c] == 'Q':
            return False

    # Check lower-left diagonal
    for r, c in zip(range(row+1, len(board)), range(col-1, -1, -1)):
        if board[r][c] == 'Q':
            return False

    return True

def print_board(board):
    """Print the chessboard in a readable format."""
    for row in board:
        print("   ".join(row))
    print()

def solve_n_queens(board, col, solutions):
    """
    Recursively try to place queens column by column.

    Args:
        board (list of list): Current chessboard state.
        col (int): Current column to place a queen.
        solutions (list): List to store all valid solutions.
    """
    N = len(board)
    if col >= N:
        # Found a valid solution, make a deep copy and store it
        solutions.append([row[:] for row in board])
        print(f"\nBoard {len(solutions)}:")
        print("----" * N)
        print_board(board)
        print("====" * N)
        return

    for row in range(N):
        board[row][col] = 'Q'
        if is_safe(board, row, col):
            solve_n_queens(board, col + 1, solutions)
        board[row][col] = '.'  # Backtrack

def main():
    """Main function to run the N-Queens solver."""
    N = int(input("Enter chessboard size: "))
    board = [['.'] * N for _ in range(N)]
    solutions = []
    solve_n_queens(board, 0, solutions)
    print(f"\nTotal solutions found: {len(solutions)}")

if __name__ == "__main__":
    main()