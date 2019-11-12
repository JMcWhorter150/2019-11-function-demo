board = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]
# print(board[0][0])
# print(board[2][2])

location = (0, 0)
player1 = "X"
player2 = "Y"
def move(board, location, player):
    row, column = location
    board[row][column].append(player)
    print(board)
    return board

print(move(board, location, player1))