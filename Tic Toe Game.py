# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Initialize the Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Main game loop
while True:
    display_board(board)
    print(f"Player {current_player}'s turn")

    # Get player input
    try:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
    except ValueError:
        print("Invalid input! Please enter numbers between 0 and 2.")
        continue

    # Check if the move is valid
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Invalid move! Row and column must be between 0 and 2.")
        continue
    if board[row][col] != " ":
        print("Invalid move! Cell already occupied.")
        continue

    # Make the move
    board[row][col] = current_player

    # Check for a winner
    if check_winner(board, current_player):
        display_board(board)
        print(f"Player {current_player} wins!")
        break

    # Check for a tie
    if is_board_full(board):
        display_board(board)
        print("It's a tie!")
        break

    # Switch players
    current_player = "O" if current_player == "X" else "X"
