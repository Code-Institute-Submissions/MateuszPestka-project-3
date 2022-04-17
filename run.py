"""
Tic Tac Toe game

Creats a board like this:
[
  [x, -, -],
  [-, -, -],
  [-, -, -]
]
User Choeses a number between 1 -9
Check if the input is valid and on the board raising ValueError
Show the input on the baord
Check if the user has won
Change between users X and O
"""

board = [["-" for r in range(3)] for c in range(3)]

user = True  # When user is true X when false O

turns = 0


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
    """
    Used to check if the slot is already taken by the user or another user
    """
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


def show_on_board(coords, board, current_user):
    """
    Shows the move on the board. X for user and O for computer
    """
    row = coords[0]
    column = coords[1]
    board[row][column] = current_user


def player(user):
    """
    Allows switch from X's and O's depending on user
    """
    if user:
        return "X"
    else:
        return "O"


def win(user, board):
    """
    Defines the conditions required to win the game.
    Three X's or O's in either a horizontal, vertical or
    diagonal position.
    """
    if check_row(user, board):
        return True
    if check_column(user, board):
        return True
    if check_diagonal(user, board):
        return True
    return False


def check_row(user, board):
    """
    Checks if a row is complete.
    If row is NOT complete it returns false and breaks out of the loop
    If row is complete user wins
    """
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False


def check_column(user, board):
    """
    Check if the user won by filing a column
    If the user has connects three of his symbols in any direction they win
    """
    for column in range(3):
        complete_column = True
        for row in range(3):
            if board[row][column] != user:
                complete_column = False
                break
        if complete_column:
            return True
    return False


def check_diagonal(user, board):
    """
    Checks if the user won diagonally.
    There are only two ways the user can win diagonally.
    """
    if board[0][0] == user and board[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    else:
        return False


while turns < 9:
    current_user = player(user)
    print_board(board)
    user_choice = input("Enter a position between 1-9 or press 'q' to quit:\n")
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
    show_on_board(coords, board, current_user)
    if win(current_user, board):
        print_board(board)
        print(f"Congratulations {current_user} Won!")
        break

    turns += 1
    if turns == 9:
        print_board(board)
        print("Its a tie! Try a rematch!")
    user = not user
