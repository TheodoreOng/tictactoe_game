# Tic-Tac-Toe Game

def initialize_board():
    return [" " for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_draw(board):
    return " " not in board

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("Spot already taken.")
        except (IndexError, ValueError):
            print("Invalid move. Please enter a number between 1 and 9.")

def tic_tac_toe():
    board = initialize_board()
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
