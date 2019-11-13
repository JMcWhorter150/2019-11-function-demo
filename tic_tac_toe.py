board = [[[], [], []],
[[], [], []],
[[], [], []]]
p1 = "X"
def print_board():
    print(board[0])
    print(board[1])
    print(board[2])
    print()

def move(board, location, player=p1):
    row, column = location
    if row not in range(3):
        raise NameError('Row outside tic-tac-toe range')
    elif column not in range(3):
        raise NameError('Column outside tic-tac-toe range')
    elif board[row][column] != []:
        raise NameError('Space already occupied')
    else:
        board[row][column].append(player)
        return board

def location_converter(number):
    number -= 1 #converting number to non-computer number
    tuple_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    return tuple_list[number]

def determine_location(player):
    user_location = int(input(f"""Where do you want to put your {player}? 
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
    if user_location < 1 or user_location > 10:
        raise NameError("You entered an invalid location.")
    return location_converter(user_location)

def place_player(player=p1):
    print_board()
    location = determine_location(player)
    return move(board, location, player)

def determine_win(player=p1):
    for i in range(3):
    # Checks rows for win
        if board[i][0] == [player] and board[i][1] == [player] and board[i][2] == [player]:
            print(f'Player {player} wins')
            raise ValueError
    # Checks columns for win
        elif board[0][i] == [player] and board[1][i] == [player] and board[2][i] == [player]:
            print(f'Player {player} wins')
            raise ValueError
    # Checks left diagonal
    if board[0][0] == [player] and board[1][1] == [player] and board[2][2] == [player]:
        print(f'Player {player} wins')
        raise ValueError
    # Checks right diagonal
    elif board[0][2] == [player] and board[1][1] == [player] and board[2][0] == [player]:
        print(f'Player {player} wins')
        raise ValueError

def clear_board():
    board = [[[], [], []],
    [[], [], []],
    [[], [], []]]
    return board
# location = (0, 0)
# player1 = "X"
# player2 = "Y"
p1 = input("Player 1, do you want to be X or Y? ")
if p1 != "X" and p1 != "Y":
    raise NameError("Entered something other than X or Y")
if p1 == "X":
    p2 = "Y"
else:
    p2 = "X"
while True:
    try:
        place_player(p1)
        determine_win(p1)
        place_player(p2)
        determine_win(p2)
    except NameError:
        print("You broke the game.")
        break
    except ValueError:
        play_again = input("Do you want to play again? (Y/N) ")
        if play_again == "N":
            break
        else:
            board = clear_board()


# Todo: Figure out why I can't clear the board after each game