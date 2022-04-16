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
        if not user_choice.isnumeric():  # Checks if user input a number
            raise ValueError("You have entered a letter")
        # Checks if user input is between 1-9
        if int(user_choice) > 9 or int(user_choice) < 1:
            raise ValueError("Your number is too high")
    except ValueError as e:
        print(f"Invalid input!! {e}.\n Please input a number between 1-9.")
        return False
    return True


def taken(coords, board):
    row = coords[0]
    column = coords[1]
    if board[row][column] != "-":
        print("Sorry this position is already taken try again")
        return True
    else:
        return False


def coordinates(zero_index):
    """
    Changes the users choice into coordinates
    to allow the programme to check if the space is
    already taken
    """
    row = int(zero_index / 3)
    column = zero_index
    if column > 2:
        column = int(column % 3)
    return (row, column)


def show_on_board(coords, board):
    row = coords[0]
    column = coords[1]
    board[row][column] = "X"


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
    print_board(board)
    user_choice = input("Enter a position between 1-9 or press 'q' to quit:")
    if quit_game(user_choice):
        print("Thanks for playing")
        break
    #  Code continues only if validate_input is true
    if not validate_input(user_choice):
        continue
    zero_index = int(user_choice) - 1
    coords = coordinates(zero_index)
    if taken(coords, board):
        print("This space is taken. Try again:")
        continue
    show_on_board(coords, board)