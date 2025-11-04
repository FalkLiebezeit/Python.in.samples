# Global counter for the number of solutions found
queenscnt = 0

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    Only checks the left side (since we place queens column by column).
    """
    n = len(board)
    # Check left side of the current row
    for c in range(col):
        if board[row][c] == 'Q':
            return False

    # Check upper-left diagonal
    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[r][c] == 'Q':
            return False

    # Check lower-left diagonal
    for r, c in zip(range(row+1, n), range(col-1, -1, -1)):
        if board[r][c] == 'Q':
            return False

    return True

def print_board(board):
    """
    Print the chessboard in a readable format.
    """
    for row in board:
        print("   ".join(row))
    print()

def solve_n_queens(board, col):
    """
    Recursive function to solve the N-Queens problem.
    """
    global queenscnt
    n = len(board)

    # If all queens are placed, print the solution
    if col >= n:
        queenscnt += 1
        print(f"\nBoard {queenscnt}:")
        print("----" * n)
        print_board(board)
        print("====" * n)
        return

    # Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Place queen
            solve_n_queens(board, col + 1)  # Recurse for next column
            board[row][col] = '.'  # Backtrack

# Main driver code
def main():
    try:
        N = int(input("Enter chessboard size: "))
        if N <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Initialize the chessboard with '.'
    board = [['.'] * N for _ in range(N)]

    # Start solving from the first column
    solve_n_queens(board, 0)

    print(f"\nTotal solutions: {queenscnt}")

if __name__ == "__main__":
    main()