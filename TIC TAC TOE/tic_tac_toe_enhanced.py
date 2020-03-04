# TIC TAC TOE game
import sys
import random
from IPython.display import clear_output

# Welcome message
def welcome_message(board):
    clear_output()
    print(">>>>>>----TIC-TAC-TOE----<<<<<<<")
    draw_board(['X',1,2,3,4,5,6,7,8,9],"")
    print("GAME DESCRIPTION: Tic-tac-toe (American English), noughts and crosses (British English),\
    or Xs and Os is a paper-and-pencil game for two players, X and O, who take turns marking the spaces\
    in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, \
    or diagonal row is the winner.\n\n\
    The numbers 1-9 indicate the cell positions (analogous to the numpad of a keyboard) over the board.\n\n")

def draw_board(board, op):
    print("\t    |    |   ")
    print(f"\t {board[7]}  | {board[8]}  |{board[9]}   ")
    print("\t    |    |   ")
    print("\t--------------")
    print("\t    |    |   ")
    print(f"\t {board[4]}  | {board[5]}  |{board[6]}   ")
    print("\t    |    |   ")
    print("\t--------------")
    print("\t    |    |   ")
    print(f"\t {board[1]}  | {board[2]}  |{board[3]}   ")
    print("\t    |    |   ")
    
    if op == "X":
        return "O"
    elif op == "O":
        return "X"

# Ask the player to choose a symbol for the game to begin
def marker_option():
    marker = " "
    while marker != "X" and marker != "O":
        marker = input("Please choose a marker (X or O):")
        clear_output()
    return marker

# Select the player to go first, randomly
def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return "PLAYER 1"
    else:
        return "PLAYER 2"

# Check if the players are ready
def ready_check():
    return input("Are you ready to play? (YES/yes to continue): ").upper() == "YES"

# Input validation
def is_valid(inp,board):
    return inp in ['1','2','3','4','5','6','7','8','9']

# Take input from the players
def take_player_input(board):
    inp = input("Enter your position (1-9): ")
    if is_valid(inp,board):
        # SPACE CHECK: Check if the cell is empty, if yes then valid input
        if board[int(inp)] == " ":
            return int(inp)
        else:
            print(f"The cell {int(inp)} is already filled")
            return 0
    else:
        clear_output()
        print("Invalid input...TRY AGAIN!!!")
        return 0

# Check game winning conditions (there are 8 win conditions for both players)
def is_game_over(op, board):
    if (board[1] == board[2] == board[3] == op) or (board[1] == board[4] == board[7] == op) or\
        (board[1] == board[5] == board[9] == op) or (board[2] == board[5] == board[8] == op) or\
        (board[3] == board[6] == board[9] == op) or (board[3] == board[5] == board[7] == op) or\
        (board[4] == board[5] == board[6] == op) or (board[7] == board[8] == board[9] == op):
        return op
    
def wanna_play_again():
    return input("Do you want to play another match? (YES/yes to continue): ")

# Run the game
def run_game():
    while True:
        # Create a dictionary (for positional mapping) for the board representation
        board = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

        # Welcome message on starting the game
        welcome_message(board)

        # Randomly select the player to go first
        print(f"{choose_first()} goes first\n\n")
        
        # Symbol selected by the first player
        op = marker_option()

        # Map the players according to the symbol chosen by the first players
        player_map = {"X":" ", "O":" "}
        if op == "X":
            player_map["X"] = "PLAYER 1"
            player_map["O"] = "PLAYER 2"
        elif op == "O":
            player_map["O"] = "PLAYER 1"
            player_map["X"] = "PLAYER 2"

        # If the players are ready
        if ready_check():
            clear_output()
            draw_board(board,"")
            i = 0
            while True:
                # At most 9 loops...the board is full and nobody has won; so its a draw
                if i == 9:
                    print("Its a DRAW\n\n")
                    break

                # Take input from one of the players
                pos = take_player_input(board)
                #print(f"position: {pos}")

                # Return control to the beginning of the loop when the input is invalid
                if pos == 0:
                    continue

                # Set the marker position on the board
                board[pos] = op
                
                # Store the current marker for checking the winning condition later
                cur_op = op

                
                # Draw the current board position and also store the new value of the symbol for the next player
                clear_output()
                op = draw_board(board, op)
                
                # Check if any winning condition is satisfied for any player
                player = is_game_over(cur_op, board)

                if player == "X":
                    print(f"{player_map[player]} wins...CONGRATULATIONS!!!\n\n")
                    break
                if player == 'O':
                    print(f"{player_map[player]} wins...CONGRATULATIONS!!!\n\n")
                    break

                # Increment only for legal inputs
                if pos is not None:
                    i += 1

        else:
            print("Game discontinued\n\n")
        
        # Check if the players want to continue playing
        if wanna_play_again().upper() != "YES":
            break
            
# run the game
run_game()
