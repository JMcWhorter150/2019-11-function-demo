# 1. Make a 3x3 board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# 2. Make a way to change the board

def move(board, location, player):
    row, column = location
    if board[row][column] != " ":
        print("That location is already taken.")
        count_change = 0
        return board, count_change
    elif row not in range(2) and column not in range(2):
        print("You have entered something outside the game board.")
        count_change = 0
        return board, count_change
    else:
        board[row][column] = player
        count_change = 1
        return board, count_change

# 3. Make a way to print the board with line breaks    
def print_board():
    for i in range(len(board)):
        print(board[i])
# move(board, (0, 1), "X")
# print_board()
# 4. Make a way for to separate locations into constituent parts
def convert_location(index):
    locations = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    location = locations[index - 1]
    return location

# 5. Make win condition
def win_condition(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(f"Player {player} has won the game.")
        return False
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(f"Player {player} has won the game.")
        return False
    else:
        for i in range(2):
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                print(f"Player {player} has won the game.")
                return False
            elif board[i][0] == player and board[i][1] == player and board[i][2] == player:
                print(f"Player {player} has won the game.")
                return False
        return True
# Make clear board function
def clear_board():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board

#  Make location list/user input function
def user_location(player):
    while True:
        try:
            user_input = int(input(f"""Where does {player} want to move?
1. Top left
2. Top middle
3. Top right
4. Middle left
5. Middle middle
6. Middle right
7. Bottom left
8. Bottom middle
9. Bottom right

"""))
        except ValueError:
            print("Please enter a number between one and nine.")
        if user_input not in range(1, 9):
            print("Please enter a number between one and nine.")
        else:
            break
    return user_input

# Make actual game loop
playing = True
while playing:
    count = 0
    p1 = "X"
    p2 = "Y"
    make_move = True
    print("Tic-tac-toe!")
    while count <= 8 and make_move == True:
        if count % 2 == 0:
            player = p1
        else:
            player = p2
        print_board()
        space = convert_location(user_location(player))
        board, count_change = move(board, space, player)
        make_move = win_condition(board, player)
        count += count_change

# Tie function
    if count == 9:
        print("The game is a tie!")

    if input("If you want to play again, type yes. ") != "yes":
        print("Thank you for playing tic-tac-toe")
        playing = False
    else:
        print("Lets play again!")
        clear_board()







#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
