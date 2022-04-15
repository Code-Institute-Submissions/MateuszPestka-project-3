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


def validate_input(user_choice):
    """
    Checks if users choice is valid,
    user choice can only be a number between 1-9
    """
    try:
        if not user_choice.isnumeric():
            raise ValueError("You have entered a letter")

        if int(user_choice) > 9 or int(user_choice) < 1:
            raise ValueError("Your number is too high")
    except ValueError as e:
        print(f"Invalid input!! {e}.\n Please input a number between 1-9.")
        return False


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
    validate_input(user_choice)