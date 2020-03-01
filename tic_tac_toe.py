# TIC TAC TOE game
import sys

# Welcome message
def welcome_message(board):
    print(">>>>>>----TIC TAC TOE----<<<<<<<")
    draw_board(board,"")

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
        return "0"
    elif op == "0":
        return "X"

# Ask the player to choose a symbol for the game to begin
def symbol_option():
    return input("Please choose a symbol (X or 0): ")

# Check if the players are ready
def ready_check():
    return input("Are you ready to play? (YES/yes to continue)").upper() == "YES"

# Input validation
def is_valid(inp):
    return inp in ['1','2','3','4','5','6','7','8','9']

# Take input from the players
def take_player_input():
    inp = input("Enter your position (1-9): ")
    if is_valid(inp):
        return int(inp)
    else:
        print("Invalid input...TRY AGAIN!!!")
        return 0

# Check game winning conditions (there are 8 win conditions for both players)
def is_game_over(board):
    if (board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or\
        (board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or\
        (board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or (board[3] == 'X' and board[5] == 'X' and board[7] == 'X') or\
        (board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or (board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
        return "X"
    if (board[1] == '0' and board[2] == '0' and board[3] == '0') or (board[1] == '0' and board[4] == '0' and board[7] == '0') or\
        (board[1] == '0' and board[5] == '0' and board[9] == '0') or (board[2] == '0' and board[5] == '0' and board[8] == '0') or\
        (board[3] == '0' and board[6] == '0' and board[9] == '0') or (board[3] == '0' and board[5] == '0' and board[7] == '0') or\
        (board[4] == '0' and board[5] == '0' and board[6] == '0') or (board[7] == '0' and board[8] == '0' and board[9] == '0'):
        return "0"

# Run the game
def run_game():
    # Create a dictionary (for positional mapping) for the board representation
    board = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
    
    # Welcome message on starting the game
    welcome_message(board)
    
    # Symbol selected by the first player
    op = symbol_option()
    print("PLAYER 1 goes first")
    
    # Map the players according to the symbol chosen by the first players
    player_map = {"X":" ", "0":" "}
    if op == "X":
        player_map["X"] = "PLAYER 1"
        player_map["0"] = "PLAYER 2"
    elif op == "0":
        player_map["0"] = "PLAYER 1"
        player_map["X"] = "PLAYER 2"
    
    # If the players are ready
    if ready_check():
        draw_board(board,"")
        i = 0
        while True:
            # At most 9 loops
            if i == 9:
                print("Its a DRAW")
                break
                
            # Take input from one of the players
            pos = take_player_input()
            #print(f"position: {pos}")
            
            # Return control to the beginning of the loop when the input is invalid
            if pos == 0:
                continue
            
            # Set the position on the board
            board[pos] = op
            
            # Draw the current board position and also store the new value of the symbol for the next player
            op = draw_board(board, op)
            
            # Check if any winning condition is satisfied for any player
            player = is_game_over(board)
            
            if player == "X":
                print(f"{player_map[player]} wins")
                break
            if player == '0':
                print(f"{player_map[player]} wins")
                break
            
            # Increment only for legal inputs
            if pos is not None:
                i += 1
                
    else:
        print("Game discontinued")
        
# Run the game
run_game()
