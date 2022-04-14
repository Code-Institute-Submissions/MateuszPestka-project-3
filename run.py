# Tic Tac Toe game

board = [["-" for r in range(3)] for c in range(3)]

def print_board(board):
    for row in board:
        for slot in board:
            print(slot)

print_board(board)