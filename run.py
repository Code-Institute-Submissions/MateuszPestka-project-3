# Tic Tac Toe game

board = [["-" for r in range(3)] for c in range(3)]

def print_board(board):
    """
    Makes the board for the game
    """
    for row in board:
        for slot in board:
            print(f"{slot}", end="")
        print()

print_board(board)