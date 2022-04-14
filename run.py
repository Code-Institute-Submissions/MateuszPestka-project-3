# Tic Tac Toe game

board = [["-" for r in range(3)] for c in range(3)]

def print_board(board):
    """
    Makes the board for the game
    """
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print() # stops grid from lining up in a single line

print_board(board)