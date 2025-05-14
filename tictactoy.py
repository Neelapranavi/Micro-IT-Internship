def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_symbol = "X"
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_symbol}, enter row (0-2): "))
        col = int(input(f"Player {current_symbol}, enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = current_symbol
            if check_winner(board, current_symbol):
                print_board(board)
                print(f"Player {current_symbol} wins!")
                return
            current_symbol = "O" if current_symbol == "X" else "X"
        else:
            print("Cell already taken. Try again.")
    print_board(board)
    print("It's a draw!")

tic_tac_toe()
