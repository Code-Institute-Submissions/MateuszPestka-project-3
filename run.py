# Tic Tac Toe game

board = [["-" for r in range(3)] for c in range(3)]


def print_board(board):
    """
    Makes the board for the game
    """
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()  # stops grid from lining up in a single line


print_board(board)


def quit_game(user_choice):
    """
    Allow user to quit the game early when they want to
    stop playing the game
    """
    return True if user_choice.lower() == "q" else False


def validate_input():
    pass


def coordinates():
    pass


def show_on_board():
    pass


def player():
    pass


def win():
    pass


def check_row():
    pass


def check_column():
    pass


def check_diagonal():
    pass


while True:
    user_choice = input("Enter a position between 1-9 or press 'q' to quit:")
    if quit_game(user_choice):
        print("Thanks for playing")
        break