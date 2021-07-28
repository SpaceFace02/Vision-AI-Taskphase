import sys
frame = ["_", "_", "_",
        "_", "_", "_",
        "_", "_", "_" ]

# Variable to check whether game is ongoing
ongoing_game = True

# To Cycle the current player
current_player = "X"

# Starting winner
winner = None

# Show the frame properly
def show_screen():
    print(f"{frame[0]} | {frame[1]} | {frame[2]}")
    print(f"{frame[3]} | {frame[4]} | {frame[5]}")
    print(f"{frame[6]} | {frame[7]} | {frame[8]}")

def tictactoe():

    while ongoing_game:
        show_screen()
        get_input(current_player)
        is_game_over()
        change_turn()

        if (winner == "X" or winner == "O"):
            show_screen()
            print(f"Winner is {winner}")
            break

def get_input(current_player):

    # Input Position
    print(f"{current_player}'s turn")

    # Error Checking
    valid_flag = False
    while valid_flag == False:
        position = input("Integer from 1 to 9: ")
        if (position.isalpha() or position.isspace() or position == ""):
            print("Enter a number!")
        else:
            # 0 indexing
            position = int(position) - 1

        if (position in range(9)):
            if (frame[position] == "_"):
                valid_flag = True
                frame[position] = current_player
            else:
                print("Enter valid position")

        if (position not in range(9)):
            print("Enter valid integer")
        

def is_game_over():
    is_game_won()
    is_game_tie()
    return

def is_game_tie():
    # No dashes left on frame
    if ("_" not in frame and winner == None):
        global ongoing_game
        ongoing_game = False
        print("TIE!")
        sys.exit()
        

def change_turn():
    # Current Player
    global current_player
    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

def is_game_won():
# A lot of if statements to check for rows, columns and diagonals, so modularizing it.
    check_rows()
    check_columns()
    check_diagonals()
    return

def check_rows():
    # Checking if any rows return true
    row_top = frame[0] == frame[1] == frame[2] != "_"
    row_middle = frame[3] == frame[4] == frame[5] != "_"
    row_bottom = frame[6] == frame[7] == frame[8] != "_"

    if (row_top | row_bottom | row_middle):
        global ongoing_game
        global winner
        ongoing_game = False

    if (row_top):
        winner = frame[0]
        return winner

    if (row_middle):
        winner = frame[3]
        return winner

    if (row_bottom):
        winner = frame[6]
        return winner
    return

def check_columns():
    # Checking if any rows return true
    column_left = frame[0] == frame[3] == frame[6] != "_"
    column_middle = frame[1] == frame[4] == frame[7] != "_"
    column_right = frame[2] == frame[5] == frame[8] != "_"

    if (column_left | column_right | column_middle):
        global ongoing_game
        global winner
        ongoing_game = False

    if (column_left):
        winner = frame[0]
        return winner

    if (column_middle):
        winner = frame[1]
        return winner

    if (column_right):
        winner = frame[2]
        return winner
    return

def check_diagonals():
    # Checking if any rows return true
    diag_one = frame[0] == frame[4] == frame[8] != "_"
    diag_two = frame[2] == frame[4] == frame[6] != "_"

    if (diag_one | diag_two):
        global ongoing_game
        global winner
        ongoing_game = False

    if (diag_one):
        winner = frame[0]
        return winner

    if (diag_two):
        winner = frame[2]
        return winner
    return


tictactoe()